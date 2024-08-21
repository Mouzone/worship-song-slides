import audio
import time


def driver(r):
    print("-Listening...")
    audio_data = audio.recordAudio(r)
    print("-Parsing...")
    output = audio.parseAudio(r, audio_data)
    print(output)


def main():
    r = audio.init()
    print("Running")

    while True:
        driver(r)
        time.sleep(20)


main()
