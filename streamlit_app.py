import streamlit as st

# Defining inline CSS
inline_css = """
<style>
    body {
        background-color: #f0f8ff;  /* Soft Blue */
        font-family: Arial, sans-serif;
    }
    .stTitle {
        color: #4a4a8a;  /* Dark Blue for Title */
        text-align: center;
    }
    .stText {
        color: #5a5a5a;  /* Slightly Gray for Text */
        text-align: center;
    }
</style>
"""

# Apply CSS inline
st.markdown(inline_css, unsafe_allow_html=True)

st.title("AuraLens")
st.write("This app analyzes emotions in tweets!")
