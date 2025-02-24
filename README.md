# Web-Content-Q-A-Tool-UI-Focused-
Web Content Q&amp;A Tool (UI-Focused)



# Author: @akash kumar

Description:
This Flask application creates a web-based Q&A tool.  Users can input URLs, 
ask questions about the content of those pages, and receive answers 
based solely on the ingested information, without relying on general 
knowledge.

# Resources Used:
Google Gemini, Flask 2.0 (for prompt engineering, code development, and debugging).

# Main Tools and Technologies:
1. Jupyter Notebook, Terminal
2. Python, HTML (for UI)
3. Frameworks: Flask (backend), LangChain (LLM interaction)
4. Cohere LLM, FAISS Vector Database, Cohere Embeddings

# HOW To Run Locally:

1. clone this repository in your local PC (and please make sure python enviorment is installed in local PC)
use "$ git clone https://github.com/Akash671/Web-Content-Q-A-Tool-UI-Focused-.git" command to clone this repository

 then go to the "Web-Content-Q-A-Tool-UI-Focused" folder and in this folder there is two main component.
 i). templates ---> folder contains UI code
 ii). app.py ----> python file contains main code
 iii). now open cmd/terminal in same directory 

2. Install Libraries:
   run below command on cmd/terminal
   pip install Flask beautifulsoup4 requests langchain-community langchain-cohere faiss-cpu


3. Set Cohere API Key:
Replace "YOUR_COHERE_API_KEY" with your actual Cohere API key in app.py file and save this file. Using environment variables (as shown below) is the recommended approach.

4. Run the App(run below command on cmd/terminal:

python app.py

5. Open in Browser:
Open your web browser and go to http://127.0.0.1:5000/

now UI is open and user can intract with that.
