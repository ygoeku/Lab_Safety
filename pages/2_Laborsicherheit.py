import streamlit as st

st.set_page_config(page_title="Laborsicherheit", layout="wide")

# Hilfsfunktion zum Laden von Bild + Infobutton
def bild_mit_info(bildname, beschreibung):
    st.image(bildname, width=150, use_column_width=False)
    st.button("ℹ️ Mehr erfahren", key=bildname, help=beschreibung)

# --- Titel der Seite ---
st.markdown("<h1 style='text-align: center; color: #3399FF;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

# --- Erster Bereich: tägliches Arbeiten ---
with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("augenschutz.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Schutzbrillen verhindern Verletzungen der Augen beim Arbeiten mit Chemikalien oder gefährlichen Stoffen.")
    with col2:
        st.image("handschutz.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Schutzhandschuhe schützen die Haut vor Chemikalien, biologischen Stoffen und mechanischen Gefahren.")
    with col3:
        st.image("labormantel.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Ein Labormantel schützt die Haut und Kleidung vor Spritzern und Verunreinigungen.")
    with col4:
        st.image("essen_und_trinken_verboten.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Im Labor ist Essen und Trinken verboten, um Kontamination und Vergiftungen zu verhindern.")

# --- Abstand ---
st.markdown("<hr>", unsafe_allow_html=True)

# --- Titel für Notfallsituation ---
st.markdown("<h1 style='text-align: center; color: #FF4500;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

# --- Zweiter Bereich: Notfallsituation ---
with st.expander("🚨 Symbole zu beachten in Notfallsituationen", expanded=False):
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.image("Augenspüleinrichtung.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Die Augenspüleinrichtung ermöglicht es, gefährliche Substanzen schnell aus den Augen zu spülen.")
    with col6:
        st.image("erste_hilfe_start.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Das Erste-Hilfe-Symbol weist auf wichtige Einrichtungen und Ausrüstung für medizinische Notfälle hin.")
    with col7:
        st.image("notausgang.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Der Notausgang zeigt den schnellsten Fluchtweg im Falle eines Brandes oder einer Evakuierung an.")
    with col8:
        st.image("notruftelefon.jpg", height=150)
        with st.expander("ℹ️ Mehr erfahren"):
            st.info("Ein Notruftelefon ermöglicht schnelle Kontaktaufnahme mit Rettungsdiensten im Notfall.")