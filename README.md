# Gemini Chatbot with Streaming Output

## Description

This script implements a simple command-line chatbot that interacts with Google's Gemini language model. It features a streaming output display, allowing the user to see the model's response being generated in real-time.

## Dependencies

The script requires the following Python libraries:
- `google-generativeai`: The official Python client for interacting with Google's generative AI models, including Gemini.
- `rich`: A library for creating rich text output and beautiful user interfaces in the terminal.
Specifically, it uses:
    - `rich.markdown`: For rendering Markdown text.
    - `rich.live`: For creating live updating displays.
    - `rich.console`: For rich terminal output.
- `time`: For pausing the execution momentarily to create a visual streaming effect.
- `os`: For accessing environment variables to securely store the API key.

## Installation

You can install the required dependencies using `pip`:
```bash
pip install google-generativeai rich

## Configuration                                                 

1. API Key: You need a Google API key with access to the Gemini model.
    - Set the GEMINI_API_KEY environment variable to your API key before running the script. For example:
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
2. Model: The script is configured to use the gemini-exp-1206 model. You can change this in the model_name variable if you want to use a different Gemini model.

3. Generation Config: The generation_config dictionary sets parameters that control the model's output. These include:
    - temperature: Controls the randomness of the output. Higher values (e.g., 1) make the output more creative but potentially less coherent. Lower values (e.g., 0) make the output more deterministic and focused. 
    - top_p: Nucleus sampling parameter, controlling the diversity of the output.
    - top_k: Limits the model's output to the top K most likely tokens.
    - max_output_tokens: Sets the maximum number of tokens the model can generate in a single response.
    - response_mime_type: Sets the format of the output.

## Usage

1. Save the script to a file, for example, `chat.py`.
2. Run the script from your terminal:
    ```bash
    python gemini_chatbot.py
3. The script will start an interactive chat session. You'll see the prompt "Juanda: ". Type your message and press Enter.  
4. The assistant's response will be displayed in a streaming fashion, with words appearing as they are generated.      

## Notes
- The chat history is initially empty, but it will accumulate as the conversation progresses.
- The script runs indefinitely until manually terminated (e.g., using Ctrl+C).
- The streaming output is designed to enhance the user experience by making the chatbot interaction feel more dynamic and responsive.

## License
MIT 2025
