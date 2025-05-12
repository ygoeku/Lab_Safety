import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Labor-Checkliste", layout="wide")

from utils.data_manager import DataManager
from utils.login_manager import LoginManager
from utils.helpers import set_vollbild_hintergrund_url

# ===== Init Block =====
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Lab_Safety")
login_manager = LoginManager(data_manager)

# Immer CSV laden + registrieren
dh = data_manager._get_data_handler()
logbuch_df = dh.load(
    "logbuch.csv",
    initial_value=pd.DataFrame(columns=["Name", "Datum", "Uhrzeit", "Zeitpunkt", "Frage", "Antwort", "Bemerkung"])
)
st.session_state["logbuch_df"] = logbuch_df
data_manager.app_data_reg["logbuch_df"] = "logbuch.csv"

# ===== Login überprüfen =====
username = st.session_state.get("user") or st.session_state.get("username")
if not username:
    st.error("⛔ Bitte zuerst auf der Startseite einloggen.")
    st.stop()

# ===== UI Setup =====
st.title("🔬 Labor-Checkliste")
st.markdown(f"**Eingeloggt als:** {username}")
st.markdown("Bitte füllen Sie die Checkliste vor und nach der Arbeit im Labor aus.\nFür jede Frage können Sie 'Ja', 'Nein' oder 'Teilweise' abhaken. Hinterlassen Sie ggf. eine Bemerkung.")

set_vollbild_hintergrund_url("https://www.kantar.com/-/media/project/kantar/global/articles/images/2022/how-to-create-a-questionnaire.jpg?h=614&iar=0&w=900&hash=C22436F9487A6B98889BDB3623FD6C84")

st.markdown("""
    <style>
    .element-container:has(> div[data-testid="stDataEditorContainer"]) {
        overflow: visible !important;
    }
    table {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# ===== Fragen =====
aufgaben_vor = [
    "Laborkittel angezogen?", "Festes Schuhwerk angezogen?", "Evtl. Schutzbrille und Schutzmaske angezogen?",
    "Hände gewaschen/desinfiziert?", "Desinfektionsmittel verfügbar und aufgefüllt?", "Handschuhe griffbereit?",
    "Arbeitsplatz steril?", "Benötigten Reagenzien bereitgestellt?",
    "Verbrauchsmaterialien aufgefüllt: Pipettenspitzen, Röhrchen, Handschuhe, Schutzmasken?",
    "Geräte kalibriert oder deren Stand-by-Modus geprüft?", "Benötigten Protokolle vorbereitet?",
    "Abfallbehälter leer?", "Tagesplan vollständig durchgelesen?", "Übergabeprotokoll gelesen?", "Notfallausrüstung vorhanden?"
]

aufgaben_nach = [
    "Alle Oberflächen desinfiziert?", "Reagenzien ordnungsgemäss zurückgestellt?", "Alle Geräte ausgeschaltet oder in Stand-by gesetzt?",
    "Notwendige Wartung dokumentiert?", "Verbrauch von Materialien nachgetragen?", "Bioabfälle separat entsorgt?",
    "Abfallbehälter geleert?", "Fehlende Ergebnisse geprüft?", "Übergabeprotokoll ausgefüllt?", "Handschuhe ausgezogen und entsorgt?",
    "Laborkittel ausgezogen?", "Evtl. Schutzbrille und Schutzmaske ausgezogen?", "Hände gründlich gewaschen/desinfiziert?"
]

# Zeitdaten
today_str = datetime.date.today().isoformat()
now_str = datetime.datetime.now().strftime("%H:%M:%S")
logbuch_df = st.session_state["logbuch_df"]

# ===== Funktionen =====
def load_existing_answers(zeitpunkt):
    return logbuch_df[
        (logbuch_df["Name"] == username) &
        (logbuch_df["Datum"] == today_str) &
        (logbuch_df["Zeitpunkt"] == zeitpunkt)
    ].drop_duplicates(subset=["Frage"], keep="last")

def render_checklist_with_restore(tasks, key, zeitpunkt):
    existing_df = load_existing_answers(zeitpunkt)
    answers = []
    for frage in tasks:
        row = existing_df[existing_df["Frage"] == frage]
        if not row.empty:
            antwort = row.iloc[0]["Antwort"]
            bemerkung = row.iloc[0]["Bemerkung"]
            ja = antwort == "Ja"
            nein = antwort == "Nein"
            teilweise = antwort == "Teilweise"
        else:
            ja = nein = teilweise = False
            bemerkung = ""
        answers.append([frage, ja, nein, teilweise, bemerkung])
    df = pd.DataFrame(answers, columns=["Frage", "Ja", "Nein", "Teilweise", "Bemerkung"])
    return st.data_editor(df, num_rows="fixed", use_container_width=True, key=key)

# ===== Checkliste anzeigen =====
st.markdown("### 🧑‍🔬 Vor der Arbeit")
df_vor = render_checklist_with_restore(aufgaben_vor, "check_vor", "vorher")

st.markdown("### 📋 Nach der Arbeit")
df_nach = render_checklist_with_restore(aufgaben_nach, "check_nach", "nachher")

# ===== Speichern =====
if st.button("💾 Checkliste speichern"):
    rows = []

    existing_vor = load_existing_answers("vorher")
    existing_nach = load_existing_answers("nachher")

    def extract_rows(df_input, zeitpunkt, existing_df):
        for _, row in df_input.iterrows():
            frage = row["Frage"]
            bemerkung = row["Bemerkung"]
            antwort = "Ja" if row["Ja"] else "Nein" if row["Nein"] else "Teilweise" if row["Teilweise"] else ""

            if not antwort:
                old = existing_df[existing_df["Frage"] == frage]
                if not old.empty:
                    antwort = old.iloc[0]["Antwort"]
                    bemerkung = old.iloc[0]["Bemerkung"]

            if antwort:
                rows.append({
                    "Name": username,
                    "Datum": today_str,
                    "Uhrzeit": now_str,
                    "Zeitpunkt": zeitpunkt,
                    "Frage": frage,
                    "Antwort": antwort,
                    "Bemerkung": bemerkung
                })

    extract_rows(df_vor, "vorher", existing_vor)
    extract_rows(df_nach, "nachher", existing_nach)

    new_entries = pd.DataFrame(rows)

    combined = logbuch_df.copy()
    for _, new_row in new_entries.iterrows():
        mask = (
            (combined["Name"] == new_row["Name"]) &
            (combined["Datum"] == new_row["Datum"]) &
            (combined["Zeitpunkt"] == new_row["Zeitpunkt"]) &
            (combined["Frage"] == new_row["Frage"])
        )
        combined = combined[~mask]
    combined = pd.concat([combined, new_entries], ignore_index=True)

    st.session_state["logbuch_df"] = combined
    data_manager.save_data("logbuch_df")

    st.success("✅ Antworten gespeichert. Vorherige Einträge bleiben erhalten.")

# ===== Filterbereich =====
st.markdown("---")
st.markdown("## 📅 Gespeicherte Checklisten durchsuchen")

filter_datum = st.date_input("Datum auswählen", datetime.date.today())
alle_namen = sorted(set(logbuch_df["Name"].unique()).union({username}))
filter_name = st.selectbox("Benutzer auswählen", options=["Alle"] + alle_namen)

df_logbuch = st.session_state["logbuch_df"]

if not df_logbuch.empty:
    df_logbuch["Datum"] = pd.to_datetime(df_logbuch["Datum"]).dt.date
    df_filtered = df_logbuch[df_logbuch["Datum"] == filter_datum]

    if filter_name != "Alle":
        df_filtered = df_filtered[df_filtered["Name"] == filter_name]

    if df_filtered.empty:
        st.info("Keine Checklisten für dieses Datum gefunden.")
    else:
        for zeitpunkt in ["vorher", "nachher"]:
            df_zeit = df_filtered[df_filtered["Zeitpunkt"] == zeitpunkt]
            if not df_zeit.empty:
                st.markdown(f"### 🕒 Checkliste: {zeitpunkt.capitalize()}")

                # Duplikate entfernen (letzte Antwort pro Person + Frage behalten)
                df_zeit = df_zeit.drop_duplicates(subset=["Frage", "Name"], keep="last")

                # Nach Name und Frage sortieren
                df_zeit = df_zeit.sort_values(by=["Name", "Frage"])

                # Nur die wichtigen Spalten anzeigen
                st.dataframe(
                    df_zeit[["Name", "Frage", "Antwort", "Bemerkung"]],
                    use_container_width=True
                )
else:
    st.warning("Noch keine Daten im Logbuch gespeichert.")

st.markdown("""
    <div style='position:fixed; bottom:0; left:0; width:100%; background-color:#d32f2f; color:white; padding:10px; font-weight:bold; text-align:center; z-index:1000;'>
        🚨 Notfallnummern: ZHAW 7070 | Ambulanz 144 | Polizei 117 | Feuerwehr 118 | REGA 1414 | Toxinfo 145
    </div>
""", unsafe_allow_html=True)