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

import os
import streamlit as st

# Dein korrekter, vollständiger Pfad
korrekter_pfad = r"C:\Users\elena\OneDrive - ZHAW\Informatik 2\Lab_Safety\logbuch.csv"

# Sicher prüfen
if os.path.exists(korrekter_pfad):
    st.session_state["logbuch_pfad"] = korrekter_pfad
    st.success(f"✅ Logbuch gefunden: {korrekter_pfad}")
else:
    st.error(f"❌ Logbuch nicht gefunden unter: {korrekter_pfad}")