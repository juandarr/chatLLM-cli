import google.generativeai as genai
from rich.markdown import Markdown
from rich.live import Live
from rich.console import Console
import time
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-exp-1206",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

while True:
    i = input("\nJuanda: ")
    response = chat_session.send_message(i, stream=True)

    # Initialize Rich components
    console = Console()
    accumulated_text = "\nAssistant: "
    md = Markdown("")

    with Live(md, auto_refresh=False) as live:
        for chunk in response:
            accumulated_text += chunk.text
            md = Markdown(accumulated_text)
            live.update(md, refresh=True)
            time.sleep(0.01) # Small delay to visualize streaming
