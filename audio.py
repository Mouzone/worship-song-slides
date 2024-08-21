import speech_recognition as sr

r = sr.Recognizer()
# rewrite to record with start and stop
# while started, record for 5 second increments and parse
with sr.Microphone() as source:
    print("Listening...")
    # Adjust for ambient noise and record the audio
    r.adjust_for_ambient_noise(source)
    audio_data = r.record(source, duration=5)

    print("Recognizing...")
    try:
        # Convert speech to text using Google's speech recognition API
        text = r.recognize_google(audio_data)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")