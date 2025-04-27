import streamlit as st
from PIL import Image

# Funktion zum Laden und Anzeigen eines Bildes mit Expander für mehr Infos
def load_image_with_info(filename, beschreibung, mehr_info):
    try:
        # Pfad ohne "pages" direkt benutzen!
        if os.path.exists(filename):
            img = Image.open(filename)
            fixed_size = (300, 300)  # Beispiel: 300x300 Pixel für gleiche Größe
            img = img.resize(fixed_size)

            st.image(img, caption=beschreibung)
            with st.expander(f"Mehr erfahren über {beschreibung}"):
                st.write(mehr_info)
        else:
            st.error(f"Bild '{filename}' nicht gefunden!")
    except Exception as e:
        st.error(f"Fehler beim Laden von {filename}: {e}")
        print(f"Fehler beim Laden von {filename}: {e}")

# Liste der Bilder, Beschreibungen und zusätzlichen Infos
bild_liste = [
    ("augenschutz.jpg", "Schutzbrille", "Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen."),
    ("Augenspüleinrichtung.jpg", "Augenspüleinrichtung", "Im Notfall kannst du mit einer Augenspüleinrichtung deine Augen schnell von gefährlichen Stoffen reinigen."),
    ("erste_hilfe_start.jpg", "Erste Hilfe", "An der Erste-Hilfe-Station findest du Verbandmaterial und Hilfe für Verletzungen."),
    ("essen_und_trinken_verboten.jpg", "Essen und Trinken verboten", "Im Labor ist Essen und Trinken verboten, um Kontaminationen und Vergiftungen zu vermeiden."),
    ("handschutz.jpg", "Schutzhandschuhe", "Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze."),
    ("labormantel.jpg", "Labormantel", "Labormäntel schützen deine Kleidung und Haut vor gefährlichen Substanzen."),
    ("notausgang.jpg", "Notausgang", "Notausgänge ermöglichen eine schnelle Flucht bei Bränden oder anderen Notfällen."),
    ("notruftelefon_2.jpg", "Notruftelefon", "Im Notfall kannst du hier schnell Hilfe rufen. Notrufnummern sollten gut sichtbar sein.")
]

# Bilder automatisch in 2 Spalten anzeigen
bilder_pro_reihe = 2

for i in range(0, len(bild_liste), bilder_pro_reihe):
    spalten = st.columns(bilder_pro_reihe)
    for spalte, (filename, beschreibung, mehr_info) in zip(spalten, bild_liste[i:i+bilder_pro_reihe]):
        with spalte:
            load_image_with_info(filename, beschreibung, mehr_info)