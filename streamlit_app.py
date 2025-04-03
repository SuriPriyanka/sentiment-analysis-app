import os
import streamlit as st

# Check the directory contents
dir_path = os.path.dirname(__file__)
files_in_dir = os.listdir(dir_path)

st.write("Files in directory:", files_in_dir)

file_path = os.path.join(dir_path, "styles.css")
if os.path.exists(file_path):
    st.write("styles.css found!")
else:
    st.write("styles.css NOT found!")

# Load CSS if found
def load_css(file_name):
    with open(file_name, "r") as f:
        return f"<style>{f.read()}</style>"

# Try applying styles if the file exists
if os.path.exists(file_path):
    st.markdown(load_css(file_path), unsafe_allow_html=True)

st.title("AuraLens")
st.write("This app analyzes emotions in tweets!")
