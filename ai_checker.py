from transformers import pipeline

# Load sentiment analysis model from HuggingFace
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_warning(message: str):
    result = sentiment_pipeline(message)[0]
    label = result['label']
    score = result['score']
    return label, score

