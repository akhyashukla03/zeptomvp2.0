# 🚀 Zepto Growth PM Project: Startup & Presentation Walkthrough Guide

> **Welcome Evaluators & Presenters!** This guide provides a complete, step-by-step walkthrough script and navigation map for presenting the **Zepto Cross-Category Discovery Engine & MVP Project**.

---

## 🎙️ Executive Presentation Script (Slide-by-Slide Narrative)

When presenting this project to a Senior PM Evaluator, team, or review panel, follow this structured narrative:

### 📍 Slide 1: Executive Brief & EBITDA Opportunity
* **Presenter Script**: 
  > *"Quick commerce platforms like Zepto, Blinkit, and Instamart have mastered 10-minute grocery delivery. However, 71.2% of users are locked into daily grocery habits (Milk, Bread, Eggs) in <45-second checkout flows. Daily groceries yield low ~10% gross margins vs 35%–50% for Beauty, Pet Care, and Utility items. Our core strategic goal is to increase Monthly Active Customers who purchase from 2+ categories from **8.2% to 28.4%**, unlocking **+300bps in blended EBITDA margin**."*

### 📍 Slide 2 & 3: Market Leakage & 10,000 Scraped Reviews Corpus
* **Presenter Script**: 
  > *"To understand why users don't buy non-grocery items on Zepto, we built an AI Discovery Engine that scraped and analyzed **10,000 customer feedback records** across 10 social channels (Play Store, App Store, Reddit, Twitter, Quora, MouthShut, LinkedIn, Trustpilot). We found users leak bulk purchases to Amazon/DMart, but want convenience top-ups on Zepto. The top buying friction is **Quality & Expiry Fear (20.1%)**—users worry active skincare or pet food degrades in hot dark stores."*

### 📍 Slide 4: Target Persona (Neha - Skincare Fan)
* **Presenter Script**: 
  > *"Meet Neha, 26, a Bangalore Digital Marketer. She buys morning staples on Zepto 3x/week but leaks all skincare purchases to Nykaa. She wants to try premium skincare risk-free without committing to full bottles. As Neha says: 'If I got a free 15ml trial sample in my grocery bag with storage quality assurance, I'd switch from Nykaa immediately.'"*

### 📍 Slide 5 & 6: Opportunity Canvas & Ideation Prioritization
* **Presenter Script**: 
  > *"We evaluated 6 high-impact growth concepts on a Reach vs. Impact vs. Effort matrix. Our #1 prioritized wedge is **Zepto In-Bag B2B Sampler** (brand-sponsored ₹0 trial riding inside grocery bags) combined with **Category Streak Quests** (5-sticker loyalty board unlocking 2x points on daily milk)."*

### 📍 Slide 7 & 8: The Live MVP & 4-Layer System Architecture
* **Presenter Script**: 
  > *"Here is our live MVP. It features a ₹0 B2B trial sampler that rides inside regular grocery bags at zero extra delivery CAC, a 5-sticker Routine Quest board unlocking 2x points on daily milk, SkinMatch AI undertone camera scanner, and Model B Dark Store Storage Quality Vault displaying live 18.2°C temperature telemetry and overhead CCTV rack snapshots."*

### 📍 Slide 9 & 10: Incrementality Framework, Guardrails & GTM Roadmap
* **Presenter Script**: 
  > *"We validate Monthly Category Exploration Rate (MCER) growth using **10% randomized holdout control groups** to measure true incremental causal lift rather than raw attach proxies. Operational guardrails cap picker packing time at <3 seconds per order and AWS S3 photo storage costs under $15/month via 7-day auto-expire rules."*

---

## 🗺️ Master Navigation & Deliverables Directory

| Deliverable | Location / Access Link | Primary Purpose |
| :--- | :--- | :--- |
| 🌐 **Live Production App** | [`https://zeptomvp2.streamlit.app`](https://zeptomvp2.streamlit.app) | Interactive cloud app for live demo & grading |
| 📄 **Official Presentation PDF** | [`NL_Zepto_Growth_PM_Graduation_Project.pdf`](NL_Zepto_Growth_PM_Graduation_Project.pdf) | Widescreen vector PDF deck for submission |
| 📊 **Editable PowerPoint File** | [`NL_Zepto_Growth_PM_Graduation_Project.pptx`](NL_Zepto_Growth_PM_Graduation_Project.pptx) | Editable presentation file (.pptx) |
| 🎨 **Live Figma Design File** | [`Figma Live Design File`](https://www.figma.com/design/2gZJHtjmpnI677IhC66PqZ/Untitled?node-id=0-1) | 8 Editable vector UI screens & wireframes |
| 💻 **Interactive Web Simulator** | [`index.html`](index.html) | Full web simulator with guided PM tour |
| 🎨 **Figma SVG Assets** | [`figma_design_assets/`](figma_design_assets/) | Vector SVG design screens |
| 🧠 **10,000 Reviews Dataset** | [`data/reviews_dataset.json`](data/reviews_dataset.json) | Scraped multi-channel feedback dataset |
| 📝 **PM Strategy Document** | [`problem_statement.md`](problem_statement.md) | Comprehensive Growth PM framework |

---

## 🧪 60-Second Live Product Demo Flow

When demonstrating the live application to an evaluator:

1. Open **[`https://zeptomvp2.streamlit.app`](https://zeptomvp2.streamlit.app)** in your web browser.
2. Navigate to **Part 1 & 2: PM Discovery Engine & Research**:
   * Review the **10,000 Social Customer Reviews** sentiment breakdown (40% Positive Delights, 30% Neutral Requests, 30% Negative Frictions).
   * Expand the **8 Core Graduation PM Questions** scorecards.
3. Navigate to **Part 3 & 4: Interactive MVP Simulator**:
   * Select persona **Neha (Skincare Fan)**.
   * Observe the **Zepto Discovery Pass Active** badge.
   * Click **"+ Add ₹0 Sample"** on the **Cetaphil Gentle Cleanser (15ml)** card.
   * Observe the **Category Streak Board** (3/5 stickers unlocked -> **2x Grocery Points activated** on Milk & Bread).
   * Launch **SkinMatch AI Undertone Viewfinder** (98.4% shade match: Maybelline #128).
   * Check **Model B Dark Store Storage Quality Vault** (Surfaces **18.2°C** storage telemetry & live overhead rack CCTV snapshot).

---

## 💻 How to Run Locally

```bash
# 1. Clone Repository
git clone https://github.com/akhyashukla03/zeptomvp2.0.git
cd zeptomvp2.0

# 2. Option A: Run Streamlit Cloud App Locally
python -m streamlit run streamlit_app.py

# 3. Option B: Run Web Simulator Portal
python -m http.server 8080
# Open http://localhost:8080 in your browser
```

---

## 🎓 Evaluation Compliance Checklist
* [x] **Chosen Product**: Zepto (Growth PM Team).
* [x] **Target Objective**: Increase MAC buying 2+ categories from 8.2% ➔ 28.4%.
* [x] **Primary Research**: N=22 Live Survey & 5 In-depth Metro User Interviews.
* [x] **AI Data Corpus**: 10,000 Multi-Platform Social Reviews across 10 channels.
* [x] **Presentation Deck**: 10 Widescreen 16:9 Slides ($\ge 14\text{pt}$ minimum font size).
* [x] **Figma System**: 8 Editable Vector UI Screens linked via live URL.
* [x] **Production Deployment**: Live 200 OK Cloud URL (`https://zeptomvp2.streamlit.app`).
