import streamlit as st


# Loading external CSS
def load_css(file_name):
    with open(file_name, "r") as f:
        css = f.read()
    return f"<style>{css}</style>"


# Applying CSS styles
st.markdown(load_css("styles.css"), unsafe_allow_html=True)


st.title("AuraLens")
st.write("This app analyzes emotions in tweets!")