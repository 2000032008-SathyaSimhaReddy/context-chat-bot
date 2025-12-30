import streamlit as st, requests
st.title("Context-Aware AI Chatbot")
msg = st.text_input("You")
if st.button("Send") and msg:
    r = requests.post("http://localhost:8000/chat", params={"message":msg}).json()
    st.write("Bot:", r["response"])
