# app.py

import os
import requests
import gradio as gr

# Use environment variable for API key
groq_api_key = os.getenv("GROQ_API_KEY")

# API endpoint and headers
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {groq_api_key}"
}

def chat_with_groq(user_input):
    body = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.json()}"

# Gradio interface
interface = gr.Interface(
    fn=chat_with_groq,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything..."),
    outputs=gr.Textbox(),
    title="DDS Chat with Groq AI (llama-3.1-8b-instant)",
    description="Type your question below and get a response powered by Groq's llama model."
)

interface.launch()
