import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("📋 Labor-Checklisten")

history_file = "/mnt/switch/checklisten/checkliste_verlauf.csv"

aufgaben_vor = [
    "Laborkittel angezogen?",
    "Festes Schuhwerk angezogen?",
    ...
]

aufgaben_nach = [
    "Alle Oberflächen desinfiziert?",
    ...
]

def render_checklist(tasks, key):
    df = pd.DataFrame({
        "Frage": tasks,
        "Ja": [False] * len(tasks),
        "Nein": [False] * len(tasks),
        "Teilweise": [False] * len(tasks),
        "Bemerkung": [""] * len(tasks)
    })
    return st.data_editor(df, num_rows="fixed", use_container_width=True, key=key)

user = st.text_input("Name der Person, die die Checkliste ausfüllt")

st.markdown("### 🧑‍🔬 Vor der Arbeit")
df_vor = render_checklist(aufgaben_vor, "check_vor")

st.markdown("### 📋 Nach der Arbeit")
df_nach = render_checklist(aufgaben_nach, "check_nach")

if st.button("✅ Checkliste abschließen"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_vor["Zeit"] = timestamp
    df_nach["Zeit"] = timestamp
    df_vor["Benutzer"] = user
    df_nach["Benutzer"] = user

    df_combined = pd.concat([
        df_vor.assign(Bereich="Vor der Arbeit"),
        df_nach.assign(Bereich="Nach der Arbeit")
    ])

    if os.path.exists(history_file):
        df_old = pd.read_csv(history_file)
        df_combined = pd.concat([df_old, df_combined], ignore_index=True)

    df_combined.to_csv(history_file, index=False)
    st.success("Checkliste erfolgreich gespeichert!")

if os.path.exists(history_file):
    st.markdown("### 📜 Verlaufshistorie")
    history_df = pd.read_csv(history_file)
    st.dataframe(history_df, use_container_width=True)

