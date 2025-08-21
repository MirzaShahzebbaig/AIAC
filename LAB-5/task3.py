# Simple product recommendation system based on user search history

# Sample product categories and recommendations
recommendations = {
    "soap": ["Dove", "Lux", "Santoor"],
    "mobile": ["Mobile Cover", "Earphones", "Screen Protector"],
    "toys": ["Board Games", "Action Figures", "Puzzles"],
    "games": ["Game Console", "Video Games", "Game Accessories"]
}

def recommend_products(search_term):
    search_term = search_term.lower()
    for key in recommendations:
        if key in search_term:
            print(f"Based on your search for '{search_term}', you might also like:")
            for item in recommendations[key]:
                print(f"- {item}")
            return
    print("Sorry, no recommendations available for your search.")

if __name__ == "__main__":
    user_search = input("Enter what you searched for (e.g., soap, mobile, toys, games): ")
    recommend_products(user_search)