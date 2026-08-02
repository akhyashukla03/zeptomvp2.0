import streamlit as st
import streamlit.components.v1 as components
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Zepto Cross-Category Discovery | Live MVP Trial",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit Header, Footer, and Sidebar Completely to Ensure 100% Top Header Visibility & Anonymity
st.markdown("""
    <style>
    /* Hide Streamlit Default Top Header, Footer, Sidebar, Viewer Badges & Avatars */
    header[data-testid="stHeader"], [data-testid="stHeader"] {
        display: none !important;
        height: 0px !important;
    }
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    footer, .stFooter, [data-testid="stFooter"], #MainMenu, #stDecoration, [data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }
    /* Hide Streamlit Cloud Floating Paper Boat Logo, Viewer Badge & Profile Avatar */
    [data-testid="stStatusWidget"],
    [data-testid="stViewerBadge"],
    .stViewerBadge,
    .viewerBadge,
    div[class*="viewerBadge"],
    div[class*="stViewerBadge"],
    div[class*="StatusWidget"],
    div[class*="stAppViewer"],
    div[class*="Profile"],
    a[href*="streamlit.app"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0px !important;
        width: 0px !important;
        pointer-events: none !important;
    }
    .stApp {
        background-color: #130d1e;
        color: #ffffff;
    }
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to build self-contained HTML bundle
def get_bundled_html():
    base_dir = os.path.dirname(__file__)
    index_path = os.path.join(base_dir, "index.html")
    css_path = os.path.join(base_dir, "style.css")
    js_path = os.path.join(base_dir, "app.js")
    reviews_path = os.path.join(base_dir, "data", "reviews_dataset.json")
    interviews_path = os.path.join(base_dir, "data", "interview_transcripts.json")
    deck_path = os.path.join(base_dir, "data", "deck_content.json")

    if not os.path.exists(index_path):
        return "<h1>index.html not found</h1>"

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Inline CSS
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()
        html = html.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css}\n</style>')

    # Inline JSON Datasets before app.js
    inlined_data_script = "<script>\n"
    if os.path.exists(reviews_path):
        with open(reviews_path, "r", encoding="utf-8") as f:
            inlined_data_script += f"window.reviewsData = {f.read()};\n"
    if os.path.exists(interviews_path):
        with open(interviews_path, "r", encoding="utf-8") as f:
            inlined_data_script += f"window.interviewsData = {f.read()};\n"
    if os.path.exists(deck_path):
        with open(deck_path, "r", encoding="utf-8") as f:
            inlined_data_script += f"window.slidesData = {f.read()};\n"
    inlined_data_script += "</script>\n"

    # Inline JS
    if os.path.exists(js_path):
        with open(js_path, "r", encoding="utf-8") as f:
            js = f.read()
        html = html.replace('<script src="app.js"></script>', f'{inlined_data_script}\n<script>\n{js}\n</script>')

    return html

bundled_html = get_bundled_html()

# Render Full-Width Interactive Web Application
components.html(bundled_html, height=1250, scrolling=True)
