import streamlit as st
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

api_key = os.getenv("MISTRAL_API_KEY")
""""Note you can get the MISTRAL API from the official website to subscribing at
https://auth.mistral.ai/ui/login?flow=94362866-2bfa-42ea-b73f-f9227693422b
also its not allowed to expose the the KEY save it in environment variable b
y using the following command
    echo 'export MISTRAL_API_KEY="your_openai_api_key"' >> ~/.bashrc
    source ~/.bashrc
    then get it the source code by using
    api_key = os.getenv("MISTRAL_API_KEY")
"""
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)


st.title("KRAI CHAT")
input = st.text_input("Enter your question")
if input:
    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=input)]
    )
    st.write(chat_response.choices[0].message.content)