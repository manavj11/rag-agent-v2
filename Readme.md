# 🧠 Local RAG AI Agent / Knowledge App

A simple local AI app that lets you query a language model using custom facts stored in a text file. All processing runs locally—no cloud APIs or external services.

---

## ✨ Overview

- Fully offline, on-device AI using Ollama  
- Lightweight, quantized LLM suitable for consumer hardware  
- Custom knowledge injected at runtime (no fine-tuning)  
- Minimal Gradio-based web UI  

---

## Steps 

## Create and activate virtual environment
python3 -m venv .venv\
source .venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Pull and test model
ollama pull llama3.2:1b\
ollama run llama3.2:1b\
Exit with Ctrl + D

## Run app
python3 app.py\
Open the local Gradio URL shown in the terminal (usually http://127.0.0.1:7860)

---

## 📄 Knowledge Source
knowledge.txt contains all custom facts\
File contents are injected into the LLM prompt on each query

## 🧠 AI Concepts Demonstrated
On-Device AI: All inference runs locally\
Quantization: Uses Llama 3.2 1B for efficient local execution\
Context Stuffing: Prompt-based knowledge injection without fine-tuning


## 📂 Project Structure
app.py: The Python logic and Gradio UI.\
knowledge.txt: Your local "database."\
.gitignore: Prevents large system files (like .venv) from being uploaded to GitHub.
