# Document Search Engine

A Flask-based TF-IDF document search engine powered by MongoDB.  
This was developed as part of the CIS 593 Final Project at Cleveland State University.

## Features
- Upload and store text documents in MongoDB
- Compute TF-IDF vectors using Python
- Query search interface using cosine similarity
- Frontend built with Flask and HTML templates

## Technologies Used
- Python
- Flask
- MongoDB
- Sklearn (TF-IDF)
- HTML/CSS

## Project Structure
CIS_593_Document_Search_Engine/
- app.py # Flask server and routing
- preprocess.py # Lemmatization, stopword removal, etc.
- TFIDF_search.py # TF-IDF generation and similarity computation
- test_search.py # Test script for query functionality
- templates/
  - search.html # UI template
- .gitignore # Ignored files

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Parth568/Document_Search_Engine.git
   cd Document_Search_Engine

2. Install required libraries
pip install -r requirements.txt
4. Run the Flask server
 python app.py 
5. Open in your browser
http://localhost:5000/

