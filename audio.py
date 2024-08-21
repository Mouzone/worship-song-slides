import speech_recognition as sr


def init():
    r = sr.Recognizer()
    r.adjust_for_ambient_noise(sr.Microphone)
    return r


def recordAudio(r):
    # Adjust for ambient noise and record the audio
    audio_data = r.record(sr.Microphone, duration=5)
    return audio_data


def parseAudio(r, audio_data):
    try:
        # Convert speech to text using Google's speech recognition API
        text = r.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "ERROR: Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"ERROR: Could not request results from Google Speech Recognition service; {e}"
