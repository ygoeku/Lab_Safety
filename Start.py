# ====== Start Init Block ======
# This needs to copied on top of the entry point of the app (Start.py)

import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Lab_Safety")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )
# ====== End Init Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st


st.title('Lab_Safety')

name = st.session_state.get('name')
st.markdown(f"✨ Hallo {name}! ✨")
st.markdown("🧪 Die Anwendung unterstützt Sie dabei, Sicherheits- und Hygienestandards im Labor einzuhalten und Aufgaben strukturiert zu dokumentieren.")

# Add some safety advice
st.info("""Diese Anwendung dient der Unterstützung bei der Einhaltung von Sicherheits- und Hygienerichtlinien. 
Sie ersetzt jedoch keine offizielle Sicherheitsunterweisung oder persönliche Schutzausrüstung.""")

st.write("Diese App wurde von Yasemin Gökuguz und Elena Avkova im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW entwickelt.")