import streamlit as st

# Defining inline CSS
inline_css = """
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #f0f8ff !important;
    }

    [data-testid="stApp"] {
        background-color: #f0f8ff !important;
    }

    h1 {
        color: #4a4a8a !important;  
        text-align: center !important;
    }

    p {
        color: #5a5a5a !important;
        text-align: center !important;
    }
</style>
"""


# Applying CSS inline
st.markdown(inline_css, unsafe_allow_html=True)


#Frontend View
st.title("AuraLens")
st.write("This app analyzes emotions in tweets!")