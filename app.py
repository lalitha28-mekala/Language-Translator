import streamlit as st
import requests
import json

st.title("🌐 Language Translator App")

text = st.text_area("Enter English text")
language = st.radio("Select Language", ["Telugu", "Hindi", "Spanish",Urdu])

if st.button("Translate"):

    # ---------- EMPTY INPUT VALIDATION ----------
    if not text.strip():
        st.error("⚠️ Please enter text for translation.")
        st.stop()
    # --------------------------------------------

    url = "https://lalithamekala.app.n8n.cloud/webhook/40c19cc0-006a-4012-a696-18245a7f7b2b"
    payload = {
        "text": text,
        "language": language
    }

    response = requests.post(url, json=payload)
    result = response.json()

    translated = None

    # Case 1: result = [{'output': 'Hola'}]
    if isinstance(result, list) and "output" in result[0]:
        translated = result[0]["output"]

    # Case 2: when output is wrapped in ```json ... ```
    if isinstance(translated, str) and translated.startswith("```"):
        try:
            cleaned = translated.replace("```json", "").replace("```", "").strip()
            cleaned_json = json.loads(cleaned)
            translated = cleaned_json.get("output", translated)
        except:
            pass

    if translated:
        st.success(translated)
    else:
        st.error("Unexpected response format.")


