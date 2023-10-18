import speech_recognition as sr
import pyaudio
def nghe0():
    r = sr.Recognizer()
    with sr.Microphone() as source:   
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio,language="vi-VI")
        print("Bạn: {}".format(text))
    except:
        text = "......"
        print("Bạn: {}".format(text))
    return text