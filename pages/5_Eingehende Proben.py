import streamlit as st

st.set_page_config(page_title="Präanalytik-Pfad", layout="wide")

st.title("🧭 Präanalytik-Anleitung")

st.markdown("Dieser Pfad hilft dir, Schritt für Schritt zu prüfen, ob eine Probe weiterverarbeitet werden darf.")

# Schritt 1
antwort_1 = st.radio("📌 Ist der Auftrag vorhanden und vollständig ausgefüllt?", ["Ja", "Nein"])
if antwort_1 == "Nein":
    st.error("⛔ Bitte Auftrag anfordern oder klären. Prozess gestoppt.")
    st.stop()

# Schritt 2
antwort_2 = st.radio("📌 Stimmen Patientendaten auf Auftrag und Probe überein?", ["Ja", "Nein"])
if antwort_2 == "Nein":
    st.error("⛔ Daten stimmen nicht überein. Rücksprache mit Einsender erforderlich.")
    st.stop()

# Schritt 3
antwort_3 = st.radio("📌 Ist die Probe eindeutig beschriftet?", ["Ja", "Nein"])
if antwort_3 == "Nein":
    st.error("⛔ Keine eindeutige Kennzeichnung – nicht weiterverarbeiten.")
    st.stop()

# Schritt 4
antwort_4 = st.radio("📌 Ist das Probenmaterial vollständig und unversehrt?", ["Ja", "Nein"])
if antwort_4 == "Nein":
    st.warning("⚠️ Material unvollständig oder beschädigt. Rücksprache nötig.")
    st.stop()

# Schritt 5
antwort_5 = st.radio("📌 Ist das richtige Gefäss verwendet und Volumen ausreichend?", ["Ja", "Nein"])
if antwort_5 == "Nein":
    st.warning("⚠️ Material eventuell ungeeignet. Entscheidung je nach Analysebereich.")
    st.stop()

# Abschluss
st.success("✅ Alle Kriterien erfüllt. Die Probe kann an die Analytik weitergegeben werden.")

from utils.helpers import set_vollbild_hintergrund_url  # falls du eine helpers.py hast

# Falls du keine helpers.py hast, einfach Funktion direkt reinkopieren (siehe oben)

set_vollbild_hintergrund_url("https://cardinalhealth.scene7.com/is/image/corpmarketdms7prod/article-featured-2LAB22-2109113-simplifying-specimen-collection-59194963_l")

# --- Notfallleiste ---
from utils.helpers import zeige_notfallleiste
zeige_notfallleiste()