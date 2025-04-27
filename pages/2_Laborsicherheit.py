import streamlit as st
from PIL import Image

# --- Funktion zum Bild mit Infobutton anzeigen ---
def bild_mit_info(bildname, beschreibung, mehr_info):
    with st.container():
        st.image(bildname, width=200)
        with st.expander(f"ℹ️ {beschreibung}"):
            st.write(mehr_info)

# --- Seitenlayout etwas zentrieren ---
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Abschnitt: Symbole für das tägliche Arbeiten ---
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)

with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("schutzbrille.jpg", "Schutzbrille", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen.")
    with col2:
        bild_mit_info("handschutz.jpg", "Schutzhandschuhe", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze.")
    with col3:
        bild_mit_info("labormantel.jpg", "Labormantel", "Labormäntel schützen deine Haut und Kleidung vor Chemikalien und Hitze.")
    with col4:
        bild_mit_info("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor darf nicht gegessen oder getrunken werden, um Kontaminationen zu vermeiden.")

# --- Abschnitt: Symbole zu beachten in Notfallsituationen ---
st.markdown("---", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #d62728;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)

with st.expander("🚨 Symbole zu beachten in Notfallsituationen"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bild_mit_info("augenschutz.jpg", "Augenschutz", "Bei Gefahr durch Flüssigkeiten oder Partikel ist ein Augenschutz zwingend erforderlich.")
    with col2:
        bild_mit_info("augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Bei Verätzungen sofort die Augen mit der Augenspüleinrichtung spülen.")
    with col3:
        bild_mit_info("notausgang.jpg", "Notausgang", "Im Notfall schnell und geordnet den Notausgang benutzen.")
    with col4:
        bild_mit_info("notruftelefon.jpg", "Notruftelefon", "Im Notfall sofort Hilfe über das Notruftelefon rufen.")