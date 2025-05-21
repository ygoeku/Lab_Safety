import streamlit as st
import pandas as pd
import os
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# ===== Konfiguration der Seite =====
st.set_page_config(page_title="Labor App Login", layout="wide")

# ===== Initialisierung von DataManager und LoginManager =====
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Safelab")
login_manager = LoginManager(data_manager)

# ===== Login anzeigen (bei Bedarf) =====
login_manager.login_register()

# ===== Login-Zustand anzeigen =====
username = st.session_state.get("username")
if username:
    st.success(f"✅ Eingeloggt als: {username}")
else:
    st.warning("⚠️ Noch nicht eingeloggt – bitte Anmeldemaske verwenden.")

# ===== Zugriff blockieren, wenn nicht eingeloggt =====
if "username" not in st.session_state and "user" not in st.session_state:
    st.stop()

# ===== Begrüßung nach Login =====
name = st.session_state.get("name", "Nutzer")

st.title("Safelab")
st.markdown(f"✨ Hallo **{name}**! Willkommen im Labor-Portal. ✨")
st.markdown("🧪 Diese Anwendung hilft Ihnen, Sicherheits- und Hygienestandards im Labor einzuhalten und Aufgaben strukturiert zu dokumentieren.")

st.info("""
Diese Anwendung dient zur Unterstützung bei der Einhaltung von Sicherheits- und Hygienerichtlinien. 
Sie ersetzt jedoch keine offizielle Sicherheitsunterweisung oder persönliche Schutzausrüstung.
""")

st.write("Diese App wurde von Yasemin Gökuguz und Elena Avkova im Rahmen des Moduls **'BMLD Informatik 2'** an der ZHAW entwickelt.")
