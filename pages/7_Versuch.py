from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Labor-Checkliste", layout="wide")

from utils.data_manager import DataManager
from utils.helpers import set_vollbild_hintergrund_url

# ===== Init Block =====
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Lab_Safety")
login_manager = LoginManager(data_manager)

data_manager.load_app_data(
    session_state_key="logbuch_df",
    file_name="logbuch.csv",
    initial_value=pd.DataFrame(columns=["Name", "Datum", "Uhrzeit", "Zeitpunkt", "Frage", "Antwort", "Bemerkung"])
)

logbuch_df = st.session_state["logbuch_df"]

# ===== Login prüfen =====
username = st.session_state.get("user") or st.session_state.get("username")
if not username:
    st.error("⛔ Bitte zuerst auf der Startseite einloggen.")
    st.stop()

# ===== UI Setup =====
st.title("🔬 Labor-Checkliste")
st.markdown(f"**Eingeloggt als:** {username}")
st.markdown("Bitte füllen Sie die Checkliste vor und nach der Arbeit im Labor aus.")

set_vollbild_hintergrund_url("https://www.kantar.com/-/media/project/kantar/global/articles/images/2022/how-to-create-a-questionnaire.jpg?h=614&iar=0&w=900&hash=C22436F9487A6B98889BDB3623FD6C84")

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

today_str = datetime.date.today().isoformat()
now_str = datetime.datetime.now().strftime("%H:%M:%S")

# ===== Funktionen =====
def load_existing_answers(zeitpunkt):
    return st.session_state["logbuch_df"][
        (st.session_state["logbuch_df"]["Name"] == username) &
        (st.session_state["logbuch_df"]["Datum"] == datetime.date.today()) &
        (st.session_state["logbuch_df"]["Zeitpunkt"] == zeitpunkt)
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

# ===== Speichern mit append_record =====
if st.button("💾 Checkliste speichern"):
    def extract_entries(df_input, zeitpunkt):
        for _, row in df_input.iterrows():
            antwort = "Ja" if row["Ja"] else "Nein" if row["Nein"] else "Teilweise" if row["Teilweise"] else ""
            if antwort:
                eintrag = {
                    "Name": username,
                    "Datum": today_str,
                    "Uhrzeit": now_str,
                    "Zeitpunkt": zeitpunkt,
                    "Frage": row["Frage"],
                    "Antwort": antwort,
                    "Bemerkung": row["Bemerkung"]
                }
                data_manager.append_record("logbuch_df", eintrag)

    extract_entries(df_vor, "vorher")
    extract_entries(df_nach, "nachher")
    st.success("✅ Checkliste wurde gespeichert!")

# ===== Filterbereich =====
st.markdown("---")
st.markdown("## 📅 Gespeicherte Checklisten durchsuchen")

filter_datum = st.date_input("Datum auswählen", datetime.date.today())
alle_namen = sorted(set(st.session_state["logbuch_df"]["Name"].unique()).union({username}))
filter_name = st.selectbox("Benutzer auswählen", options=["Alle"] + alle_namen)

df_logbuch = st.session_state["logbuch_df"]
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
            df_zeit = df_zeit.sort_values(by=["Name", "Frage", "Uhrzeit"])
            df_zeit["Bemerkung"] = df_zeit["Bemerkung"].fillna("-")

            def create_status(row):
                if row["Bemerkung"].strip() != "-":
                    return f"Needs review – {row['Uhrzeit']}"
                elif row["Datum"] == datetime.date.today():
                    return f"New – {row['Uhrzeit']}"
                else:
                    return f"Success – {row['Uhrzeit']}"

            df_zeit["Status"] = df_zeit.apply(create_status, axis=1)
            st.dataframe(
                df_zeit[["Name", "Frage", "Antwort", "Bemerkung", "Status"]],
                use_container_width=True
            )

# ===== Notfall-Balken =====
st.markdown("""
    <div style='position:fixed; bottom:0; left:0; width:100%; background-color:#d32f2f; color:white; padding:10px; font-weight:bold; text-align:center; z-index:1000;'>
        🚨 Notfallnummern: ZHAW 7070 | Ambulanz 144 | Polizei 117 | Feuerwehr 118 | REGA 1414 | Toxinfo 145
    </div>
""", unsafe_allow_html=True)