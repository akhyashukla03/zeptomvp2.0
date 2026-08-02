import streamlit as st
import streamlit.components.v1 as components
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Zepto Cross-Category Discovery | Live MVP & Submission Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Sleek Dark Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #130d1e;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(135deg, #7c3aed, #9333ea);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
    }
    .submission-bar {
        background: linear-gradient(135deg, #1e1430, #281545);
        border: 2px solid #7c3aed;
        border-radius: 12px;
        padding: 16px 24px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation & Deliverables
st.sidebar.title("⚡ Zepto PM Portal")
st.sidebar.caption("Growth PM Graduation Project Submission")

page = st.sidebar.radio(
    "Select Component:",
    [
        "📱 Live MVP Prototype Trial",
        "🧠 AI Review Analysis Workflow (10k Reviews)",
        "📄 Official 10-Slide Pitch Deck (PDF)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("📥 Official Deliverables")

pdf_path = os.path.join(os.path.dirname(__file__), "NL_Zepto_Growth_PM_Graduation_Project.pdf")
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        st.sidebar.download_button(
            label="📄 Download Submission PDF (NL Zepto.pdf)",
            data=f.read(),
            file_name="NL Zepto.pdf",
            mime="application/pdf",
            use_container_width=True
        )

pptx_path = os.path.join(os.path.dirname(__file__), "NL_Zepto_Growth_PM_Graduation_Project.pptx")
if os.path.exists(pptx_path):
    with open(pptx_path, "rb") as f:
        st.sidebar.download_button(
            label="📊 Download Editable PPTX Deck",
            data=f.read(),
            file_name="NL_Zepto_Growth_PM_Graduation_Project.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            use_container_width=True
        )

st.sidebar.markdown("---")
st.sidebar.markdown("🎨 **[Open Figma Vector Design System](https://www.figma.com/design/2gZJHtjmpnI677IhC66PqZ/Untitled?node-id=0-1)**")

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

def render_portal(height=1150):
    components.html(bundled_html, height=height, scrolling=True)

if page == "📱 Live MVP Prototype Trial":
    st.title("📱 Zepto AI Cross-Category Discovery MVP")
    st.caption("Interactive live mobile simulator: Persona Neha, ₹0 B2B Sampler, Category Streak 2x Points, SkinMatch AI, Model B Dark Store CCTV Quality Vault.")
    render_portal(1150)

elif page == "🧠 AI Review Analysis Workflow (10k Reviews)":
    st.title("🧠 AI Review Analysis Workflow Engine")
    st.caption("Ingested 10,000 customer review records across 10 social channels to identify buying frictions and feature demands.")
    render_portal(1150)

elif page == "📄 Official 10-Slide Pitch Deck (PDF)":
    st.title("📄 Official 10-Slide Presentation Pitch Deck")
    st.caption("Widescreen 16:9 vector PDF deck complying strictly with all submission guidelines (Anonymous, 10 slides, >=14pt font, <40MB).")
    
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📄 Download Official PDF Deck (NL Zepto.pdf)",
                data=f.read(),
                file_name="NL Zepto.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    st.markdown("---")
    render_portal(1100)
