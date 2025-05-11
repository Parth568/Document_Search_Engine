from flask import Flask, render_template, request
from TFIDF_search import search_reviews

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    query = ''
    results = []
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if query:
            results = search_reviews(query)

    return render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
