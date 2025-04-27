import streamlit as st

# Funktion um Bild + Infobutton anzuzeigen
def bild_mit_info(bildname, beschreibung, mehr_info):
    col = st.container()
    with col:
        c1, c2 = st.columns([4,1])
        with c1:
            st.image(bildname, width=150)
            st.caption(beschreibung)
        with c2:
            with st.expander(💚 + " Mehr erfahren"):
                st.write(mehr_info)

# -----------------------------

# Titel 1
st.markdown("""
<h1 style='text-align: center; color: #2196f3;'>🧪 Symbole für das tägliche Arbeiten im Labor</h1>
""", unsafe_allow_html=True)

with st.expander("🧪 Symbole für das tägliche Arbeiten im Labor anzeigen"):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        bild_mit_info("augenschutz.jpg", "Schutzbrille", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen.")
    with c2:
        bild_mit_info("handschutz.jpg", "Schutzhandschuhe", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze.")
    with c3:
        bild_mit_info("labormantel.jpg", "Labormantel", "Labormantel schützt deine Kleidung und Haut vor Schäden.")
    with c4:
        bild_mit_info("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor ist Essen und Trinken verboten, um Kontamination zu vermeiden.")

st.divider()

# Titel 2
st.markdown("""
<h1 style='text-align: center; color: #f44336;'>🚨 Symbole zu beachten in Notfallsituationen</h1>
""", unsafe_allow_html=True)

with st.expander("🚨 Symbole in Notfallsituationen anzeigen"):
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        bild_mit_info("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Im Notfall sofort die Augenspüleinrichtung benutzen, um Verunreinigungen auszuspülen.")
    with c6:
        bild_mit_info("erste_hilfe_start.jpg", "Erste Hilfe", "Bei Verletzungen die Erste-Hilfe-Station aufsuchen.")
    with c7:
        bild_mit_info("notausgang.jpg", "Notausgang", "Im Notfall den gekennzeichneten Notausgang benutzen.")
    with c8:
        bild_mit_info("notruftelefon.jpg", "Notruftelefon", "Bei Notfällen sofort das Notruftelefon benutzen.")

# -----------------------------

# Hinweis unten
t = """
<style>
    .stMarkdown p {text-align: center; color: gray; font-size: 12px;}
</style>
"""
st.markdown(t, unsafe_allow_html=True)
st.markdown("Alles korrekt geladen 👌")