import streamlit as st
import pandas as pd

st.set_page_config(page_title="Labor-Checkliste", layout="wide")

st.title("🔬 Labor-Checkliste")
st.markdown("Bitte füllen Sie die Checkliste vor und nach der Arbeit im Labor aus.\nFür jede Frage können Sie 'Ja', 'Nein' oder 'Teilweise' abhaken. Hinterlassen Sie ggf. eine Bemerkung.")

def render_checklist(title, tasks):
    st.subheader(title)
    df = pd.DataFrame({
        "Frage": tasks,
        "Ja": [False] * len(tasks),
        "Nein": [False] * len(tasks),
        "Teilweise": [False] * len(tasks),
        "Bemerkung": [""] * len(tasks)
    })
    edited_df = st.data_editor(df, num_rows="fixed", use_container_width=True, key=title)
    return edited_df

# Aufgaben vor der Arbeit (als Fragen formuliert)
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

# Aufgaben nach der Arbeit (als Fragen formuliert)
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

# Checklisten anzeigen
with st.expander("🧪 Checkliste vor der Arbeit", expanded=True):
    df_vor = render_checklist("vor", aufgaben_vor)

with st.expander("🧼 Checkliste nach der Arbeit", expanded=True):
    df_nach = render_checklist("nach", aufgaben_nach)

# Ergebnisse anzeigen
if st.button("✅ Checkliste abschließen"):
    st.success("Checkliste erfolgreich ausgefüllt!")
    st.write("### Ergebnisse - Vor der Arbeit")
    st.dataframe(df_vor)
    st.write("### Ergebnisse - Nach der Arbeit")
    st.dataframe(df_nach)
