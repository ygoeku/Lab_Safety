import streamlit as st
from PIL import Image
import os

# Basis-Pfad zu deinen Bildern
basis_pfad = r"C:\Users\elena\OneDrive\Desktop\signale"

# Funktion zum Laden und Anzeigen eines Bildes
def load_image_with_info(filename, beschreibung, mehr_info):
    bild_pfad = os.path.join(basis_pfad, filename)
    if os.path.exists(bild_pfad):
        img = Image.open(bild_pfad)
        img = img.resize((300, 300))
        st.image(img, caption=beschreibung)
        with st.expander(f"Mehr erfahren über {beschreibung}"):
            st.write(mehr_info)
    else:
        st.error(f"Bild '{filename}' nicht gefunden!")

# Deine Liste:
bild_liste = [
    ("augenschutz.jpg", "Schutzbrille", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen."),
    ("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Im Notfall kannst du mit einer Augenspüleinrichtung deine Augen schnell von gefährlichen Stoffen reinigen."),
    ("erste_hilfe_start.jpg", "Erste Hilfe", "An der Erste-Hilfe-Station findest du Verbandmaterial und Hilfe für Verletzungen."),
    ("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor ist Essen und Trinken verboten, um Kontaminationen und Vergiftungen zu vermeiden."),
    ("handschutz.jpg", "Schutzhandschuhe", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze."),
    ("labormantel.jpg", "Labormantel", "Labormäntel schützen deine Kleidung und Haut vor gefährlichen Substanzen."),
    ("notausgang.jpg", "Notausgang", "Notausgänge ermöglichen eine schnelle Flucht bei Bränden oder anderen Notfällen."),
    ("notruftelefon.jpg", "Notruftelefon", "Im Notfall kannst du hier schnell Hilfe rufen. Notrufnummern sollten gut sichtbar sein.")
]

# Layout: 2 Spalten
bilder_pro_reihe = 2

# Anzeigen:
for i in range(0, len(bild_liste), bilder_pro_reihe):
    spalten = st.columns(bilder_pro_reihe)
    for spalte, (filename, beschreibung, mehr_info) in zip(spalten, bild_liste[i:i+bilder_pro_reihe]):
        with spalte:
            load_image_with_info(filename, beschreibung, mehr_info)