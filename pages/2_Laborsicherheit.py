import streamlit as st
from PIL import Image
import os

# Funktion zum Laden und Anzeigen eines Bildes
def load_image_with_info(filename, beschreibung, mehr_info):
    if os.path.exists(filename):
        img = Image.open(filename)
        st.image(img, caption=beschreibung, width=300)
        with st.expander(f"Mehr erfahren über {beschreibung}"):
            st.write(mehr_info)
    else:
        st.error(f"Bild '{filename}' nicht gefunden!")

# Liste der Bilder
bild_liste = [
    ("augenschutz.jpg", "Schutzbrille", "Schützt deine Augen vor Splittern oder Flüssigkeiten."),
    ("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Spült bei Notfällen chemische Substanzen aus den Augen."),
    ("erste_hilfe_start.jpg", "Erste Hilfe", "Hier gibt es Verbandmaterial und Erste-Hilfe-Sets."),
    ("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Schützt vor Kontamination und Gefährdung."),
    ("handschutz.jpg", "Schutzhandschuhe", "Schützt Hände vor Chemikalien und Schnitten."),
    ("labormantel.jpg", "Labormantel", "Schützt Kleidung und Haut."),
    ("notausgang.jpg", "Notausgang", "Ermöglicht eine sichere Flucht im Notfall."),
    ("notruftelefon_2.jpg", "Notruftelefon", "Schnelle Hilfe im Notfall über das Notruftelefon.")
]

# Zwei-Spalten-Layout
bilder_pro_reihe = 2

for i in range(0, len(bild_liste), bilder_pro_reihe):
    spalten = st.columns(bilder_pro_reihe)
    for spalte, (filename, beschreibung, mehr_info) in zip(spalten, bild_liste[i:i+bilder_pro_reihe]):
        with spalte:
            load_image_with_info(filename, beschreibung, mehr_info)
