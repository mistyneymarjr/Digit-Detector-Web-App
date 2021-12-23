import digit
import helpstart
import streamlit as st

PAGES = {
    "Digit Recogniser": digit,
    "How to Use": helpstart
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()