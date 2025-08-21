def analyze_sentiment(text):
    positive_words = {'good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'amazing', 'awesome', 'fantastic', 'positive'}
    negative_words = {'bad', 'terrible', 'sad', 'hate', 'awful', 'horrible', 'worst', 'negative', 'poor', 'disappoint'}
    
    text_words = set(word.lower().strip('.,!?') for word in text.split())
    pos_count = len(text_words & positive_words)
    neg_count = len(text_words & negative_words)
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    user_input = input("Enter text for sentiment analysis: ")
    sentiment = analyze_sentiment(user_input)
    print(f"Sentiment: {sentiment}")