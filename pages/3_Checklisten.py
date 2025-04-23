import streamlit as st
import pandas as pd
from datetime import datetime
import os
from utils.data_manager import DataManager

st.set_page_config(page_title="Labor-Checkliste", layout="wide")

st.title("🔬 Labor-Checkliste")
st.markdown("Bitte füllen Sie die Checkliste vor und nach der Arbeit im Labor aus.\nFür jede Frage können Sie 'Ja', 'Nein' oder 'Teilweise' abhaken. Hinterlassen Sie ggf. eine Bemerkung.")

# CSS für bessere Darstellung
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

# DataManager initialisieren
history_file = st.secrets["storage"]["verlaufspfad"]
data_manager = DataManager()  # Singleton + internes fs handling

# Fragen vor der Arbeit
aufgaben_vor = [
    "Laborkittel angezogen?",
    "Festes Schuhwerk angezogen?",
    "Evtl. Schutzbrille und Schutzmaske angezogen?",
    "Hände gewaschen/desinfiziert?",
    "Desinfektionsmittel verfügbar und aufgefüllt?",
    "Handschuhe griffbereit?",
    "Arbeitsplatz steril?",
    "Benötigten Reagenzien bereitgestellt?",
    "Verbrauchsmaterialien aufgefüllt: Pipettenspitzen, Röhrchen, Handschuhe, Schutzmasken?",
    "Geräte kalibriert oder deren Stand-by-Modus geprüft?",
    "Benötigten Protokolle vorbereitet?",
    "Abfallbehälter leer?",
    "Tagesplan vollständig durchgelesen?",
    "Übergabeprotokoll gelesen?",
    "Notfallausrüstung vorhanden?"
]

# Fragen nach der Arbeit
aufgaben_nach = [
    "Alle Oberflächen desinfiziert?",
    "Reagenzien ordnungsgemäss zurückgestellt?",
    "Alle Geräte ausgeschaltet oder in Stand-by gesetzt?",
    "Notwendige Wartung dokumentiert?",
    "Verbrauch von Materialien nachgetragen?",
    "Bioabfälle separat entsorgt?",
    "Abfallbehälter geleert?",
    "Fehlende Ergebnisse geprüft?",
    "Übergabeprotokoll ausgefüllt?",
    "Handschuhe ausgezogen und entsorgt?",
    "Laborkittel ausgezogen?",
    "Evtl. Schutzbrille und Schutzmaske ausgezogen?",
    "Hände gründlich gewaschen/desinfiziert?"
]

# Funktion zur Erstellung der Checkliste
def render_checklist(tasks, key):
    df = pd.DataFrame({
        "Frage": tasks,
        "Ja": [False] * len(tasks),
        "Nein": [False] * len(tasks),
        "Teilweise": [False] * len(tasks),
        "Bemerkung": ["" for _ in tasks]
    })
    return st.data_editor(df, num_rows="fixed", use_container_width=True, key=key)

# Benutzername-Eingabe
user = st.text_input("Name der Person, die die Checkliste ausfüllt")

st.markdown("### 🧑‍🔬 Vor der Arbeit")
df_vor = render_checklist(aufgaben_vor, "check_vor")

st.markdown("### 📋 Nach der Arbeit")
df_nach = render_checklist(aufgaben_nach, "check_nach")

# Speichern der Ergebnisse mit DataManager
if st.button("✅ Checkliste abschließen"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_vor["Zeit"] = timestamp
    df_nach["Zeit"] = timestamp
    df_vor["Benutzer"] = user
    df_nach["Benutzer"] = user
    df_vor["Bereich"] = "Vor der Arbeit"
    df_nach["Bereich"] = "Nach der Arbeit"

    df_combined = pd.concat([df_vor, df_nach], ignore_index=True)

    for _, row in df_combined.iterrows():
        data_manager.append_record(session_state_key="verlauf_df", record_dict=row.to_dict())

    st.success("Checkliste erfolgreich gespeichert!")

# Verlauf anzeigen
st.markdown("### 📜 Verlaufshistorie")
data_manager.load_app_data("verlauf_df", "checkliste_verlauf.csv", initial_value=pd.DataFrame())
verlauf_df = st.session_state["verlauf_df"]
st.dataframe(verlauf_df, use_container_width=True)

