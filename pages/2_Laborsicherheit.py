import streamlit as st
import os

# Setze hier deinen absoluten Bildpfad!
BILDER_ORDNER = r"C:/Users/elena/OneDrive/Desktop/signale"

# Hilfsfunktion zum Laden der Bilder
def bild_mit_info(dateiname, titel, beschreibung):
    bildpfad = os.path.join(BILDER_ORDNER, dateiname)
    if os.path.exists(bildpfad):
        with st.container():
            st.image(bildpfad, width=150)
            if st.button(f"ℹ️ Mehr erfahren über {titel}", key=titel):
                st.info(beschreibung)
    else:
        st.error(f"Bild '{dateiname}' nicht gefunden!")

# --- Haupttitel ---
st.markdown("<h1 style='text-align: center; color: #2E8BFF;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

# --- Erster Bereich: tägliches Arbeiten ---
with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("augenschutz.jpg", "Schutzbrille", "Schutzbrillen verhindern Augenschäden.")
    with col2:
        bild_mit_info("handschutz.jpg", "Handschutz", "Schutzhandschuhe verhindern Hautkontakt mit Chemikalien.")
    with col3:
        bild_mit_info("labormantel.jpg", "Labormantel", "Labormantel schützt Kleidung und Haut.")
    with col4:
        bild_mit_info("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor dürfen keine Lebensmittel konsumiert werden.")

# --- Abstand ---
st.markdown("<hr>", unsafe_allow_html=True)

# --- Zweiter Bereich: Notfallsituation ---
st.markdown("<h1 style='text-align: center; color: #FF4500;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

with st.expander("🚨 Symbole zu beachten in Notfallsituationen", expanded=True):
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        bild_mit_info("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Im Notfall Augen sofort ausspülen.")
    with col6:
        bild_mit_info("erste_hilfe_start.jpg", "Erste Hilfe", "Sofort Erste Hilfe Maßnahmen einleiten.")
    with col7:
        bild_mit_info("notausgang.jpg", "Notausgang", "Den nächsten Notausgang benutzen.")
    with col8:
        bild_mit_info("notruftelefon.jpg", "Notruftelefon", "Notrufnummer für schnelle Hilfe kontaktieren.")