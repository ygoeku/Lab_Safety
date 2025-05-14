import streamlit as st
import os
from utils.helpers import zeige_notfallleiste

# --- Bilder-Ordner ---
BILDER_ORDNER = "pages"

# --- Hilfsfunktion: Bild + Info ---
def bild_mit_info(dateiname, beschreibung, key_suffix):
    bildpfad = os.path.join(BILDER_ORDNER, dateiname)
    if os.path.exists(bildpfad):
        st.image(bildpfad, width=100)
        if st.button("ℹ️ Mehr erfahren", key=f"info_{key_suffix}"):
            st.info(beschreibung)
    else:
        st.error(f"Bild nicht gefunden: {bildpfad}")

# --- Style-Container ---
def farbiger_container(farbe_hex, content_function):
    st.markdown(f"""
        <div style="background-color: {farbe_hex}; padding: 30px; border-radius: 10px;">
    """, unsafe_allow_html=True)
    content_function()
    st.markdown("</div>", unsafe_allow_html=True)

# --- Haupttitel ---
st.markdown("<h1 style='text-align: center;'>🧪 Laborsymbole nach Bedeutung</h1>", unsafe_allow_html=True)

# --- Pflichtsymbole (blau) ---
with st.expander("🧪 Pflicht-Symbole (tägliche Arbeit)", expanded=True):
    def inhalt_pflicht():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("**Schutzbrille tragen**")
            bild_mit_info("augenschutz.jpg", "Schutzbrillen verhindern Verletzungen der Augen beim Arbeiten mit Chemikalien oder gefährlichen Stoffen.", "schutzbrille")
        with col2:
            st.markdown("**Handschutz**")
            bild_mit_info("handschutz.jpg", "Schutzhandschuhe schützen die Haut vor Chemikalien, biologischen Stoffen und mechanischen Gefahren.", "handschutz")
        with col3:
            st.markdown("**Labormantel**")
            bild_mit_info("labormantel.jpg", "Ein Labormantel schützt die Haut und Kleidung vor Spritzern und Verunreinigungen.", "labormantel")
        with col4:
            st.markdown("**Essen & Trinken verboten**")
            bild_mit_info("essen_und_trinken_verboten.jpg", "Im Labor ist Essen und Trinken verboten, um Kontamination und Vergiftungen zu verhindern.", "essen_verboten")
    farbiger_container("#e6f0ff", inhalt_pflicht)

# --- Erste Hilfe & Flucht (grün) ---
with st.expander("🚨 Erste Hilfe & Flucht", expanded=True):
    def inhalt_hilfe():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("**Erste Hilfe**")
            bild_mit_info("erste_hilfe_start.jpg", "Das Erste-Hilfe-Symbol weist auf wichtige Einrichtungen und Ausrüstung für medizinische Notfälle hin.", "erstehilfe")
        with col2:
            st.markdown("**Notausgang**")
            bild_mit_info("notausgang.jpg", "Der Notausgang zeigt den schnellsten Fluchtweg im Falle eines Brandes oder einer Evakuierung an.", "notausgang")
        with col3:
            st.markdown("**Notruftelefon**")
            bild_mit_info("notruftelefon.jpg", "Ein Notruftelefon ermöglicht schnelle Kontaktaufnahme mit Rettungsdiensten im Notfall.", "notruftelefon")
        with col4:
            st.empty()  # optional frei lassen
    farbiger_container("#e6ffe6", inhalt_hilfe)

# --- Notfallleiste (wie gehabt) ---
zeige_notfallleiste()