import streamlit as st
import os
from utils.helpers import zeige_notfallleiste

# --- Bilder-Ordner ---
BILDER_ORDNER = "pages"

# --- Hilfsfunktion ---
def bild_mit_info(dateiname, beschreibung, key_suffix):
    bildpfad = os.path.join(BILDER_ORDNER, dateiname)
    if os.path.exists(bildpfad):
        with st.container():
            st.image(bildpfad, width=120)
            if st.button("ℹ️ Mehr erfahren", key=f"info_{key_suffix}"):
                st.info(beschreibung)
    else:
        st.error(f"Bild '{bildpfad}' nicht gefunden!")

# --- Haupttitel ---
st.markdown("<h1 style='text-align: center; color: #2E8BFF;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

# --- Bereich 1: tägliche Arbeit ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    bild_mit_info("augenschutz.jpg", "Schutzbrillen verhindern Verletzungen der Augen beim Arbeiten mit Chemikalien oder gefährlichen Stoffen.", "schutzbrille")
with col2:
    bild_mit_info("handschutz.jpg", "Schutzhandschuhe schützen die Haut vor Chemikalien, biologischen Stoffen und mechanischen Gefahren.", "handschutz")
with col3:
    bild_mit_info("labormantel.jpg", "Ein Labormantel schützt die Haut und Kleidung vor Spritzern und Verunreinigungen.", "labormantel")
with col4:
    bild_mit_info("essen_und_trinken_verboten.jpg", "Im Labor ist Essen und Trinken verboten, um Kontamination und Vergiftungen zu verhindern.", "essen_verboten")

# --- Abstand ---
st.markdown("<hr>", unsafe_allow_html=True)

# --- Bereich 2: Notfallsymbole ---
st.markdown("<h1 style='text-align: center; color: #FF4500;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

col5, col6, col7, col8 = st.columns(4)
with col5:
    bild_mit_info("Augenspüleinrichtung.jpg", "Die Augenspüleinrichtung ermöglicht es, gefährliche Substanzen schnell aus den Augen zu spülen.", "augenspuele")
with col6:
    bild_mit_info("erste_hilfe_start.jpg", "Das Erste-Hilfe-Symbol weist auf wichtige Einrichtungen und Ausrüstung für medizinische Notfälle hin.", "erstehilfe")
with col7:
    bild_mit_info("notausgang.jpg", "Der Notausgang zeigt den schnellsten Fluchtweg im Falle eines Brandes oder einer Evakuierung an.", "notausgang")
with col8:
    bild_mit_info("notruftelefon.jpg", "Ein Notruftelefon ermöglicht schnelle Kontaktaufnahme mit Rettungsdiensten im Notfall.", "notruftelefon")

# --- Abstand ---
st.markdown("<hr>", unsafe_allow_html=True)

# --- Bereich 3: Warnsymbole ---
st.markdown("<h1 style='text-align: center; color: #FFA500;'>⚠️ Warn- und Gefahrensymbole</h1>", unsafe_allow_html=True)

col9, col10, col11, col12 = st.columns(4)
with col9:
    bild_mit_info("Giftig.png", "Dieses Symbol warnt vor akut toxischen Substanzen, die beim Einatmen, Verschlucken oder Hautkontakt lebensgefährlich sein können.", "giftig")
with col10:
    bild_mit_info("Feuer.png", "Kennzeichnet leicht entzündliche Stoffe, die sich bei Kontakt mit Luft, Hitze oder Funken schnell entzünden können.", "feuer")
with col11:
    bild_mit_info("Biogefahr.png", "Warnt vor biologischen Gefahren wie Viren, Bakterien oder anderen Mikroorganismen, die Krankheiten verursachen können.", "bio")
with col12:
    bild_mit_info("Vorsicht.png", "Dieses Symbol weist auf eine allgemeine Gefahrenquelle hin. Zusätzliche Hinweise beachten!", "vorsicht")

# --- Notfallleiste am Ende ---
zeige_notfallleiste()