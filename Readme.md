Simple app that runs locally on your system and you can query after adding some facts in a supporting file called knowledge.txt

## Steps
python3 -m venv .venv          
source .venv/bin/activate      
pip install -r requirements.txt   
ollama pull llama3.2:1b
ollama run llama3.2:1b 
Ctrl+D                        
python3 app.py                 
