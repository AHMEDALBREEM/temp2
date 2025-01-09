from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

def emotion_predictor(text):
    """
    Predicts the emotions in the given text using Watson NLP.
    Raises a ValueError if the input text is blank.
    """
    if not text:
        raise ValueError("Input text cannot be blank.")

    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        iam_apikey='YOUR_API_KEY',
        url='YOUR_SERVICE_URL'
    )

    response = nlu.analyze(
        text=text,
        features=Features(sentiment=SentimentOptions())
    ).get_result()

    formatted_response = {
        'emotion': response['sentiment']['document']['label'],
        'score': response['sentiment']['document']['score']
    }
    return formatted_response
