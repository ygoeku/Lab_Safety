import streamlit as st

st.title("Sicherheitszeichen")

# Handschuhe Bild
st.image("handschuhe.jpg", caption="Handschuhe tragen", width=200)
link1 = st.text_input("Infos zu Handschuhe tragen:", "https://dein-link-zu-infos.de")
if st.button("Mehr Infos Handschuhe"):
    st.markdown(f"[Hier klicken]({link1})")

st.divider()

# Schutzbrille Bild
st.image("laborbrille.gif", caption="Schutzbrille tragen", width=200)
link2 = st.text_input("Infos zu Schutzbrille tragen:", "https://dein-link-zu-infos.de")
if st.button("Mehr Infos Schutzbrille"):
    st.markdown(f"[Hier klicken]({link2})")

st.divider()

# Laborkittel Bild
st.image("laborkittel.png", caption="Laborkittel tragen", width=200)
link3 = st.text_input("Infos zu Laborkittel tragen:", "https://dein-link-zu-infos.de")
if st.button("Mehr Infos Laborkittel"):
    st.markdown(f"[Hier klicken]({link3})")

st.divider()

# Notausgang Bild
st.image("notfall ausgang.jpg", caption="Notausgang", width=200)
link4 = st.text_input("Infos zu Notausgang:", "https://dein-link-zu-infos.de")
if st.button("Mehr Infos Notausgang"):
    st.markdown(f"[Hier klicken]({link4})")
