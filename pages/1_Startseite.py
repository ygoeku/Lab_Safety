import streamlit as st

st.set_page_config(page_title="Startseite", layout="wide")

# --- Stil für Karten und Layout ---
st.markdown("""
    <style>
    body {
        background-color: #F0F2F6;
        font-family: 'Arial', sans-serif;
    }
    .card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .card:hover {
        transform: scale(1.05);
        background-color: #E8F0FE;
        box-shadow: 6px 6px 25px rgba(0, 0, 0, 0.2);
    }
    h1 {
        text-align: center;
        font-size: 50px;
        color: #0A66C2;
        margin-bottom: 50px;
    }
    .card-title {
        font-size: 30px;
        font-weight: bold;
        margin-top: 20px;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# --- Titel ---
st.markdown("<h1>🔬 Willkommen im Labor-Portal 🔬</h1>", unsafe_allow_html=True)

# --- Vier Karten nebeneinander ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🧪 Regeln im Labor", use_container_width=True):
        st.switch_page("pages/2_Laborsicherheit.py")

with col2:
    if st.button("✅ Checkliste", use_container_width=True):
        st.switch_page("pages/3_Checklisten.py")

with col3:
    if st.button("📊 Statistik", use_container_width=True):
        st.switch_page("pages/4_Statistik der Checkliste.py")

with col4:
    if st.button("🧬 Eingehende Proben", use_container_width=True):
        st.switch_page("pages/5_Eingehende Proben.py")

# --- Notfallleiste ---
from utils.helpers import zeige_notfallleiste
zeige_notfallleiste()
from utils.helpers import set_vollbild_hintergrund_url

set_vollbild_hintergrund_url("https://d2jx2rerrg6sh3.cloudfront.net/images/appnotes/ImageForAppNote_5166_17219167727185418.jpg")


        
