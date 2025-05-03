from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["yelpdb"]
reviews_col = db["reviews"]
business_col = db["businesses"]

# Fetch 10000 Reviews and Preprocess
print(" Loading and preprocessing business details and their reviews...")
raw_reviews = list(reviews_col.find({}, {"text": 1, "business_id": 1, "_id": 0}).limit(10000))

texts = []
original_reviews = []
business_infos = []

for doc in raw_reviews:
    if "text" in doc and doc["text"]:
        cleaned_text = preprocess(doc["text"])
        texts.append(cleaned_text)
        original_reviews.append(doc["text"])

        business_id = doc.get("business_id")
        business_info = business_col.find_one({"business_id": business_id})

        business_name = business_info.get("name", "Unknown Business") if business_info else "Unknown Business"
        city = business_info.get("city", "unknown") if business_info else "Unknown"
        stars = business_info.get("stars", "N/A") if business_info else "N/A"

        business_infos.append({
            "business_name": business_name,
            "city": city,
            "stars": stars
        })

# Build TF-IDF Matrix
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(texts)

print(" TF-IDF Matrix created!")


# Search Function
def search_reviews(query, top_n=10):
    """Search reviews using cosine similarity."""
    cleaned_query = preprocess(query)
    query_vec = vectorizer.transform([cleaned_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    for idx, doc in enumerate(texts):
        if cleaned_query in doc:
            similarities[idx] += 0.1

    top_indices = similarities.argsort()[-top_n:][::-1]

    results = []
    for i in top_indices:
        results.append({
            "review": original_reviews[i],
            "score": round(similarities[i], 4),
            "business_name": business_infos[i]["business_name"],
            "city": business_infos[i]["city"],
            "stars": business_infos[i]["stars"]
        })

    return results
