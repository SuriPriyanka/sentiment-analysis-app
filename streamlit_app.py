import streamlit as st
from streamlit_option_menu import option_menu

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


# Sidebar styling
st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Profile", "Notifications", "Settings", "Add another account", "Sign out", "Plans and Pricing", "Report Content", "Privacy Policy", "Suggest Improvement"],
        icons=["house", "person", "bell", "gear", "plus-circle", "box-arrow-right", "currency-dollar", "flag", "shield-lock", "lightbulb"],
        menu_icon="list",  # Icon for the menu
        default_index=0
    )