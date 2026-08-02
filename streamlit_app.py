import streamlit as st
import streamlit.components.v1 as components
import json
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Zepto Cross-Category Discovery | Self-Guided Growth PM Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Streamlit App
st.markdown("""
    <style>
    .stApp {
        background-color: #130d1e;
        color: #ffffff;
    }
    .css-1d38152 {
        background-color: #1b1328;
    }
    .stButton>button {
        background: linear-gradient(135deg, #7c3aed, #9333ea);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
    }
    .guide-banner {
        background: linear-gradient(135deg, #1e1430, #281545);
        border: 2px solid #7c3aed;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.2);
    }
    .guide-header {
        color: #f59e0b;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .step-box {
        background-color: #1e293b;
        border-left: 4px solid #10b981;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .badge-purple {
        background-color: #7c3aed;
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Top Welcome & Evaluator Startup Guide Banner
st.markdown("""
<div class="guide-banner">
    <div class="guide-header">⚡ Welcome Evaluator! Self-Guided Presentation & Startup Navigation Tour</div>
    <p style="color: #e2e8f0; font-size: 14px; margin-bottom: 15px;">
        This interactive portal is a <strong>100% self-explaining submission</strong> for the Zepto Growth PM Graduation Project. 
        No manual walkthrough is required—follow the guided steps below or use the sidebar navigation to evaluate every project component.
    </p>
</div>
""", unsafe_allow_html=True)

# Interactive Evaluator Tour Expander Guide
with st.expander("📖 **CLICK HERE FOR STEP-BY-STEP EVALUATOR PRESENTATION SCRIPT & DEMO WALKTHROUGH**", expanded=True):
    tour_tab1, tour_tab2, tour_tab3, tour_tab4 = st.tabs([
        "🎯 Step 1: Strategic Brief", 
        "🧠 Step 2: 10k AI Reviews Data", 
        "📱 Step 3: Live MVP Simulator Guide", 
        "📁 Step 4: Figma & Deliverables"
    ])
    
    with tour_tab1:
        st.markdown("""
        ### 📍 Step 1: Executive Problem Statement & EBITDA Opportunity
        * **The Grocery Tunnel Vision**: **71.2%** of active Zepto users repeatedly buy daily staples (Milk, Bread, Eggs) in <45-second checkout flows.
        * **The Exploration Deficit**: Only **8.2%** of Monthly Active Customers (MAC) explore high-margin non-grocery categories (*Beauty, Pets, Electronics*).
        * **The Margin Cliff**: Daily groceries yield low **~10% gross margins** vs **35%–50%** for Personal Care & Pet Supplies.
        * **Strategic Goal**: Increase 2+ category MAC from **8.2% ➔ 28.4%**, unlocking **+300bps in blended EBITDA margin**.
        """)
        
    with tour_tab2:
        st.markdown("""
        ### 📍 Step 2: 10,000 Social Customer Reviews Corpus
        * **Multi-Platform Scraped Corpus**: Analyzed 10,000 feedback records across 10 channels (*Play Store, App Store, Reddit, Twitter, Quora, LinkedIn, ProductHunt, Trustpilot, MouthShut*).
        * **Sentiment Breakdown**: **40% Positive Delights** (sub-10 min emergency refills), **30% Neutral Feature Requests**, **30% Negative Frictions**.
        * **Top Frictions Identified**: **Quality & Expiry Fear (20.1%)** (fear skincare degrades in hot dark stores) and **Bulk Buy Mismatch (19.9%)** (leaking bulk diapers/pet food to DMart/Amazon).
        """)
        
    with tour_tab3:
        st.markdown("""
        ### 📍 Step 3: How to Test the Live Interactive MVP Simulator (60-Second Demo)
        1. Scroll down to **"Part 3: Interactive Zepto AI MVP Simulator"**.
        2. Select Persona **Neha (Skincare Fan)** in the simulator controls.
        3. Observe **Zepto Discovery Pass Active** badge.
        4. Click **"+ Add ₹0 Sample"** on the **Cetaphil Gentle Cleanser (15ml)** card (rides inside regular grocery bags at zero extra delivery CAC).
        5. Observe the **Category Streak Board** (3/5 stickers unlocked ➔ **2x Grocery Points activated** on Milk & Bread).
        6. Launch **SkinMatch AI Viewfinder** (98.4% undertone shade recommendation: Maybelline #128).
        7. Audit **Model B Dark Store Storage Quality Vault** (Surfaces live **18.2°C** storage telemetry & overhead rack CCTV snapshot).
        """)
        
    with tour_tab4:
        st.markdown("""
        ### 📍 Step 4: Submission Links & Verification Directory
        * 📄 **Vector PDF Presentation**: [`NL_Zepto_Growth_PM_Graduation_Project.pdf`](NL_Zepto_Growth_PM_Graduation_Project.pdf)
        * 📊 **PowerPoint Presentation (.pptx)**: [`NL_Zepto_Growth_PM_Graduation_Project.pptx`](NL_Zepto_Growth_PM_Graduation_Project.pptx)
        * 🎨 **Live Figma Vector System**: [Figma Design System & Wireframes](https://www.figma.com/design/2gZJHtjmpnI677IhC66PqZ/Untitled?node-id=0-1)
        * 💻 **GitHub Repository**: [github.com/akhyashukla03/zeptomvp2.0](https://github.com/akhyashukla03/zeptomvp2.0)
        """)

# Sidebar Navigation
st.sidebar.title("⚡ Zepto PM Navigation")
st.sidebar.markdown("**Growth PM Graduation Project**")

page = st.sidebar.radio(
    "Select Section to Explore:",
    [
        "🚀 Full Interactive Web Portal & MVP",
        "📊 Part 1: AI PM Discovery Engine (10k Reviews)",
        "👥 Part 2: Primary User Research (N=22)",
        "📱 Part 3: Zepto AI MVP Simulator",
        "🖼️ Part 4: 10-Slide Pitch Deck (PDF/PPTX)"
    ]
)

# Download Deliverables Sidebar Section
st.sidebar.markdown("---")
st.sidebar.subheader("📥 Download Project Deliverables")

pdf_path = os.path.join(os.path.dirname(__file__), "NL_Zepto_Growth_PM_Graduation_Project.pdf")
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        st.sidebar.download_button(
            label="📄 Download PDF Pitch Deck",
            data=f.read(),
            file_name="NL_Zepto_Growth_PM_Graduation_Project.pdf",
            mime="application/pdf",
            use_container_width=True
        )

pptx_path = os.path.join(os.path.dirname(__file__), "NL_Zepto_Growth_PM_Graduation_Project.pptx")
if os.path.exists(pptx_path):
    with open(pptx_path, "rb") as f:
        st.sidebar.download_button(
            label="📊 Download PPTX Pitch Deck",
            data=f.read(),
            file_name="NL_Zepto_Growth_PM_Graduation_Project.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            use_container_width=True
        )

dataset_path = os.path.join(os.path.dirname(__file__), "data", "reviews_dataset.json")
if os.path.exists(dataset_path):
    with open(dataset_path, "rb") as f:
        st.sidebar.download_button(
            label="🧠 Download 10,000 Reviews Dataset",
            data=f.read(),
            file_name="reviews_dataset.json",
            mime="application/json",
            use_container_width=True
        )

st.sidebar.markdown("---")
st.sidebar.markdown("🎨 **[Open Live Figma Design File](https://www.figma.com/design/2gZJHtjmpnI677IhC66PqZ/Untitled?node-id=0-1)**")

# Helper function to build self-contained HTML bundle with inlined CSS, JS, and JSON Datasets
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

if page == "🚀 Full Interactive Web Portal & MVP":
    st.title("⚡ Zepto Cross-Category Discovery Portal & Interactive MVP")
    st.caption("Full production web portal featuring AI PM Engine, Survey Scorecards, Interactive iPhone Simulator, and Pitch Deck.")
    render_portal(1150)

elif page == "📊 Part 1: AI PM Discovery Engine (10k Reviews)":
    st.title("📊 Part 1: AI-Powered PM Discovery Engine")
    st.markdown("""
    **Dataset Scope**: 10,000 multi-platform social reviews across 10 channels (*Play Store, App Store, Reddit, Quora, LinkedIn, ProductHunt, Trustpilot, Twitter, MouthShut*).
    
    ### 🔑 Key Insight Summary:
    * **40% Positive Delights (4,000 records)**: High adoption for sub-10 min emergency refills (sunscreen, travel grooming, pet treats, fast phone chargers).
    * **30% Neutral Feature Requests (3,000 records)**: Unmet demand for AI Shade Matchers, Doorstep Try & Inspect, and Category Streak Points.
    * **30% Negative Frictions (3,000 records)**: Core barriers include dark-store expiry anxiety (20.1%) and refund bot loops (17%).
    """)
    render_portal(1050)

elif page == "👥 Part 2: Primary User Research (N=22)":
    st.title("👥 Part 2: Primary User Research & Cohort Validation")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Power-User Frequency", "82%", "1–4+ orders/week")
    col2.metric("Points Streak Preference", "68%", "Voted over cashback")
    col3.metric("Return Anxiety Blocker", "50%", "Refund chatbot loops")
    col4.metric("Doorstep Swap Trust", "91%", "3.0–5.0 rating")
    
    st.markdown("---")
    st.subheader("🗣️ 5 Metro User Transcripts (Bangalore, Mumbai, Delhi, Gurgaon)")
    render_portal(1050)

elif page == "📱 Part 3: Zepto AI MVP Simulator":
    st.title("📱 Part 3: Interactive Zepto AI MVP Simulator")
    st.info("💡 Evaluator Demo Guide: 1. Select persona Neha, 2. Claim free ₹0 Cetaphil cleanser trial sample, 3. View Category Streak Board (2x Points activated), 4. Launch SkinMatch AI, 5. Click 'View Storage Audit' for Model B CCTV logs!")
    render_portal(1100)

elif page == "🖼️ Part 4: 10-Slide Pitch Deck (PDF/PPTX)":
    st.title("🖼️ Part 4: 10-Slide Pitch Deck Deliverables")
    st.markdown("Download official submission files below or view the interactive deck in the portal:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📄 Download Official PDF Presentation Deck",
                    data=f.read(),
                    file_name="NL_Zepto_Growth_PM_Graduation_Project.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
    with col_b:
        if os.path.exists(pptx_path):
            with open(pptx_path, "rb") as f:
                st.download_button(
                    label="📊 Download Editable PowerPoint (.pptx) Deck",
                    data=f.read(),
                    file_name="NL_Zepto_Growth_PM_Graduation_Project.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    use_container_width=True
                )
    
    st.markdown("---")
    render_portal(1050)
