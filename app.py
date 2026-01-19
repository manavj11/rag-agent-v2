import ollama
import gradio as gr

# Minimal function to process AI logic
def ai_assistant(user_input, context_file_path):
    # Read a local file to act as the "Knowledge Base"
    try:
        with open("knowledge.txt", "r") as f:
            context = f.read()
    except FileNotFoundError:
        context = "No local knowledge found."

    # Combine context with user question
    prompt = f"Use this info: {context}. Question: {user_input}"
    
    # Call local Ollama model
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': prompt},
    ])
    
    return response['message']['content']

# Simple UI components
view = gr.Interface(
    fn=ai_assistant,
    inputs=["text"],
    outputs="text",
    title="Minimal Local AI Assistant",
    description="I answer questions based on your local 'knowledge.txt' file."
)

view.launch()