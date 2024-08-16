import requests
import streamlit as st

def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }
    response = requests.post("https://lecl-translator.onrender.com/chain/invoke", json=json_body)
    return response.json().get("output", "Translation not found")

# Add a header
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 10px; text-align: center; border-radius: 5px;'>
        <h2 style='color: #333;'>Sky-Translator</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Streamlit app
# Add a dropdown menu for language selection
language = st.selectbox(
    "Select the language you want to translate to:",
    ["French", "Hindi", "Spanish", "German", "Chinese"]
)

input_text = st.text_input("Enter the text you want to convert to the selected language")

if input_text:
    translation = get_groq_response(input_text, language)
    st.write(translation)

# Add a footer
st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 5px; text-align: center; border-radius: 5px; margin-top: 50px;'>
        <p style='color: #666;'>LLM Application using LECL</p>
    </div>
    """,
    unsafe_allow_html=True
)
