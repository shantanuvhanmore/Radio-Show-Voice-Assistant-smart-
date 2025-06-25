import requests
import re
import os

def get_latest_news(api_key, num_articles=5, country='us'):
    """Fetch latest news headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'ok':
            return data['articles'][:num_articles]
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return []
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

def display_news(articles):
    """Display news articles in a readable format"""
    if not articles:
        print("Sorry, couldn't fetch any news at the moment.")
        return
    
    print("\nHere are the latest headlines:")
    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Published: {article['publishedAt'][:10]}")  # Just show date


def is_news_request(user_input):
    """Check if user is asking for news"""
    news_keywords = ['news', 'headlines', 'updates', 'current affairs', 'latest']
    return any(re.search(rf'\b{keyword}\b', user_input.lower()) for keyword in news_keywords)

def main():
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Replace with your actual API key as a string with "os.getenv("NEWS_API_KEY")"
    
    print("News Bot: Type your request (e.g., 'Tell me the latest news') or 'quit' to exit")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("News Bot: Goodbye!")
            break
            
        if is_news_request(user_input):
            articles = get_latest_news(NEWS_API_KEY)
            display_news(articles)
        else:
            print("News Bot: I can provide the latest news. Try asking something like:")
            print(" - 'Tell me the latest news'")
            print(" - 'Show me headlines'")
            print(" - 'What's happening in the world?'")

if __name__ == "__main__":
    main()