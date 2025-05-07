import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Statistik der Checkliste")
st.markdown("Diese Seite zeigt die Verteilung der Antworten (Ja, Nein, Teilweise) pro Aufgabe über mehrere Tage.")

# Beispiel: Ersetze dies mit echten Daten aus Checkliste oder st.session_state
data = {
    "Datum": [
        "2025-05-01", "2025-05-01", "2025-05-01",
        "2025-05-02", "2025-05-02", "2025-05-02",
        "2025-05-03", "2025-05-03", "2025-05-03",
        "2025-05-03", "2025-05-03"
    ],
    "Aufgabe": [
        "Handschuhe gewechselt", "Laborkittel angezogen", "Arbeitsfläche desinfiziert",
        "Handschuhe gewechselt", "Laborkittel angezogen", "Arbeitsfläche desinfiziert",
        "Handschuhe gewechselt", "Laborkittel angezogen", "Arbeitsfläche desinfiziert",
        "Handschuhe gewechselt", "Laborkittel angezogen"
    ],
    "Antwort": [
        "Ja", "Nein", "Ja",
        "Ja", "Ja", "Teilweise",
        "Nein", "Ja", "Ja",
        "Ja", "Teilweise"
    ]
}
df = pd.DataFrame(data)
df["Datum"] = pd.to_datetime(df["Datum"])

# Gruppieren: Alle Antworten pro Aufgabe zählen
stats = df.groupby(["Aufgabe", "Antwort"]).size().unstack(fill_value=0)

# Gestapeltes Balkendiagramm
st.subheader("Antwortverteilung pro Aufgabe")
fig, ax = plt.subplots(figsize=(10, 6))
stats.plot(kind="barh", stacked=True, ax=ax)
ax.set_xlabel("Anzahl")
ax.set_ylabel("Aufgabe")
ax.set_title("Gestapelte Antworten: Ja / Nein / Teilweise")
ax.grid(axis='x', linestyle='--', alpha=0.6)
st.pyplot(fig)