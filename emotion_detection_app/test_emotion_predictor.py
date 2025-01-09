# Test script to verify the output format of the emotion_predictor function
from emotion_detector import emotion_predictor

def test_emotion_predictor():
    sample_text = "I am so happy today!"
    result = emotion_predictor(sample_text)
    print(result)

if __name__ == "__main__":
    test_emotion_predictor()
