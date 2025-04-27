import streamlit as st
import os

# Funktion zum Laden und Anzeigen eines Bildes mit Expander für mehr Infos
def load_image_with_info(filename, beschreibung, mehr_info, column):
    try:
        path = os.path.join("pages", filename)
        if os.path.exists(path):
            column.image(path, caption=beschreibung, use_container_width=True)
            with column.expander(f"Mehr erfahren über {beschreibung}"):
                st.write(mehr_info)
        else:
            column.error(f"Bild '{filename}' nicht gefunden!")
    except Exception as e:
        column.error(f"Fehler beim Laden von {filename}: {e}")
        print(f"Fehler beim Laden von {filename}: {e}")

# Zwei-Spalten-Layout
col1, col2 = st.columns(2)

# Liste der Bilder, Beschreibungen und zusätzlichen Infos
bild_liste = [
    ("handschuhe.jpg", "Schutzhandschuhe", " Schutzhandschuhe schützen deine Hände vor Chemikalien, Schnitten und Hitze. Immer tragen, wenn du mit gefährlichen Stoffen arbeitest!"),
    ("laborbrille.jpg", "Schutzbrille", " Schutzbrillen verhindern, dass gefährliche Flüssigkeiten oder Splitter deine Augen verletzen."),
    ("laborkittel.jpg", "Laborkittel", " Laborkittel schützen deine Kleidung und Haut. Achte darauf, dass der Kittel aus schwer entflammbarem Material besteht."),
    ("notausgang.jpg", "Notausgang", " Notausgänge ermöglichen eine schnelle Flucht bei Bränden oder anderen Notfällen. Halte sie immer frei und wisse, wo sie sind!")
]

# Bilder automatisch in zwei Spalten laden
for index, (filename, beschreibung, mehr_info) in enumerate(bild_liste):
    if index % 2 == 0:
        load_image_with_info(filename, beschreibung, mehr_info, col1)
    else:
        load_image_with_info(filename, beschreibung, mehr_info, col2)
        










