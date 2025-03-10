# state_machine.py
import time
from config import HELP_DETECTION_THRESHOLD_CHUNKS, STATE_IDLE, STATE_T0


class StateMachine:
    def __init__(self):
        self.state = STATE_IDLE
        self.first_help_time = None
        self.accumulated_audio = []  # store audio chunks for verification (T1/T3)
        self.chunk_count = 0  # count chunks since first help detection

    def reset(self):
        self.state = STATE_IDLE
        self.first_help_time = None
        self.accumulated_audio = []
        self.chunk_count = 0
        print("StateMachine reset to INITIAL")

    def process_audio_chunk(self, is_help, audio_chunk):
        """
        Process an incoming audio chunk classification result.
        """
        if self.state == STATE_IDLE:
            if is_help:
                self.state = "T0"
                self.first_help_time = time.time()
                self.accumulated_audio.append(audio_chunk)
                self.chunk_count = 1
                print("Transition to T0: first help detected")
        elif self.state == "T0":
            self.chunk_count += 1
            self.accumulated_audio.append(audio_chunk)
            if is_help:
                if self.chunk_count <= HELP_DETECTION_THRESHOLD_CHUNKS:
                    self.state = "T1"
                    print("Transition to T1: second help detected within threshold")
                else:
                    print("Second help detected but outside threshold; remain in T0")
            else:
                if self.chunk_count > HELP_DETECTION_THRESHOLD_CHUNKS:
                    print("Threshold exceeded without second help; resetting state")
                    self.reset()

    def get_accumulated_audio(self):
        # Combine accumulated audio chunks into one long audio segment
        return b''.join(self.accumulated_audio)

    def clear_accumulated_audio(self):
        self.accumulated_audio = []
        self.chunk_count = 0

# Usage:
# state_machine = StateMachine()
# state_machine.process_audio_chunk(is_help, audio_chunk)
