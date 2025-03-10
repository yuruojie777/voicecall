# audio_prompt.py
import time
import pyaudio
import wave
from config import AUDIO_PROMPT_PATH, EMERGENCY_CONFIRM_RECORD_DURATION


def play_audio(file_path):
    """
    Plays an audio file using PyAudio.
    """
    chunk = 1024
    wf = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


def record_audio(duration=EMERGENCY_CONFIRM_RECORD_DURATION, output_file="user_response.wav"):
    """
    Records audio from the microphone for a given duration and saves it to output_file.
    Returns the recorded audio data.
    """
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording emergency confirmation...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return b''.join(frames)

# Usage:
# play_audio("audio/prompt_is_it_emergency.wav")
# user_response = record_audio()
