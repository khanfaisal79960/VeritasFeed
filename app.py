# app.py

import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Retrieve API key directly from environment variables
# It's crucial that NEWS_API_KEY is set in your system's environment
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_BASE_URL = "https://newsapi.org/v2/"

# --- Helper Functions ---

def fetch_news(endpoint, params=None):
    """
    Fetches news data from the NewsAPI.
    Args:
        endpoint (str): The API endpoint (e.g., 'top-headlines', 'everything').
        params (dict): Optional dictionary of query parameters.
    Returns:
        dict: JSON response from the API, or an empty dict if an error occurs.
    """
    if not NEWS_API_KEY:
        print("Error: NEWS_API_KEY environment variable is not set.")
        # You might want to render an error page or display a message to the user
        return {"articles": []}

    url = f"{NEWS_API_BASE_URL}{endpoint}"
    headers = {"X-Api-Key": NEWS_API_KEY}
    
    # Default parameters
    default_params = {
        "language": "en",
        "pageSize": 20 # Fetch 20 articles by default
    }
    if params:
        default_params.update(params)

    try:
        response = requests.get(url, headers=headers, params=default_params)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news from API: {e}")
        return {"articles": []}

def get_placeholder_image(category=None):
    """
    Returns a placeholder image path based on category.
    """
    if category == "technology":
        return "/static/images/placeholder_tech.jpg"
    elif category == "sports":
        return "/static/images/placeholder_sports.jpg"
    else:
        return "/static/images/placeholder_news.jpg"

# --- Routes ---

@app.route("/")
def index():
    """
    Renders the homepage with top headlines.
    """
    top_headlines = fetch_news("top-headlines", {"country": "us"})
    articles = top_headlines.get("articles", [])
    
    # Add placeholder images if original image is missing
    for article in articles:
        if not article.get("urlToImage"):
            article["urlToImage"] = get_placeholder_image()

    return render_template("index.html", articles=articles, title="Top Headlines")

@app.route("/category/<string:category_name>")
def category(category_name):
    """
    Renders a page showing news for a specific category.
    """
    category_headlines = fetch_news("top-headlines", {"category": category_name, "country": "us"})
    articles = category_headlines.get("articles", [])

    # Add placeholder images if original image is missing
    for article in articles:
        if not article.get("urlToImage"):
            article["urlToImage"] = get_placeholder_image(category_name)
            
    return render_template("category.html", articles=articles, title=f"{category_name.capitalize()} News", category=category_name)

@app.route("/search")
def search():
    """
    Handles news search functionality.
    """
    query = request.args.get("q", "").strip()
    articles = []
    if query:
        search_results = fetch_news("everything", {"q": query, "sortBy": "relevancy"})
        articles = search_results.get("articles", [])
        
        # Add placeholder images if original image is missing
        for article in articles:
            if not article.get("urlToImage"):
                article["urlToImage"] = get_placeholder_image()

    return render_template("search.html", articles=articles, query=query, title=f"Search Results for '{query}'")

# --- Error Handling ---
@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 Not Found errors."""
    return render_template("error.html", error_code=404, error_message="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handles 500 Internal Server errors."""
    return render_template("error.html", error_code=500, error_message="Internal Server Error"), 500

if __name__ == "__main__":
    app.run(debug=True) # Set debug=False in production
