import streamlit as st
import pandas as pd

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

# Hinweis statt Speicherung
if st.button("✅ Checkliste abschließen"):
    st.success("Checkliste abgeschlossen (wird nicht gespeichert).")

