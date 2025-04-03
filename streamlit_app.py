import streamlit as st
import os


# Loading external CSS
def load_css(file_name):
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    if os.path.exists(css_path):
      st.write("styles.css found!")
    else:
      st.write("styles.css NOT found!")
    with open(file_name, "r") as f:
        css = f.read()
    return f"<style>{css}</style>"


# Applying CSS styles
st.markdown(load_css("styles.css"), unsafe_allow_html=True)


st.title("AuraLens")
st.write("This app analyzes emotions in tweets!")