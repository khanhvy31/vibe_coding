# Hugging Face Chatbot with Streamlit

This project is a simple chatbot web app using a free Hugging Face conversational model (DialoGPT-small) and Streamlit.

## Features

- Chat with an AI model for free (no API key required)
- Powered by [microsoft/DialoGPT-small](https://huggingface.co/microsoft/DialoGPT-small)
- Easy to run locally or deploy for free on [Streamlit Community Cloud](https://streamlit.io/cloud)

## Setup & Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run locally

```bash
streamlit run app.py
```

The app will open in your browser.

### 3. Deploy for free (Streamlit Community Cloud)

1. Push this project to a public GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign in.
3. Click "New app", select your repo, and set the main file path to `vibe_coding/app.py`.
4. Click "Deploy".

No Hugging Face API key is required for this model.

## File Structure

- `app.py` — Streamlit app with chatbot interface
- `requirements.txt` — Python dependencies

## License

MIT
