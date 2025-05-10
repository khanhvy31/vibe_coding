import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

st.set_page_config(page_title="Hugging Face Chatbot", page_icon="🤖")

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")
    return tokenizer, model

tokenizer, model = load_model()

if "chat_history_ids" not in st.session_state:
    st.session_state.chat_history_ids = None
if "past" not in st.session_state:
    st.session_state.past = []
if "generated" not in st.session_state:
    st.session_state.generated = []

st.title("🤖 Hugging Face Chatbot")
st.write("Chat with a free Hugging Face model (DialoGPT-small).")

if st.session_state.generated:
    for i in range(len(st.session_state.generated)):
        st.markdown(f"**You:** {st.session_state.past[i]}")
        st.markdown(f"**Bot:** {st.session_state.generated[i]}")

def send_message():
    user_input = st.session_state.input
    if user_input:
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        bot_input_ids = (
            torch.cat([st.session_state.chat_history_ids, new_input_ids], dim=-1)
            if st.session_state.chat_history_ids is not None
            else new_input_ids
        )

        chat_history_ids = model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
        )

        response = tokenizer.decode(
            chat_history_ids[:, bot_input_ids.shape[-1]:][0],
            skip_special_tokens=True,
        )

        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        st.session_state.chat_history_ids = chat_history_ids
        st.session_state.input = ""  # This is safe in on_change callback

st.text_input("You:", key="input", on_change=send_message)
