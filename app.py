"""

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

# To Run This:

1. Install Libraries:
   run below command on cmd/terminal
   pip install Flask beautifulsoup4 requests langchain-community langchain-cohere faiss-cpu


2. Set Cohere API Key:
Replace "YOUR_COHERE_API_KEY" with your actual Cohere API key in app.py file and save this file. Using environment variables (as shown below) is the recommended approach.

3. Run the App(run below command on cmd/terminal:

python app.py

4. Open in Browser:
Open your web browser and go to http://127.0.0.1:5000/

now UI is open and user can intract with that.

"""

from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from langchain_cohere import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import Cohere
import os

# Initialize the Flask application
app = Flask(__name__)

# Replace with your actual Cohere API key
COHERE_API_KEY = "YOUR_COHERE_API_KEY"  
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

# Initialize CohereEmbeddings ONCE, outside the function
embeddings = CohereEmbeddings(model="small")  # LLM model name

@app.route("/", methods=["GET", "POST"])
def index():
    answers = []
    if request.method == "POST":
        # Get URLs and question from the form
        urls = request.form.get("urls").splitlines()
        question = request.form.get("question")

        if urls and question:
            try:
                all_text = ""
                for url in urls:
                    try:
                        # Fetch content from the URL
                        response = requests.get(url)
                        response.raise_for_status()
                        soup = BeautifulSoup(response.content, "html.parser")
                        text = soup.get_text(strip=True)
                        all_text += text + "\n\n"

                    except requests.exceptions.RequestException as e:
                        return render_template("index.html", error=f"Error fetching URL {url}: {e}")

                if all_text:
                    # Split the text into chunks
                    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
                    docs = text_splitter.split_text(all_text)
                    db = FAISS.from_texts(docs, embeddings)  # Use the pre-initialized embeddings

                    # Initialize the language model
                    llm = Cohere(temperature=0)
                    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
                    
                    # Retrieve answer to the question
                    result = qa.run(question)
                    answers.append({"question": question, "answer": result})
                else:
                    return render_template("index.html", error="No content found in the provided URLs.")

            except Exception as e:
                return render_template("index.html", error=f"An error occurred: {e}")

    return render_template("index.html", answers=answers)

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
