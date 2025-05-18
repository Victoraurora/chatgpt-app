import openai
import streamlit as st
import os

# Use a variável de ambiente definida no Streamlit Cloud
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="ChatGPT Simples", layout="centered")
st.title("🤖 ChatGPT com Streamlit")

# Histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Você é um assistente amigável e útil."}
    ]

# Entrada do usuário
user_input = st.text_input("Você:", "")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # GPT-4 funciona, mas gpt-3.5 é mais barato
        messages=st.session_state.messages
    )

    reply = response.choices[0].message["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Exibe o histórico
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"*Você:* {msg['content']}")
    else:
        st.markdown(f"*ChatGPT:* {msg['content']}")
