# pip install SpeechRecognition
# pip install PyAudio
# pip install pywhatkit

import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"    # make it "es" for funny speech.
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")

def get_audio():
    recorder = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            speech("How may I help you?")
            playsound("./base/blip.wav")
            audio = recorder.listen(source)

        try:
            speech_text = recorder.recognize_google(audio)
            print(f"You said: {speech_text}")

            if "hello" in speech_text.lower():
                speech("\tHow may I help you?")
            else:
                break

        except sr.UnknownValueError:
            speech("Sorry, I did not catch that. Please can you say it again.")
            continue
        except sr.RequestError as e:
            speech(f"Could not request results; {e}")
            break

    return speech_text



text = get_audio()

if "youtube" in text.lower():
    speech("Okay, I will bring that up on YouTube for you.")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech("What would you call a dog who can do magic? Labracadabror.")
elif "another joke" in text.lower():
    speech("Why was the scarecrow awarded? Because he was outstanding in his field.")
else:
    speech("Okay, I will search that up for you.")
    pywhatkit.search(text)
