Simple app that runs locally on your system and you can query after adding some facts in a supporting file called knowledge.txt

## Steps (Enter the code in your terminal)
- Venv Creation - python3 -m venv .venv
  - source .venv/bin/activate      
- Req: pip install -r requirements.txt   
- Ollama pull and test: ollama pull llama3.2:1b
  - ollama run llama3.2:1b
  - Ctrl+D                        
- Run App - python3 app.py
- Open browser and test!

🧠 AI Concepts Demonstrated

On-Device AI: Processing happens locally; no data is sent to external servers (OpenAI/Google).

Quantization: Utilizing a 1-billion parameter model (Llama 3.2 1B) optimized for consumer hardware.

Context Stuffing: Passing local file content into the LLM prompt to provide custom knowledge without "fine-tuning."

📂 Project Structure

app.py: The Python logic and Gradio UI.

knowledge.txt: Your local "database."

.gitignore: Prevents large system files (like .venv) from being uploaded to GitHub.
