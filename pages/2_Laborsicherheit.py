import streamlit as st
import os

# Automatisch Desktop Pfad finden
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

st.title("Sicherheitszeichen")

# Funktion zum sicheren Laden
def load_image(filename, beschreibung):
    full_path = os.path.join(desktop_path, filename)
    if os.path.exists(full_path):
        st.image(full_path, caption=beschreibung, width=200)
        link = st.text_input(f"Link für {beschreibung}:", f"https://dein-link-zu-{beschreibung.replace(' ', '_').lower()}.de")
        if st.button(f"Mehr Infos zu {beschreibung}"):
            st.markdown(f"[Hier klicken]({link})")
    else:
        st.error(f"Datei nicht gefunden: {filename}")

# Bilder laden
load_image("handschuhe.jpg", "Handschuhe tragen")
load_image("laborbrille.gif", "Schutzbrille tragen")
load_image("laborkittel.png", "Laborkittel tragen")
load_image("notfall ausgang.jpg", "Notausgang")


