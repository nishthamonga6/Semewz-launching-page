import streamlit as st
from PIL import Image
import os
from datetime import datetime, timedelta
import time

st.set_page_config(
    page_title="SEMEWZ | Launching Soon",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Launch date (15 days from now)
launch_date = datetime.now() + timedelta(days=15)

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

/* Layout */
.block-container {
    padding-top: 1rem;
    max-width: 1200px;
}

/* Animation */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Logo Center */
.logo-wrapper {
    width: 60%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 100px;
}

/* Ensure image stays centered */
.logo-wrapper img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 120px;
    max-width: 60vw;
}

/* Hero */
.hero {
    text-align: center;
    margin-top: 20px;
    animation: fadeUp 1.3s ease;
}

.hero h1 {
    font-size: 90px;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-weight: 600;
    color: black;
    margin-bottom: 10px;
}

.hero p {
    font-size: 24px;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    color: #333;
    margin-bottom: 55px;
}

/* Countdown */
.countdown {
    display: flex;
    justify-content: center;
    gap: 60px;
    margin-top: 40px;
    margin-bottom: 80px;
    flex-wrap: wrap;
}

.time-box {
    text-align: center;
}

.time-number {
    font-size: 64px;
    font-family: 'Cormorant Garamond', serif;
    font-weight: 500;
    color: black;
}

.time-label {
    font-size: 14px;
    letter-spacing: 2px;
    color: #444;
    font-family: 'Cormorant Garamond', serif;
}

/* Features */
.features {
    margin-top: 90px;
    display: flex;
    justify-content: space-around;
    text-align: center;
    flex-wrap: wrap;
}

.feature-card {
    margin: 20px;
}

.feature-card h3 {
    font-size: 26px;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
}

.feature-card p {
    color: #444;
    font-size: 16px;
    font-family: 'Cormorant Garamond', serif;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 100px;
    color: #555;
    font-size: 15px;
    font-family: 'Cormorant Garamond', serif;
}

/* Mobile responsive */
@media (max-width: 768px) {

.hero h1 {
    font-size: 48px;
}

.hero p {
    font-size: 18px;
}

.time-number {
    font-size: 40px;
}

.countdown {
    gap: 30px;
}

}

</style>
""", unsafe_allow_html=True)

# Logo centered for all screen sizes
if os.path.exists("logo.png"):
    image = Image.open("logo.png")
    st.markdown('<div class="logo-wrapper">', unsafe_allow_html=True)
    st.image(image)
    st.markdown('</div>', unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero">
    <h1>Launching Soon</h1>
    <p>Luxury fashion is arriving with elegance, identity, and timeless confidence.</p>
</div>
""", unsafe_allow_html=True)

# Countdown placeholder
placeholder = st.empty()

# Bottom placeholder
bottom = st.empty()

while True:

    now = datetime.now()
    remaining = launch_date - now

    days = remaining.days
    hours = remaining.seconds // 3600
    minutes = (remaining.seconds % 3600) // 60
    seconds = remaining.seconds % 60

    placeholder.markdown(f"""
    <div class="countdown">
        <div class="time-box">
            <div class="time-number">{days}</div>
            <div class="time-label">DAYS</div>
        </div>
        <div class="time-box">
            <div class="time-number">{hours}</div>
            <div class="time-label">HOURS</div>
        </div>
        <div class="time-box">
            <div class="time-number">{minutes}</div>
            <div class="time-label">MINUTES</div>
        </div>
        <div class="time-box">
            <div class="time-number">{seconds}</div>
            <div class="time-label">SECONDS</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    bottom.markdown("""
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
        © 2026 SEMEWZ • Be your own muse
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1)