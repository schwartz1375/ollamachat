# Ollama Chat

`ollamachat.py` is a Python script that utilizes Streamlit to create a conversational AI app with multiple AI models. This script allows users to interact with different versions of the Ollama model, providing a simple and intuitive interface for real-time AI conversations.

## Features

- **Multiple AI Models:** Users can select from various AI models, such as "mistral-openorca:latest", "orca-mini", "codellama:13b-instruct", "llama2-uncensored:latest", and "llama2:13b".
- **Real-Time Conversations:** Integrates with Streamlit's conversational UI, allowing for seamless user-AI interactions.
- **History Tracking:** Maintains a history of the conversation, enabling context-aware responses from the AI.
- **Error Handling:** Incorporates exception handling to manage and display errors effectively.


## Dependencies
To run `ollamachat.py`, you need Python installed on your system along with the following dependencies:

- `streamlit`
- `langchain`

You can install these packages using pip, ensure you have `pip` installed on your system. If it's not installed, you can download and install it from the [official website](https://pip.pypa.io/en/stable/installation/).

Once `pip` is installed, you can install all required packages using the `requirements.txt` file included in the repository.

Open a terminal (command prompt), navigate to the directory containing `requirements.txt`, and run the following command:
```
pip install -r requirements.txt
```

### Installing Ollama

To use the Ollama models, you'll need to install and set up Ollama. Follow the instructions on the [Ollama website](https://ollama.ai/) for setup and installation guidelines.

Additionally, you can modify `ollamachat.py` to match the specific models you have installed. Update the `initialize_models` function in the script with the names of your installed models.

## Usage

1. **Start the Streamlit App:**
   ```
   streamlit run ollamachat.py
   ```
2. **Select an AI Model:** Use the dropdown menu to choose an AI model for the conversation.
3. **Engage in Conversation:** Type your messages and get responses from the selected AI model.


## Configuration

 The script initializes with predefined AI models, but you can modify or expand the model list in the `initialize_models` function.

## Debugging

If errors occur, the script is set up to display the exception details. Additionally, a traceback is printed for debugging purposes.

## Further Reading

For more details on building conversational apps with Streamlit, refer to these resources:
- [Streamlit Documentation](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)
- [Streamlit Chat API Reference](https://docs.streamlit.io/library/api-reference/chat)


## Acknowledgments
- Thanks to the [Streamlit community](https://streamlit.io/), the [LangChain community](https://github.com/LangChain/langchain), and [Ollama AI](https://ollama.ai/) for their continuous support and resources.
