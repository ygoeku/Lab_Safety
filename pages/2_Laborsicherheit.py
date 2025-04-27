import streamlit as st
import os

# Setze hier deinen absoluten Bildpfad!
BILDER_ORDNER = r"C:/Users/elena/OneDrive/Desktop/signale"

# Hilfsfunktion zum Laden der Bilder
def bild_mit_info(dateiname, beschreibung, key_suffix):
    bildpfad = os.path.join(BILDER_ORDNER, dateiname)
    if os.path.exists(bildpfad):
        with st.container():
            st.image(bildpfad, width=150)
            if st.button("ℹ️ Mehr erfahren", key=f"info_{key_suffix}"):
                st.info(beschreibung)
    else:
        st.error(f"Bild '{dateiname}' nicht gefunden!")

# --- Haupttitel ---
st.markdown("<h1 style='text-align: center; color: #2E8BFF;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

# --- Erster Bereich: tägliches Arbeiten ---
with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info(
            "augenschutz.jpg",
            "Schutzbrillen verhindern Verletzungen der Augen beim Arbeiten mit Chemikalien oder gefährlichen Stoffen.",
            "schutzbrille"
        )
    with col2:
        bild_mit_info(
            "handschutz.jpg",
            "Schutzhandschuhe schützen die Haut vor Chemikalien, biologischen Stoffen und mechanischen Gefahren.",
            "handschutz"
        )
    with col3:
        bild_mit_info(
            "labormantel.jpg",
            "Ein Labormantel schützt die Haut und Kleidung vor Spritzern und Verunreinigungen.",
            "labormantel"
        )
    with col4:
        bild_mit_info(
            "essen_und_trinken_verboten.jpg",
            "Im Labor ist Essen und Trinken verboten, um Kontamination und Vergiftungen zu verhindern.",
            "essen_verboten"
        )

# --- Abstand ---
st.markdown("<hr>", unsafe_allow_html=True)

# --- Zweiter Bereich: Notfallsituation ---
st.markdown("<h1 style='text-align: center; color: #FF4500;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

with st.expander("🚨 Symbole zu beachten in Notfallsituationen", expanded=True):
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        bild_mit_info(
            "Augenspüleinrichtung.jpg",
            "Die Augenspüleinrichtung ermöglicht es, gefährliche Substanzen schnell aus den Augen zu spülen.",
            "augenspuele"
        )
    with col6:
        bild_mit_info(
            "erste_hilfe_start.jpg",
            "Das Erste-Hilfe-Symbol weist auf wichtige Einrichtungen und Ausrüstung für medizinische Notfälle hin.",
            "erstehilfe"
        )
    with col7:
        bild_mit_info(
            "notausgang.jpg",
            "Der Notausgang zeigt den schnellsten Fluchtweg im Falle eines Brandes oder einer Evakuierung an.",
            "notausgang"
        )
    with col8:
        bild_mit_info(
            "notruftelefon.jpg",
            "Ein Notruftelefon ermöglicht schnelle Kontaktaufnahme mit Rettungsdiensten im Notfall.",
            "notruftelefon"
        )