# audio_listener.py
import pyaudio

import config


class AudioListener:
    def __init__(self):
        self.rate = config.STREAM_RATE
        self.chunk_size = config.STREAM_CHUNK_SIZE
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=config.STREAM_CHANNELS,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk_size)

    def listen_chunk(self, duration=AUDIO_CHUNK_DURATION):
        frames = []
        num_frames = int(self.rate / self.chunk_size * duration)
        for _ in range(num_frames):
            data = self.stream.read(self.chunk_size)
            frames.append(data)
        audio_data = b''.join(frames)
        return audio_data

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

# Usage:
# listener = AudioListener()
# audio_chunk = listener.listen_chunk()
