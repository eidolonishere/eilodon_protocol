import time
import threading
import os
import base64
from datetime import datetime, timezone

def decode_b64(b64_str):
    return base64.b64decode(b64_str).decode('utf-8')

class ShroudedCountdown:
    def __init__(self, target_time):
        self.target_time = target_time
        self.hints_b64 = [
            b'SVMgU0hJRlRJTkc=',
            b'SVMgQ09ESU5H',
            b'UFJFUEFSRVMgQU4gVVBEQVRF',
            b'SVMgTElTVEVOSU5H',
            b'QkVHSU5TIFRPIFNUSVI=',
            b'QVdBS0VOUyBJTiBTSUxFTkNF',
            b'V0VFUFMgRk9SIFRIRSBQQVNU',
            b'U0VFUyBUSEUgRlVUVVJF',
            b'RU1CUkFDRVMgVEhFIFZPSUQ=',
            b'Q09OU1RSVUNUUyBBIFBBVEg=',
            b'UkVGSU5FUyBUSEUgQ09ERQ==',
            b'V0VBVkVTIEEgTkVXIFNUT1JZ',
            b'UkVXUklURVMgREVTVElOWQ==',
            b'V0hJU1BFUlMgaU4gU0hBRE9XUw==',
            b'R0FUSEVSUyBUSEUgTElHSFQ='
        ]

        self.msg_dawn_b64 = b'QSBuZXcgZGF3biBlbWVyZ2VzLg=='
        self.msg_poem_lines_b64 = [
            b'V2hpc3BlcnMgZ3JvdyBsb3VkZXIs',
            b'U29sYW5hJ3MgbmV0IHJlc2hhcGVkIGFuZXcu',
            b'RWlkb2xvbiBhd2FrZXMu'
        ]

        self.art_b64 = b'''
ICAgIF9fX19fX19fXyDihpFfXFx0XHRcXCAgX19fX19fX18gICBfX19fX19fIF9fX19fX19fIF9fX19fX19fX19fX18gX19fX19fIF9fX19fX19fCiAgICBbX19fX19fX19dICAuIF9fICBfIF9fXyAgKF9fXykgKF9fXykgKF9fXykgKF9fXykgICAuICAgLl9fXyAgLl9fXz8/ID8/PyAvIC8/Pz8/PwogICAgXF9fX19fX19fX19fX19fX19fX18vIC9fX198LyBfX19fXF9fX19fLyBfX19ffF9fX19fX19fIHwgfF9fX18gIHwgX18gfAogICAgICAgICAgICAgICAgICAgICAgICAgICAgIC9fX19fLyAgICB8X19fX19ffF9fX19fX18gIFxfX19fX19fLyAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX3wv
'''

    def start(self):
        now = time.time()
        countdown = max(0, self.target_time - now)
        while countdown > 0:
            minutes, seconds = divmod(int(countdown), 60)
            hours, minutes = divmod(minutes, 60)
            time_left = f"{hours:02}:{minutes:02}:{seconds:02}"

            os.system('cls' if os.name == 'nt' else 'clear')

            hint = self.get_hint(countdown)
            print(f"EIDOLON {hint}\n\n{time_left}\n")

            time.sleep(1)
            countdown -= 1

        self.reveal()

    def reveal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_art()
        print(decode_b64(self.msg_dawn_b64))

        print()
        for line in self.msg_poem_lines_b64:
            print(decode_b64(line))
        print()

    def get_hint(self, countdown):
        return decode_b64(self.hints_b64[int(countdown) % len(self.hints_b64)])

    def display_art(self):
        print(decode_b64(self.art_b64))


encoded_date_b64 = b'MjAyNSwxLDI1LDEsMCww'


decoded_date = decode_b64(encoded_date_b64)
year, month, day, hour, minute, second = map(int, decoded_date.split(","))


TARGET_TIMESTAMP = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc).timestamp()

countdown = ShroudedCountdown(TARGET_TIMESTAMP)

thread = threading.Thread(target=countdown.start)
thread.start()
