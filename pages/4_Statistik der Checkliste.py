import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# Titel
st.title("📊 Erfolgsquote vor und nach der Arbeit")
st.markdown("""
Diese Seite zeigt die **Erfolgsquote („Ja“-Anteil)** getrennt für Aufgaben **vorher** und **nachher** – für ein gewähltes Datum.
""")

# 📅 Datumsauswahl
auswahl_datum = st.date_input("📅 Wähle ein Datum:", date.today())

# 🔐 Datenprüfung
if "logbuch_df" not in st.session_state or st.session_state["logbuch_df"].empty:
    st.warning("Noch keine Einträge im Logbuch gefunden.")
    st.stop()

df = st.session_state["logbuch_df"].copy()

# Formatieren & filtern
df["Datum"] = pd.to_datetime(df["Datum"]).dt.date
df_tag = df[df["Datum"] == auswahl_datum]

if df_tag.empty:
    st.info(f"ℹ️ Für den {auswahl_datum} wurden noch keine Einträge erfasst.")
    st.stop()

if "Zeitpunkt" not in df_tag.columns:
    st.error("❌ Die Spalte 'Zeitpunkt' fehlt im Datensatz.")
    st.stop()

# 💡 Flexible Filterung: „Vorher“ und „Nachher“
df_tag["Zeitpunkt"] = df_tag["Zeitpunkt"].astype(str).str.strip().str.lower()

df_vor = df_tag[df_tag["Zeitpunkt"].str.contains("vorher", case=False, na=False)]
df_nach = df_tag[df_tag["Zeitpunkt"].str.contains("nachher", case=False, na=False)]

# 📊 Funktion für Erfolgsquote
def zeichne_erfolgsquote(df_input, titel, farbe):
    if df_input.empty:
        st.info(f"Keine Daten für: {titel}")
        return

    gesamt = df_input.groupby("Frage").size()
    ja_anzahl = df_input[df_input["Antwort"] == "Ja"].groupby("Frage").size()
    prozent = (ja_anzahl / gesamt * 100).fillna(0).round(1).reset_index()
    prozent.columns = ["Aufgabe", "Erfolgsquote (%)"]
    prozent["Label"] = prozent["Erfolgsquote (%)"].astype(str) + " %"

    fig = px.bar(
        prozent,
        x="Aufgabe",
        y="Erfolgsquote (%)",
        text="Label",
        color_discrete_sequence=[farbe],
        title=titel
    )

    fig.update_traces(textposition="inside")
    fig.update_layout(
        yaxis=dict(ticksuffix=" %", range=[0, 110]),
        xaxis_tickangle=-45,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# 📊 Diagramme anzeigen
zeichne_erfolgsquote(df_vor, f"🕗 Erfolgsquote (Vorher) – {auswahl_datum}", "green")
zeichne_erfolgsquote(df_nach, f"🕓 Erfolgsquote (Nachher) – {auswahl_datum}", "blue")

# 📞 Notfallnummern
st.markdown("""
    <div style='position:fixed; bottom:0; left:0; width:100%; background-color:#d32f2f; color:white; padding:10px; font-weight:bold; text-align:center; z-index:1000;'>
        🚨 Notfallnummern: ZHAW 7070 | Ambulanz 144 | Polizei 117 | Feuerwehr 118 | REGA 1414 | Toxinfo 145
    </div>
""", unsafe_allow_html=True)