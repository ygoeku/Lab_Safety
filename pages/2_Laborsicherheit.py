import streamlit as st
from PIL import Image
import os

# Funktion zum Laden und Anzeigen eines Bildes
def load_image_with_info(filename, beschreibung, mehr_info):
    if os.path.exists(filename):
        img = Image.open(filename)
        img = img.resize((300, 300))  # Alle Bilder 300x300 Pixel
        st.image(img, caption=beschreibung)
        with st.expander(f"Mehr erfahren über {beschreibung}"):
            st.write(mehr_info)
    else:
        st.error(f"Bild '{filename}' nicht gefunden!")

# Liste der Bilder (angepasst auf deine echten Dateinamen!)
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

# Layout: 2 Bilder nebeneinander
bilder_pro_reihe = 2

# Bilder in zwei Spalten anzeigen
for i in range(0, len(bild_liste), bilder_pro_reihe):
    spalten = st.columns(bilder_pro_reihe)
    for spalte, (filename, beschreibung, mehr_info) in zip(spalten, bild_liste[i:i+bilder_pro_reihe]):
        with spalte:
            load_image_with_info(filename, beschreibung, mehr_info)