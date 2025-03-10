# audio_classifier.py
import tensorflow as tf
import numpy as np
from config import TF_MODEL_PATH, TF_MODEL_CONFIDENCE_THRESHOLD


class AudioClassifier:
    def __init__(self):
        self.model = tf.keras.models.load_model(TF_MODEL_PATH)

    def classify(self, audio_data):
        # Preprocess audio_data appropriately (placeholder implementation)
        processed_audio = self.preprocess(audio_data)
        prediction = self.model.predict(processed_audio)
        # Assume prediction[0][0] is the probability for "help"
        help_probability = prediction[0][0]
        is_help = help_probability >= TF_MODEL_CONFIDENCE_THRESHOLD
        return is_help, help_probability

    def preprocess(self, audio_data):
        # Dummy preprocessing: in a real scenario, convert raw audio bytes into the format
        # your model expects (e.g., spectrogram, MFCC, etc.)
        # For demonstration, we create a dummy numpy array.
        dummy_input = np.random.rand(1, 100).astype('float32')  # adjust dimensions as needed
        return dummy_input

# Usage:
# classifier = AudioClassifier()
# is_help, prob = classifier.classify(audio_chunk)
