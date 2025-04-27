import streamlit as st
import os

# Automatisch Desktop Pfad finden
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

st.title("Sicherheitszeichen")

# Funktion zum sicheren Laden
def load_image(filename):
    full_path = os.path.join(desktop_path, filename)
    if os.path.exists(full_path):
        st.image(full_path, caption=filename, width=200)
    else:
        st.error(f"Datei nicht gefunden: {filename}")

# Bilder laden
load_image("handschuhe.png")
load_image("laborbrille.gif")
load_image("laborkittel.png")
load_image("notfall ausgang.jpg")

