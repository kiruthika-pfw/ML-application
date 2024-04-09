# app.py
import streamlit as st
import requests

def summarize_text(text):
    url = "http://localhost:8000/summarize"  # Update the port number if necessary
    payload = {"text": text}
    print("Request Payload:", payload)  # Print the request payload
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            if "summary" in data:
                return data["summary"]
    except Exception as e:
        st.error(f"Error occurred: {e}")
    return "Failed to summarize text"

st.title("Text Summarization Tool")

text_input = st.text_area("Enter text:")
if st.button("Summarize"):
    if text_input:
        summary = summarize_text(text_input)
        st.write("Summary:")
        st.write(summary)
    else:
        st.error("Please enter some text.")
