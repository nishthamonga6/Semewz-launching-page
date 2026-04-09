import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="SEMEWZ | Launched",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown("""
<style>
/* Luxury Font */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,500;1,600&display=swap');

/* Hide Streamlit UI */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Background */
[data-testid="stAppViewContainer"] {
    background: #F2D3C5;
}

/* Force Global Centering for all Streamlit Elements */
[data-testid="stVerticalBlock"] {
    align-items: center;
}

/* Layout */
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

/* Logo Sizing */
.logo-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 10px;
}

.logo-wrapper img {
    width: 90px; /* Smaller, elegant width */
    height: auto;
}

/* Hero Section */
.hero {
    text-align: center;
}

.hero h1 {
    font-size: clamp(40px, 8vw, 80px);
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-weight: 600;
    color: black;
    margin-top: 0;
    margin-bottom: 5px;
}

.hero p {
    font-size: clamp(18px, 4vw, 24px);
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    color: #333;
    line-height: 1.4;
    margin-bottom: 30px;
}

/* Countdown */
.countdown {
    display: flex;
    justify-content: center;
    gap: clamp(15px, 5vw, 50px);
    margin-bottom: 50px;
}

.time-box {
    text-align: center;
}

.time-number {
    font-size: clamp(30px, 6vw, 55px);
    font-family: 'Cormorant Garamond', serif;
    font-weight: 500;
    color: black;
}

.time-label {
    font-size: 11px;
    letter-spacing: 2px;
    color: #444;
}

/* Features */
.features {
    display: flex;
    justify-content: center;
    text-align: center;
    flex-wrap: wrap;
    margin-top: 30px;
    gap: 20px;
}

.feature-card {
    flex: 1;
    min-width: 200px;
    max-width: 300px;
}

.feature-card h3 {
    font-size: 22px;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
}

.feature-card p {
    color: #444;
    font-size: 15px;
    font-family: 'Cormorant Garamond', serif;
}

/* Footer with Address */
.footer {
    text-align: center;
    margin-top: 60px;
    padding-bottom: 40px;
    color: #444;
    font-size: 14px;
    font-family: 'Cormorant Garamond', serif;
    line-height: 1.6;
}

.footer-info {
    margin-top: 10px;
    font-style: normal;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# 1. Logo (Using a markdown wrapper for perfect centering)
if os.path.exists("logo.png"):
    st.markdown('<div class="logo-wrapper">', unsafe_allow_html=True)
    st.image("logo.png", width=90)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. Hero Section
st.markdown("""
<div class="hero">
    <h1>Launched Come Visit Us</h1>
    <p>Where you become your own muse.<br>
    Timeless shirts & coords for polished comfort.</p>
</div>
""", unsafe_allow_html=True)

# 3. Static Features & Footer (Updated with Address & Phone)
st.markdown("""
<div class="features">
    <div class="feature-card">
        <h3>Luxury Identity</h3>
        <p>Crafted for women who define their own style.</p>
    </div>
    <div class="feature-card">
        <h3>Premium Fashion</h3>
        <p>Minimal silhouettes with timeless elegance.</p>
    </div>
    <div class="feature-card">
        <h3>Own Your Muse</h3>
        <p>Wear confidence in every collection.</p>
    </div>
</div>

<div class="footer">
    <div>© 2026 SEMEWZ • Be your own muse</div>
    <div class="footer-info">
        Beri wali gali, Surat Garia Market, Sirsa<br>
        Contact: +91 9812594125
    </div>
</div>
""", unsafe_allow_html=True)

