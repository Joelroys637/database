import pyttsx3

def speech(speech_text):
    
    eng=pyttsx3.init()
    eng.say(speech_text)
    eng.runAndWait()
