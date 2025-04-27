import streamlit as st

# Funktion zum Anzeigen der Bilder mit Infobutton
def bild_mit_info(bildname, beschreibung, mehr_info):
    col = st.container()
    with col:
        # Bild laden
        st.image(bildname, width=150)
        st.caption(beschreibung)
        # Infobutton als Expander
        with st.expander("ℹ️ Mehr erfahren"):
            st.write(mehr_info)

# Layout: Zwei Bereiche (Tägliche Arbeiten & Notfallsituation)
st.markdown("<h1 style='text-align: center; color: #1995dc;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

with st.expander("Symbole für das tägliche Arbeiten im Labor"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("augenschutz.jpg", "Augenschutz", "Schutzbrillen verhindern Verletzungen durch Flüssigkeiten oder Splitter.")
    with col2:
        bild_mit_info("handschutz.jpg", "Handschutz", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze.")
    with col3:
        bild_mit_info("labormantel.jpg", "Labormantel", "Labormäntel schützen deine Haut und Kleidung vor gefährlichen Stoffen.")
    with col4:
        bild_mit_info("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Verhindert Kontamination durch gefährliche Substanzen im Labor.")

st.divider()

st.markdown("<h1 style='text-align: center; color: #d62728;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

with st.expander("Symbole zu beachten in Notfallsituationen"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Schnelle Spülung bei Augenkontakt mit Chemikalien.")
    with col2:
        bild_mit_info("erste_hilfe_start.jpg", "Erste Hilfe", "Zeigt den Standort der Erste-Hilfe-Ausrüstung.")
    with col3:
        bild_mit_info("notausgang.jpg", "Notausgang", "Weg zur schnellen Evakuierung im Notfall.")
    with col4:
        bild_mit_info("notruftelefon.jpg", "Notruftelefon", "Schneller Kontakt zur Notfallzentrale oder Feuerwehr.")