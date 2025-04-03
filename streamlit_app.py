import os
import streamlit as st

# Get the absolute path of styles.css
file_path = os.path.join(os.path.dirname(__file__), "styles.css")

# Debugging: Check if the file exists
if os.path.isfile(file_path):
    st.write("styles.css found!")
else:
    st.write("styles.css NOT found!")

# Load CSS only if the file exists
def load_css(path):
    with open(path, "r") as f:
        return f"<style>{f.read()}</style>"

if os.path.isfile(file_path):
    st.markdown(load_css(file_path), unsafe_allow_html=True)

st.title("AuraLens")
st.write("This app analyzes emotions in tweets!")
