import speech_recognition as sr


def recordAudio(r, source):
    r.adjust_for_ambient_noise(source)
    audio_data = r.listen(source, timeout=5, phrase_time_limit=5)
    return audio_data


def parseAudio(r, audio_data):
    try:
        # todo: rewrite to instead of using api, search the song lyrics
        text = r.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "ERROR: Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"ERROR: Could not request results from Google Speech Recognition service; {e}"
