import pandas as pd
import streamlit as st
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

st.set_page_config(page_title="Start – Labor Checklisten-App", layout="centered")

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Lab_Safety")

# initialize the login manager and open login/register tabs
login_manager = LoginManager(data_manager)
login_manager.login_register()

# Wenn Login erfolgreich → Benutzername in Session speichern & Daten laden
if st.session_state.get("authentication_status") is True:
    st.session_state["user"] = st.session_state.get("username")

    # Nur laden, wenn logbuch_df noch nicht geladen wurde
    data_manager.load_app_data(
        session_state_key='logbuch_df',
        file_name='logbuch.csv',
        initial_value=pd.DataFrame(columns=["Name", "Datum", "Uhrzeit", "Zeitpunkt", "Frage", "Antwort", "Bemerkung"]),
    )

    # ===== EINMALIGE Willkommensanzeige =====
    st.title('Lab_Safety')

    name = st.session_state["user"]
    st.markdown(f"✨ Hallo **{name}!** ✨")

    st.markdown("🧪 Die Anwendung unterstützt Sie dabei, Sicherheits- und Hygienestandards im Labor einzuhalten und Aufgaben strukturiert zu dokumentieren.")

    st.info("""Diese Anwendung dient der Unterstützung bei der Einhaltung von Sicherheits- und Hygienerichtlinien. 
    Sie ersetzt jedoch keine offizielle Sicherheitsunterweisung oder persönliche Schutzausrüstung.""")

    st.write("Diese App wurde von Yasemin Gökuguz und Elena Avkova im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW entwickelt.")

else:
    st.warning("Bitte melden Sie sich zuerst an oder registrieren Sie sich.")