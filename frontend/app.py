import streamlit as st

# Page config
st.set_page_config(page_title="Server Sundaram", page_icon="🍽️", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>Server Sundaram</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-style: italic;'>Your healthy meal companion 🍽️</h3>", unsafe_allow_html=True)

# Image placeholder

st.image("frontend/images/Screenshot 2025-08-01 165246.png")  # Replace with your image path

# Section: Menu
st.markdown("## 🧾 Today's Menu")
menu_items = {
    "Idly": 15,
    "Dosa": 50,
    "Koozh": 50,
    "Ragi kali": 50,
    "Chapathi": 30,
    "Tea" : 15,
    "Coffee" : 15
}

# Display menu with prices
for item, price in menu_items.items():
    st.markdown(f"**{item}** — ₹{price}")

# Image placeholder for menu
#st.image("frontend/images/alaap-d-Fv3uNhZVMJU-unsplash.jpg ")
#st.image("frontend/images/shreyak-singh-gFB1IPmH6RE-unsplash.jpg")
st.image("frontend/images/Screenshot 2025-08-01 164929.png")
st.image("frontend/images/Screenshot 2025-08-01 165109.png")      
# Section: Order Form
st.markdown("---")
st.markdown("## 🛒 Place Your Order now through our Chat Bot Below")


import streamlit.components.v1 as components

chatbot_html = """
<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  intent="WELCOME"
  chat-title="Server_Sundaram"
  agent-id="40bb4085-7454-47fe-84f7-abe2277490f4"
  language-code="en"
></df-messenger>

<style>
  df-messenger {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 999;
  }
</style>
"""

components.html(chatbot_html, height=500)


# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 Server Sundaram. Eat Healthy, Live (Well)thy.</p>", unsafe_allow_html=True)
