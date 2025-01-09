import unittest
from emotion_detector import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_emotion_predictor(self):
        sample_text = "I am so happy today!"
        result = emotion_predictor(sample_text)
        self.assertIn('emotion', result)
        self.assertIn('score', result)

if __name__ == "__main__":
    unittest.main()
