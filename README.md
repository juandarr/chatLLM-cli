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

 ## License
 MIT 2025
