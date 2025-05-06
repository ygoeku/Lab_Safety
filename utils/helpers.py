import pandas as pd
from datetime import datetime
import pytz

def ch_now(rounding='s'):
    """
    Returns current Swiss time as pandas timestamp without timezone suffix
    Args:
        rounding (str): Time unit to floor to (e.g. 'min', 'H', 's'). Default is 's' (second)
    """
    swiss_tz = pytz.timezone('Europe/Zurich')
    current_time = datetime.now(swiss_tz)
    ts = pd.Timestamp(current_time.replace(tzinfo=None))
    
    return ts.floor(rounding) if rounding else ts
import streamlit as st

def zeige_notfallleiste():
    st.markdown("""
        <style>
        .emergency-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: red;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            z-index: 9999;
        }
        </style>
        <div class="emergency-bar">
            🚨 Notfallnummern: ZHAW 7070 | Ambulanz 144 | Polizei 117 | Feuerwehr 118 | REGA 1414 | Toxinfo 145
        </div>
    """, unsafe_allow_html=True)


import streamlit as st
def set_hintergrundfarbe(farbe="#F5F5F5"):
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {farbe};
        }}
        </style>
    """, unsafe_allow_html=True)
import streamlit as st

def set_vollbild_hintergrund_url(bild_url):
    st.markdown(f"""
        <style>
        html, body, .stApp {{
            height: 100%;
            margin: 0;
            padding: 0;
        }}
        .stApp {{
            background-image: url("{bild_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)