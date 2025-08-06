import streamlit as st
import requests
import webbrowser
import time

def open_link(url):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True)
# ✅ Must be at the very top
st.set_page_config(page_title="Aryan's FastAPI App", page_icon="⚡")

# ----------------- Constants -----------------
API_BASE = "https://aryans-first-fastapi.onrender.com/"

DUMMY_QUESTIONS = [
    "Who created this project?",
    "What does this project do?",
    "What are the endpoints?",
    "How can I run this project?",
    "Is it open source?",
    "Thank you!"
]

# ----------------- Sidebar -----------------
st.sidebar.title("📁 Project Info")
st.sidebar.markdown("""
### ⚡ Hello FastAPI
A minimal FastAPI project that responds with greetings and redirects.

**Author:** Aryan Bhan  
[🌐 GitHub](https://github.com/AryanBhan/hello_fast_api)  
[🔗 LinkedIn](https://www.linkedin.com/in/aryanbhan/)  

---

**Endpoints:**
- `/` → Hello message  
- `/owner` → Owner info  
- `/github` → Redirect to GitHub  
- `/linkedin` → Redirect to LinkedIn  
""")

# ----------------- Main Buttons -----------------
st.title("⚡ Aryan's FastAPI Demo")
st.markdown("Use the buttons below to interact with the FastAPI backend:")

col1, col2 = st.columns(2)

with col1:
    if st.button("👋 Say Hello"):
        try:
            res = requests.get(f"{API_BASE}/")
            st.success(res.json()["message"])
        except:
            st.error("FastAPI server is not running!")

    if st.button("🧑‍💻 Who's the Owner?"):
        try:
            res = requests.get(f"{API_BASE}/owner")
            st.info(res.json()["message"])
        except:
            st.error("FastAPI server is not running!")

with col2:
    if st.button("🔗 Open GitHub Repo"):
        open_link("https://github.com/AryanBhan/hello_fast_api")

    if st.button("🔗 Visit LinkedIn"):
        open_link("https://www.linkedin.com/in/aryanbhan/")


# ----------------- Chatbot Section -----------------
st.markdown("---")
st.subheader("💬 Ask the Bot about this Project")

# Dummy question buttons
cols = st.columns(len(DUMMY_QUESTIONS))
for i, question in enumerate(DUMMY_QUESTIONS):
    if cols[i].button(question):
        st.session_state.chat_input = question  # Sets the input field dynamically

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="chat_input")

def chatbot_response(msg):
    msg = msg.lower()
    if any(x in msg for x in ["who", "owner", "author", "made", "creator", "created"]):
        return "This project was created by Aryan Bhan. 😊"
    elif any(x in msg for x in ["what", "project", "about", "do", "does", "purpose"]):
        return "It's a FastAPI demo that responds to basic GET requests and redirects to GitHub and LinkedIn."
    elif "endpoint" in msg or "routes" in msg:
        return "Available endpoints are: `/`, `/owner`, `/github`, and `/linkedin`."
    elif "github" in msg:
        return "Here's the GitHub link: [GitHub → AryanBhan](https://github.com/AryanBhan/hello_fast_api)"
    elif "linkedin" in msg or "connect" in msg:
        return "You can connect with Aryan here: [LinkedIn → Aryan Bhan](https://www.linkedin.com/in/aryanbhan/)"
    elif "stack" in msg or "tech" in msg or "technology" in msg:
        return "This project uses FastAPI (Python) for backend and Streamlit for frontend."
    elif "run" in msg or "start" in msg or "launch" in msg:
        return "Start the FastAPI server with `uvicorn main:app --reload`, and run the Streamlit app with `streamlit run app.py`."
    elif "license" in msg or "open source" in msg:
        return "Yes, it's open-source under the MIT license. Feel free to use and modify!"
    elif "deploy" in msg or "host" in msg:
        return "You can deploy this FastAPI app to platforms like Render, Vercel, or Azure App Service."
    elif any(x in msg for x in ["thank you", "thanks", "thx", "ty", "appreciate"]):
        return "You're welcome! 😊 Let me know if you have more questions."
    else:
        return "Hii, I'm a simple bot! Ask me about the project, endpoints, author, or how to run it. 😊"

# Run chat interaction
if user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = chatbot_response(user_input)
    st.session_state.chat_history.append(("Bot", ""))

    for idx, (sender, message) in enumerate(st.session_state.chat_history):
        if sender == "Bot" and idx == len(st.session_state.chat_history) - 1:
            placeholder = st.empty()
            typed = ""
            for char in bot_reply:
                typed += char
                placeholder.markdown(f"**Bot:** {typed}")
                time.sleep(0.02)
            st.session_state.chat_history[-1] = ("Bot", bot_reply)
        else:
            st.markdown(f"**{sender}:** {message}")
