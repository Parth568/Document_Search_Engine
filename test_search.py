from TFIDF_search import search_reviews
from preprocess import preprocess

def get_user_query():
    query = input("\nEnter your search query (or type 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        return None
    return query

def display_results(results):
    print("\n Top Matching Reviews:")
    print("\n{:<5} {:<10} {:<25} {:<15} {:<5} {}".format("No.", "Score", "Business Name", "Place", "stars","Review"))
    print("-" * 150)

    for idx, result in enumerate(results, 1):
        print("{:<5} {:<10} {:<25} {:<15} {:<5} {}".format(
            idx,
            result['score'],
            result['business_name'][:24],
            result['city'][:14],
            result['stars'],
            result['review'][:80] + ("..." if len(result['review']) > 80 else "")
            ))
def main():
    print("\n Welcome to the Yelp Review Search Engine!")
    while True:
        query = get_user_query()
        if query is None:
            print("\n Goodbye! Thanks for using the search engine!")
            break

        cleaned_query = preprocess(query)
        if not cleaned_query.strip():
            print("\n Your query is too generic or empty after cleaning. Please use better keywords!")
            continue

        results = search_reviews(query)

        if not results:
            print("\n No result found. Try a different query.")
        else:
            display_results(results)

if __name__ == "__main__":
    main()
