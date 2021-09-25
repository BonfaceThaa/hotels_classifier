import os
import requests

from sent_classifier.database.database import get_reviews, update_review_sentiment

BASE_URL = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

headers = {
    'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
    'x-rapidapi-key': os.environ.get('x_rapidapi_key')
    }


def get_sentiment_update(review):
    """
    Function for fetching sentiment of review from rapidAPI
    :param review: online hotel review
    :return: list of sentiment and score of the review
    """
    response = requests.get(BASE_URL, headers=headers, params={'text': review})
    data = response.json()
    sentiment = data['type']
    score = data['score']
    return [sentiment, score]


# Fetch reviews from the database
reviews = get_reviews()

# Loop through reviews
for row in reviews:
    review_id = row[0]
    review = row[1]
    # request for sentiment for the review
    sentiment_data = get_sentiment_update(review)
    sentiment = sentiment_data[0]
    score = sentiment_data[1]
    # update the sentiment of the review in the database
    update_review_sentiment(review_id, sentiment, score)
