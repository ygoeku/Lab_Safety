import streamlit as st
from PIL import Image
import os

# Basis-Pfad zu deinen Bildern
basis_pfad = r"C:\Users\elena\OneDrive\Desktop\signale"

# CSS für Design
st.markdown("""
    <style>
    img {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        margin-bottom: 10px;
    }
    .block-container {
        background-color: #f5f5f5;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Funktion zum Laden und Anzeigen eines Bildes
def load_image_with_info(filename, beschreibung, mehr_info):
    bild_pfad = os.path.join(basis_pfad, filename)
    if os.path.exists(bild_pfad):
        img = Image.open(bild_pfad)
        img = img.resize((300, 300))  # Größe einheitlich
        st.image(img, caption=beschreibung)  # Nur st.image verwenden!
        with st.expander(f"Mehr erfahren über {beschreibung}"):
            st.write(mehr_info)
    else:
        st.error(f"Bild '{filename}' nicht gefunden!")

# ------------------------------
# Erste Gruppe: Tägliche Arbeit
# ------------------------------
st.header("Symbole für das tägliche Arbeiten im Labor")

arbeit_bilder = [
    ("augenschutz.jpg", "Schutzbrille", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen."),
    ("handschutz.jpg", "Schutzhandschuhe", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze."),
    ("labormantel.jpg", "Labormantel", "Labormäntel schützen deine Kleidung und Haut vor gefährlichen Substanzen."),
    ("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor ist Essen und Trinken verboten, um Kontaminationen und Vergiftungen zu vermeiden.")
]

for i in range(0, len(arbeit_bilder), 2):
    spalten = st.columns(2)
    for spalte, (filename, beschreibung, mehr_info) in zip(spalten, arbeit_bilder[i:i+2]):
        with spalte:
            load_image_with_info(filename, beschreibung, mehr_info)

# ------------------------------
# Trennlinie
# ------------------------------
st.divider()

# ------------------------------
# Zweite Gruppe: Notfallsymbole
# ------------------------------
st.header("Symbole zu beachten in Notfallsituationen")

notfall_bilder = [
    ("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Im Notfall kannst du mit einer Augenspüleinrichtung deine Augen schnell von gefährlichen Stoffen reinigen."),
    ("erste_hilfe_start.jpg", "Erste Hilfe", "An der Erste-Hilfe-Station findest du Verbandmaterial und Hilfe für Verletzungen."),
    ("notausgang.jpg", "Notausgang", "Notausgänge ermöglichen eine schnelle Flucht bei Bränden oder anderen Notfällen."),
    ("notruftelefon.jpg", "Notruftelefon", "Im Notfall kannst du hier schnell Hilfe rufen. Notrufnummern sollten gut sichtbar sein.")
]

for i in range(0, len(notfall_bilder), 2):
    spalten = st.columns(2)
    for spalte, (filename, beschreibung, mehr_info) in zip(spalten, notfall_bilder[i:i+2]):
        with spalte:
            load_image_with_info(filename, beschreibung, mehr_info)