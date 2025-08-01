
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

