import streamlit as st

st.set_page_config(page_title="Laborsicherheit", layout="wide")

# Hilfsfunktion zum Laden von Bild + Infobutton
def bild_mit_info(bildname, beschreibung, titel):
    st.image(bildname, width=150)
    with st.expander("ℹ️ Mehr erfahren", expanded=False):
        st.markdown(
            f"<div style='background-color: #e6f2ff; padding: 10px; border-radius: 10px;'>{beschreibung}</div>",
            unsafe_allow_html=True
        )

# --- Titel der Seite ---
st.markdown("<h1 style='text-align: center; color: #3399FF;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

# --- Erster Bereich: tägliches Arbeiten ---
with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor", expanded=False):
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

# --- Titel für Notfallsituation ---
st.markdown("<h1 style='text-align: center; color: #FF4500;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

# --- Zweiter Bereich: Notfallsituation ---
with st.expander("🚨 Symbole zu beachten in Notfallsituationen", expanded=False):
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