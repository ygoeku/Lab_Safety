import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="Labor-Checkliste", layout="wide")

from utils.data_manager import DataManager
from utils.login_manager import LoginManager
from utils.helpers import set_vollbild_hintergrund_url

# ===== Init Block =====
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Lab_Safety")
login_manager = LoginManager(data_manager)

data_manager.load_app_data(
    session_state_key='logbuch_df',
    file_name='logbuch.csv',
    initial_value=pd.DataFrame(columns=["Name", "Datum", "Uhrzeit", "Zeitpunkt", "Frage", "Antwort", "Bemerkung"]),
)

# ===== Login überprüfen =====
username = st.session_state.get("user")
if not username:
    st.error("⛔ Bitte zuerst auf der Startseite einloggen.")
    st.stop()

# ===== UI Setup =====
st.title("🔬 Labor-Checkliste")
st.markdown(f"**Eingeloggt als:** `{username}`")
st.markdown("Bitte füllen Sie die Checkliste vor und nach der Arbeit im Labor aus.\nFür jede Frage können Sie 'Ja', 'Nein' oder 'Teilweise' abhaken. Hinterlassen Sie ggf. eine Bemerkung.")

set_vollbild_hintergrund_url("https://www.kantar.com/-/media/project/kantar/global/articles/images/2022/how-to-create-a-questionnaire.jpg?h=614&iar=0&w=900&hash=C22436F9487A6B98889BDB3623FD6C84")

st.markdown("""
    <style>
    .element-container:has(> div[data-testid=\"stDataEditorContainer\"]) {
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
    ]

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

    def extract_rows(df, zeitpunkt):
        for _, row in df.iterrows():
            antwort = "Ja" if row["Ja"] else "Nein" if row["Nein"] else "Teilweise" if row["Teilweise"] else ""
            rows.append({
                "Name": username,
                "Datum": today_str,
                "Uhrzeit": now_str,
                "Zeitpunkt": zeitpunkt,
                "Frage": row["Frage"],
                "Antwort": antwort,
                "Bemerkung": row["Bemerkung"]
            })

    extract_rows(df_vor, "vorher")
    extract_rows(df_nach, "nachher")

    new_entries = pd.DataFrame(rows)
    st.session_state["logbuch_df"] = pd.concat([logbuch_df, new_entries], ignore_index=True)

    data_manager.save_data("logbuch_df")

    st.success("✅ Checkliste erfolgreich gespeichert!")

# ===== Filterbereich =====
st.markdown("---")
st.markdown("## 📅 Gespeicherte Checklisten durchsuchen")

filter_datum = st.date_input("Datum auswählen", datetime.date.today())

# Alle Namen im Dropdown (inkl. "Alle")
alle_namen = sorted(logbuch_df["Name"].unique()) if not logbuch_df.empty else []
filter_name = st.selectbox("Benutzer auswählen", options=["Alle"] + alle_namen)

df_logbuch = st.session_state["logbuch_df"]
st.write("Verfügbare Benutzerdaten:", logbuch_df["Name"].unique())

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
                df_pivot = df_zeit.pivot(index="Frage", columns="Name", values=["Antwort", "Bemerkung"])
                st.dataframe(df_pivot, use_container_width=True)
else:
    st.warning("Noch keine Daten im Logbuch gespeichert.")