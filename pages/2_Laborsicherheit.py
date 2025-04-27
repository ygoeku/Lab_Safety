import streamlit as st

# Funktion für ein Bild + Infobutton darunter
def bild_mit_info(bildname, titel, info):
    col = st.container()
    with col:
        st.image(bildname, width=200)
        with st.expander(f"ℹ️ Mehr erfahren über {titel}"):
            st.write(info)

# Schöne Überschrift
st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>",
    unsafe_allow_html=True
)

# Erster Expander
with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("schutzbrille.jpg", "Schutzbrille", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen.")
    with col2:
        bild_mit_info("handschutz.jpg", "Schutzhandschuhe", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze.")
    with col3:
        bild_mit_info("labormantel.jpg", "Labormantel", "Labormäntel schützen deine Kleidung und Haut vor Chemikalien und Feuer.")
    with col4:
        bild_mit_info("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Essen und Trinken im Labor sind verboten, um Kontaminationen und Vergiftungen zu vermeiden.")

# Abstandslinie
st.markdown("---")

# Zweite Überschrift
st.markdown(
    "<h1 style='text-align: center; color: #C0392B;'>🚨 Symbole zu beachten in Notfallsituationen</h1>",
    unsafe_allow_html=True
)

# Zweiter Expander
with st.expander("🚨 Symbole zu beachten in Notfallsituationen", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("augenschutz.jpg", "Augenspüleinrichtung", "Im Falle einer Verätzung oder Verunreinigung können die Augen sofort ausgespült werden.")
    with col2:
        bild_mit_info("erste_hilfe_start.jpg", "Erste Hilfe", "Standort für Erste-Hilfe-Material und medizinische Notfallversorgung.")
    with col3:
        bild_mit_info("notausgang.jpg", "Notausgang", "Fluchtweg bei Feuer oder anderen Notfällen. Immer freihalten!")
    with col4:
        bild_mit_info("notruftelefon.jpg", "Notruftelefon", "Im Notfall kann hier direkt Hilfe gerufen werden.")