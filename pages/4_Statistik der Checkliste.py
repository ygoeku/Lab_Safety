import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Statistik der Checkliste")
st.markdown("Diese Seite zeigt die Verteilung von *Ja / Nein / Teilweise* pro Frage über alle gespeicherten Checklisten.")

# Prüfen, ob Logbuch vorhanden ist
if "logbuch_df" not in st.session_state or st.session_state["logbuch_df"].empty:
    st.warning("Noch keine Einträge im Logbuch gefunden.")
    st.stop()

# Lade Logbuch-Daten
df = st.session_state["logbuch_df"].copy()

# Datum zu DateTime umwandeln (für spätere Filteroptionen)
df["Datum"] = pd.to_datetime(df["Datum"])

# Gruppiere: Frage × Antwort → Zähle Häufigkeit
antworten_stats = df.groupby(["Frage", "Antwort"]).size().unstack(fill_value=0)

# Sortiere nach Gesamtzahl der Antworten
antworten_stats["Gesamt"] = antworten_stats.sum(axis=1)
antworten_stats = antworten_stats.sort_values(by="Gesamt", ascending=False).drop(columns="Gesamt")

# Zeichne gestapeltes Balkendiagramm
st.subheader("Antwortverteilung pro Aufgabe (alle Tage)")

fig, ax = plt.subplots(figsize=(10, 8))
antworten_stats.plot(kind="barh", stacked=True, ax=ax)
ax.set_xlabel("Anzahl")
ax.set_ylabel("Frage")
ax.set_title("Verteilung der Antworten: Ja / Nein / Teilweise")
ax.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
    <div style='position:fixed; bottom:0; left:0; width:100%; background-color:#d32f2f; color:white; padding:10px; font-weight:bold; text-align:center; z-index:1000;'>
        🚨 Notfallnummern: ZHAW 7070 | Ambulanz 144 | Polizei 117 | Feuerwehr 118 | REGA 1414 | Toxinfo 145
    </div>
""", unsafe_allow_html=True)