import streamlit as st

# Funktion zum Bildanzeigen mit eigenem Infobutton
def bild_mit_info(bildname, beschreibung, mehr_info):
    if st.button(f"ℹ️ {beschreibung}", key=bildname):
        st.image(bildname, width=200)
        with st.expander(f"Mehr erfahren über {beschreibung}"):
            st.write(mehr_info)
    else:
        st.image(bildname, width=200)
        st.caption(beschreibung)

# Layout

st.markdown("<h1 style='text-align: center;'>🔬 Symbole für das tägliche Arbeiten im Labor</h1>", unsafe_allow_html=True)
spalte1, spalte2, spalte3, spalte4 = st.columns(4)

with spalte1:
    bild_mit_info("schutzbrille.jpg", "Schutzbrille", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen.")

with spalte2:
    bild_mit_info("handschutz.jpg", "Handschuhe", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze.")

with spalte3:
    bild_mit_info("labormantel.jpg", "Labormantel", "Laborkittel schützen deine Kleidung und Haut. Achte darauf, dass der Kittel schwer entflammbar ist.")

with spalte4:
    bild_mit_info("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor darf nicht gegessen oder getrunken werden, um Kontamination zu vermeiden.")

st.markdown("---")

st.markdown("<h1 style='text-align: center;'>🚨 Symbole zu beachten in Notfallsituationen</h1>", unsafe_allow_html=True)
spalte5, spalte6, spalte7, spalte8 = st.columns(4)

with spalte5:
    bild_mit_info("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Bei Kontakt mit gefährlichen Stoffen sofort die Augenspüleinrichtung benutzen.")

with spalte6:
    bild_mit_info("erste_hilfe_start.jpg", "Erste Hilfe", "Hier findest du die Erste-Hilfe-Ausrüstung für Verletzungen im Labor.")

with spalte7:
    bild_mit_info("notausgang.jpg", "Notausgang", "Im Notfall sofort den nächstgelegenen Notausgang benutzen.")

with spalte8:
    bild_mit_info("notruftelefon.jpg", "Notruftelefon", "Benutze dieses Telefon, um im Notfall schnell Hilfe zu rufen.")