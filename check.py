import streamlit as st

st.set_page_config(page_title="Amal's love", page_icon=":tada:", layout="wide")

st.title("Do you want to learn who is KorAmaaal's crush?")

correct_password = "Heisenberg"

password_input = st.text_input("Enter the password:", type="password")


if password_input == correct_password:

    button_clicked = st.button("Click to see")

    def reveal_crush():
        st.write("Nargis :heart: Nargis :heart: Nargis :heart: ...")
        st.balloons()

    if button_clicked:
        reveal_crush()

