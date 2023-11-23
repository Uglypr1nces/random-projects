#speechrecognition
import speech_recognition as sr
from gtts import gTTS
import os

def listen_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't understand."
    except sr.RequestError:
        return "Sorry, I couldn't connect to the speech recognition service."

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('response.mp3')
    os.system('mpg321 response.mp3')  # You'll need mpg321 or another player installed

while True:
    command = listen_microphone()
    print("You said:", command)

    response = "You said: " + command  # Modify this to generate appropriate responses

    print("Response:", response)
    speak(response)
