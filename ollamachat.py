__author__ = 'Matthew Schwartz (@schwartz1375)'

import streamlit as st
from langchain.llms import Ollama
import traceback

# Function to initialize models - can be expanded or modified as needed
def initialize_models():
    models = {
        "mistral-openorca:latest": None,
        "orca-mini": None,
        "codellama:13b-instruct": None,
        "llama2-uncensored:latest": None,
        "llama2:13b": None
    }
    for model_name in models.keys():
        models[model_name] = Ollama(base_url='http://localhost:11434', model=model_name)
    return models

# Set up the page
st.title('🤔🦙 Talk to the Local AI models')

# Model Initialization
if "models" not in st.session_state:
    st.session_state.models = initialize_models()

# Model selection dropdown
model_names = list(st.session_state.models.keys())
selected_model = st.selectbox(label="Select a model", options=model_names, index=0)

# Initialize or access the session's message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))

# Chat input
prompt = st.chat_input('Enter your prompt here!')

if prompt:
    try:
        # Combine previous messages with the new prompt
        history_limit = 5  # Adjust as needed
        full_prompt = "\n".join([msg["content"] for msg in st.session_state.messages[-history_limit:]] + [prompt])

        # Add user's prompt to storage
        prompt_display = f'{selected_model}🤔 {prompt}'
        st.session_state.messages.append({"role": "user", "content": prompt_display})

        # Display what the user entered
        with st.chat_message("user"):
            st.write(prompt_display)

        # Get response from the model
        ollama_model = st.session_state.models[selected_model]
        response = ollama_model(full_prompt)

        # Store and display AI response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        traceback.print_exc()  # For debugging purposes