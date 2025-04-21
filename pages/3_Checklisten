import streamlit as st

st.set_page_config(page_title="Laborsicherheit & Hygiene", layout="centered")

st.title("🧪 Laborsicherheit & Hygiene Checkliste")

st.write("Bitte hake alle erledigten Aufgaben ab:")

# Aufgabenliste
tasks = {
    "Arbeitsplatz aufgeräumt": False,
    "Mikroskop gereinigt": False,
    "Abfälle korrekt entsorgt": False,
    "Oberflächen desinfiziert": False,
    "Geräte ausgeschaltet": False,
    "Chemikalien sicher verstaut": False,
    "Schutzhandschuhe entfernt": False,
    "Laborbuch aktualisiert": False,
}

# Checkboxen anzeigen
completed_tasks = []
for task in tasks:
    if st.checkbox(task):
        completed_tasks.append(task)

# Zusammenfassung
st.markdown("---")
st.subheader("✅ Erledigte Aufgaben:")

if completed_tasks:
    for done in completed_tasks:
        st.markdown(f"- {done}")
else:
    st.info("Noch keine Aufgaben abgehakt.")

# Optional: Button zur Rückmeldung
if st.button("Checkliste abgeschlossen"):
    if len(completed_tasks) == len(tasks):
        st.success("Alle Aufgaben erledigt – Gute Arbeit!")
    else:
        st.warning("Nicht alle Aufgaben sind abgehakt.")
