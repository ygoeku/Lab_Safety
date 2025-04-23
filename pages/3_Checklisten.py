import streamlit as st
import pandas as pd

st.set_page_config(page_title="Labor-Checkliste", layout="wide")

st.title("🔬 Labor-Checkliste")
st.markdown("Bitte füllen Sie die Checkliste vor und nach der Arbeit im Labor aus.\nWählen Sie für jede Frage, ob sie zutrifft, teilweise zutrifft oder nicht zutrifft.\nHinterlassen Sie ggf. eine Bemerkung.")

options = ["", "Ja", "Nein", "Teilweise"]

def render_checklist(title, tasks):
    st.subheader(title)
    checklist = []
    for task in tasks:
        cols = st.columns([4, 1, 1, 1, 3])
        cols[0].markdown(f"**{task}**")
        status = cols[1].radio("", options, key=task+"_status", label_visibility="collapsed")
        bemerkung = cols[4].text_input("Bemerkung", key=task+"_bem")
        checklist.append({
            "Aufgabe": task,
            "Status": status,
            "Bemerkung": bemerkung
        })
    return pd.DataFrame(checklist)

# Aufgaben vor der Arbeit (als Fragen formuliert)
aufgaben_vor = [
    "Laborkittel angezogen?",
    "Festes Schuwerk angezogen?",  
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
    "Übergabeprotkoll ausgefüllt?",
    "Handschuhe ausgezogen und entsorgt?",
    "Laborkittel ausgezogen?",
    "Evtl. Schutzbrille und Schutzmaske ausgezogen?",
    "Hände gründlich gewaschen/desinfiziert?"
]

# Checklisten anzeigen
with st.expander("🧪 Vor der Arbeit"):
    df_vor = render_checklist("Checkliste vor der Arbeit", aufgaben_vor)

with st.expander("🧼 Nach der Arbeit"):
    df_nach = render_checklist("Checkliste nach der Arbeit", aufgaben_nach)

# Ergebnisse anzeigen
if st.button("✅ Checkliste abschließen"):
    st.success("Checkliste erfolgreich ausgefüllt!")
    st.write("### Ergebnisse - Vor der Arbeit")
    st.dataframe(df_vor)
    st.write("### Ergebnisse - Nach der Arbeit")
    st.dataframe(df_nach)

