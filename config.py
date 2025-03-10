"""
config.py
---------
This module contains configuration constants for the audio monitoring project.
Adjust the parameters below to customize the behavior of the system.
"""

import os

# Working hours
VOICE_ACTIVE_HOUR_START = '00:00'
VOICE_ACTIVE_HOUR_END = '23:59'
TIME_ZONE = 'Australia/Sydney'


# Stream Settings
STREAM_RATE = 16000  # 16000 samples per second
STREAM_CHANNELS = 1
STREAM_CHUNK_SIZE = 1024  # How many chunks will trigger callback

# Audio Processing Configurations
VOICE_BATCH_SIZE = 3 # When it reaches 3 samples, it will be sent to classify
VOICE_THREAD_LOOP_PERIOD = 0.5  # Loop every 0.5s
EMERGENCY_CONFIRM_RECORD_DURATION = 3  # seconds to record user response for emergency confirmation
SILENCE_THRESHOLD = 100 #

# Help Detection Thresholds
# Number of consecutive chunks (each of AUDIO_CHUNK_DURATION) allowed between "help" detections
# For example, 8 chunks * 1.5 sec = 12 seconds maximum interval
HELP_DETECTION_THRESHOLD_CHUNKS = 8

# TensorFlow Model Configuration (for initial "help" classification)
TF_MODEL_PATH = os.path.join("model", "model2.tflite")
TF_MODEL_CONFIDENCE_THRESHOLD = 0.5  # minimum probability to consider a detection as "help"

# Whisper Model Configuration (for double-checking long audio segments)
WHISPER_MODEL_PATH = os.path.join("models", "whisper_model.pt")
WHISPER_HELP_KEYWORD = "help"  # keyword to verify in the long audio segment
WHISPER_NEGATIVE_KEYWORD = "no"  # keyword to detect a negative response during emergency confirmation

# MQTT Configuration (for sending alerts to other systems)
MQTT_BROKER_ADDRESS = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC_EMERGENCY = "emergency/alert"

# Audio Playback Configuration (for prompting the user)
AUDIO_PROMPT_PATH = os.path.join("audio", "prompt_is_it_emergency.wav")
AUDIO_EMERGENCY_RESPONSE_PATH = os.path.join("audio", "activated_alarm.wav")

# State Machine Statuses
STATE_IDLE = "IDLE"      # Waiting for first "help" detection
STATE_T0 = "T0"             # First "help" detected; waiting for second "help"
STATE_T1 = "T1"             # Second "help" detected; awaiting verification by Whisper (blocking further processing)
STATE_T3 = "T3"             # Verification complete; system ready to prompt for emergency confirmation
STATE_T4 = "T4"             # Recording user's emergency confirmation response (help detection paused)
STATE_T5 = "T5"             # Awaiting Whisper analysis on the recorded emergency confirmation

# Add more configurations below as needed
