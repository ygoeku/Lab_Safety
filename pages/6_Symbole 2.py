import streamlit as st

st.set_page_config(page_title="Laborsymbole nach Kategorie", layout="wide")

# === Farbschema und Stil ===
st.markdown("""
<style>
.section {
    padding: 1.5em;
    border-radius: 1em;
    margin-bottom: 2em;
}
.blue-section {
    background-color: #e3f2fd;
}
.green-section {
    background-color: #e8f5e9;
}
.red-section {
    background-color: #ffebee;
}
.symbol {
    text-align: center;
    padding: 1em;
}
.symbol img {
    max-height: 120px;
}
.symbol-text {
    margin-top: 0.5em;
    font-weight: bold;
    font-size: 1.1em;
}
</style>
""", unsafe_allow_html=True)

st.title("💡 Laborsymbole nach Bedeutung")

# === Sektion 1: Tägliche Pflichten ===
st.markdown("<div class='section blue-section'>", unsafe_allow_html=True)
st.subheader("🧪 Pflicht-Symbole (tägliche Arbeit)")
cols = st.columns(4)
with cols[0]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/augenschutz.jpg'>
        <div class='symbol-text'>Schutzbrille tragen</div>
    </div>""", unsafe_allow_html=True)
with cols[1]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/handschutz.jpg'>
        <div class='symbol-text'>handschutz</div>
    </div>""", unsafe_allow_html=True)
with cols[2]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/labormantel.jpg'>
        <div class='symbol-text'>labormantel</div>
    </div>""", unsafe_allow_html=True)
with cols[3]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/essen_und_trinken_verboten.jpg'>
        <div class='symbol-text'>essen_und_trinken_verboten</div>
    </div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# === Sektion 2: Erste Hilfe & Fluchtwege ===
st.markdown("<div class='section green-section'>", unsafe_allow_html=True)
st.subheader("🚨 Erste Hilfe & Flucht")
cols = st.columns(4)
with cols[0]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/Augenspüleinrichtung.jpg'>
        <div class='symbol-text'>augenschutz</div>
    </div>""", unsafe_allow_html=True)
with cols[1]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/erste_hilfe_start.jpg'>
        <div class='symbol-text'>erste_hilfe_start</div>
    </div>""", unsafe_allow_html=True)
with cols[2]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/notausgang.jpg'>
        <div class='symbol-text'>notausgang</div>
    </div>""", unsafe_allow_html=True)
with cols[3]:
    st.markdown("""
    <div class='symbol'>
        <img src='/mnt/data/notruftelefon.jpg'>
        <div class='symbol-text'>notruftelefon</div>
    </div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)