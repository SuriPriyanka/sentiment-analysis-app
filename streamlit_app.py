import streamlit as st

# Defining inline CSS
inline_css = """
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #E3F2FD !important;
    }

    [data-testid="stApp"] {
        background-color: #E3F2FD !important;
    }

    h1 {
        color: #673AB7 !important;  
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