# **Document Search Engine using TF-IDF, MongoDB, and Flask**

## **Overview**

This project implements an intelligent document search engine over Yelp's review dataset using TF-IDF and cosine similarity. It allows users to enter natural language queries and returns top-matching reviews ranked by semantic relevance. The system integrates a Flask web interface, MongoDB for storage, and Python-based NLP preprocessing.

---

## **Features**

- Query processing with text normalization
- TF-IDF vectorization on 10,000+ Yelp reviews
- Cosine similarity ranking
- MongoDB integration for business metadata
- Flask-based web interface for interaction
- Real-time query responses (< 1 second)

---

## **Project Structure**

─ app.py # Flask backend to serve search UI
─ TFIDF_search.py # Vectorization and similarity logic
─ preprocess.py # Text cleaning and normalization functions
─ templates/
    ─ search.html # Frontend Jinja2 template
─ static/
   ─ styles.css # (Optional) CSS styling for UI
─ README.md
─ requirements.txt # Python dependencies
─ test_search.py # CLI-based search testing script

---

## **Setup Instructions**

### **1.Clone the Repository**

- git clone <https://github.com/Parth568/Document_Search_Engine.git>
- cd TFIDF-Search-Engine

### **2.Create and activate a virtual environment**

- python -m venv venv
- source venv/bin/activate # On Windows: venv\Scripts\activate.bat

### **3. Install dependencies**

```bash
pip install pymongo
pip install nltk
pip install scikit-learn
pip install flask
```

### **4. Download NLTK corpora**

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

### **5. Setup MongoDB**

- Install MongoDB Community Server
- Launch mongod
- Import review.json and business.json into MongoDB using Compass or scripts

---

## **Running the Application**

python app.py
Visit http://127.0.0.1:5000 in your browser.

---

## **Usage Example**

1. Enter a query like best coffee near downtown
2. The system will:
   - Preprocess the query
   - Compare it with cleaned review vectors
   - Rank results using cosine similarity
   - Return top reviews with business name, city, and star rating

---

## **Sample Query Output**

| Score  | Business Name | City    | Stars | Review                                 |
| ------ | ------------- | ------- | ----- | -------------------------------------- |
| 0.8123 | Brew House    | Austin  | 4.5   | great coffee and cozy downtown spot... |
| 0.7965 | Java Central  | Houston | 4.0   | best espresso I've had in TX...        |

---

## **Known Issues / Improvements**

- Reviews shown are currently lowercased and cleaned (raw text can be used for better UX)
- MongoDB $lookup not used; all joins handled in code
- Semantic search (e.g., BERT) is not yet implemented

---

## **Author**

Parth Chaudhari

---

## **License**

MIT License or as per academic submission guidelines.

