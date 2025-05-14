import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# ===== Konfiguration der Seite =====
st.set_page_config(page_title="Labor App Login", layout="wide")

# ===== Initialisierung von DataManager und LoginManager =====
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Lab_Safety")
login_manager = LoginManager(data_manager)

# ===== Login anzeigen (bei Bedarf) =====
login_manager.login_register()

# ===== Zugriff blockieren, wenn nicht eingeloggt =====
if "username" not in st.session_state and "user" not in st.session_state:
    st.stop()

# ===== Begrüßung nach Login =====
name = st.session_state.get("name", "Nutzer")

st.title("Lab_Safety")
st.markdown(f"✨ Hallo **{name}**! Willkommen im Labor-Portal. ✨")
st.markdown("🧪 Diese Anwendung hilft Ihnen, Sicherheits- und Hygienestandards im Labor einzuhalten und Aufgaben strukturiert zu dokumentieren.")

st.info("""
Diese Anwendung dient zur Unterstützung bei der Einhaltung von Sicherheits- und Hygienerichtlinien. 
Sie ersetzt jedoch keine offizielle Sicherheitsunterweisung oder persönliche Schutzausrüstung.
""")

st.write("Diese App wurde von Yasemin Gökuguz und Elena Avkova im Rahmen des Moduls **'BMLD Informatik 2'** an der ZHAW entwickelt.")

# Start.py
import streamlit as st
import os

# Automatische Pfaderkennung
def finde_logbuch_pfad():
    moegliche_pfade = [
        os.path.expanduser("~/SwitchDrive/Lab_Safety/logbuch.csv"),
        os.path.expanduser("~/SwitchDrive/Lab_Safety (2)/logbuch.csv"),
        os.path.expanduser("~/SwitchDrive/Lab_Safety_Shared/logbuch.csv"),
    ]
    for pfad in moegliche_pfade:
        if os.path.exists(pfad):
            return pfad
    return None

# Ergebnis speichern
if "logbuch_pfad" not in st.session_state:
    st.session_state["logbuch_pfad"] = finde_logbuch_pfad()

# Benutzerinfo
if st.session_state["logbuch_pfad"]:
    st.info(f"Aktive Logbuch-Datei: {st.session_state['logbuch_pfad']}")
else:
    st.error("Keine Logbuch-Datei gefunden.")