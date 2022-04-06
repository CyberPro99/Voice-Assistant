from multiprocessing.connection import wait
import os
from time import ctime, time # for time
import webbrowser # for search
import time
import playsound  
from gtts import gTTS
import random
from pyparsing import null_debug_action
import speech_recognition as sr
import requests

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r =  sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        audio = r.listen(source) # listen to our microphoe as souce
        if ask:
              sarey_speak(ask)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            # sarey_speak(voice_data)
        except sr.UnknownValueError:
            print(".......")
        except sr.RequestError:
            sarey_speak('my speech service is down')
        return voice_data

def sarey_speak(audio_string):
    tts = gTTS(text= audio_string, lang='en',slow=False,lang_check=True)
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
sarey_speak("Hi and welecome i am  arietta your your voice assistant")

def respond(voice_data):
    if there_exists(["hi","ola","what's"]):
        greetings = [f"hey, how can I help you {person_obj.name}",f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        sarey_speak(greet)

    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            sarey_speak("my name is Alexis")
        else:
            sarey_speak("my name is Alexis. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        sarey_speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object
 
    if there_exists(["time now","time","what is time now"]):
        sarey_speak(ctime())

    if there_exists(["search for me","search now","can you search for me"]):
        sarey_speak('what do you want to search for')
        search  = record_audio('Loding....')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        sarey_speak('Here is what I found for ' + search)

    if there_exists(["google map","map ","Earth"]):
        sarey_speak('what do you want to search for')
        location = record_audio('Loding....')
        url = 'https://google.com/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        sarey_speak('Here is your location ' + location)

    if there_exists(["thank you","i love you","you are the best","thanks"]):
        sarey_speak('thanks for all your love i love you too')

    # Current city or region
    if there_exists(["where am i","find me","what is my location","location of me"]):
        Ip_info = requests.get('http://ipinfo.io/json').json()
        loc = Ip_info["region"]
        sarey_speak(f"You must be somewhere in {loc}")    

    if there_exists(["goodby","good Night","salam","see you"]):
       sarey_speak('Goodbye my dear, I wish you a good night, do not forget me 😭🖐️')
       exit()

time.sleep(1)
person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond
