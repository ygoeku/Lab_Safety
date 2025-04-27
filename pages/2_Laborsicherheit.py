import streamlit as st

st.title("Sicherheitszeichen")

st.divider()

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
