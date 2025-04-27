import streamlit as st

# Funktion zum Laden der Bilder
def bild_mit_info(bildname, titel, info):
    col = st.container()
    with col:
        st.image(bildname, width=150)
        with st.expander(f"ℹ️ Mehr erfahren über {titel}"):
            st.write(info)

# Hauptüberschrift
st.markdown("<h1 style='text-align: center; color: #2196f3;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

# Expander für tägliche Arbeit
with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("augenschutz.jpg", "Augenschutz", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen.")
    with col2:
        bild_mit_info("handschutz.jpg", "Handschutz", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze.")
    with col3:
        bild_mit_info("labormantel.jpg", "Labormantel", "Laborkittel schützen deine Kleidung und Haut. Sie sollten schwer entflammbar sein.")
    with col4:
        bild_mit_info("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor ist Essen und Trinken strengstens verboten, um Kontamination zu vermeiden.")

# Trennlinie
st.markdown("---")

# Zweite Hauptüberschrift
st.markdown("<h1 style='text-align: center; color: #e53935;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

# Expander für Notfallsituationen
with st.expander("🚨 Symbole zu beachten in Notfallsituationen"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Bei Verätzungen oder Fremdkörpern in den Augen sofort die Augenspüleinrichtung benutzen.")
    with col2:
        bild_mit_info("erste_hilfe_start.jpg", "Erste Hilfe", "Im Notfall findest du hier das Erste-Hilfe-Set für schnelle medizinische Versorgung.")
    with col3:
        bild_mit_info("notausgang.jpg", "Notausgang", "Bei Gefahr sofort den gekennzeichneten Notausgang benutzen.")
    with col4:
        bild_mit_info("notruftelefon.jpg", "Notruftelefon", "Im Notfall erreichst du über das Notruftelefon die Sicherheitsdienste.")