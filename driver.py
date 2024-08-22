import speech_recognition as sr
import audio
import time


def driver(r, source):
    print("-Listening...")
    audio_data = audio.recordAudio(r, source)
    print("-Parsing...")
    output = audio.parseAudio(r, audio_data)
    print(output)


def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Running")

        while True:
            driver(r, source)
            print("Waiting")
            time.sleep(20)


main()
