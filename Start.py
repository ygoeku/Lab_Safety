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

st.title("Lab_Safety")
st.markdown(f"✨ Hallo **{name}**! Willkommen im Labor-Portal. ✨")
st.markdown("🧪 Diese Anwendung hilft Ihnen, Sicherheits- und Hygienestandards im Labor einzuhalten und Aufgaben strukturiert zu dokumentieren.")

st.info("""
Diese Anwendung dient zur Unterstützung bei der Einhaltung von Sicherheits- und Hygienerichtlinien. 
Sie ersetzt jedoch keine offizielle Sicherheitsunterweisung oder persönliche Schutzausrüstung.
""")

st.write("Diese App wurde von Yasemin Gökuguz und Elena Avkova im Rahmen des Moduls **'BMLD Informatik 2'** an der ZHAW entwickelt.")

# ===== Debug: Lokaler Pfadprüfung (optional) =====
korrekter_pfad = r"C:\Users\elena\OneDrive - ZHAW\Informatik 2\Lab_Safety\logbuch.csv"
if os.path.exists(korrekter_pfad):
    st.session_state["logbuch_pfad"] = korrekter_pfad
    st.success(f"✅ Logbuch gefunden: {korrekter_pfad}")
else:
    st.error(f"❌ Logbuch nicht gefunden unter: {korrekter_pfad}")

# ===== WebDAV-Konfiguration prüfen =====
if "webdav" in st.secrets:
    st.success("✅ WebDAV-Konfiguration aus secrets geladen.")
    st.json(st.secrets["webdav"])  # Debug – später entfernen
else:
    st.error("❌ WebDAV-Zugang nicht gefunden in secrets.toml.")

# ===== Debug: Dateisystem und Credentials anzeigen =====
st.caption(f"📁 Aktives Dateisystem: {type(data_manager.fs)}")
st.caption(f"📄 credentials.yaml wird verwendet unter: {data_manager.fs_root_folder}/credentials.yaml")

# ===== Gemeinsame Datei aus WebDAV laden =====
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='logbuch.csv', 
    initial_value=pd.DataFrame()
)