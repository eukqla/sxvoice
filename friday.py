import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import socket

r=sr.Recognizer()


response = ''


def konusma(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice = ''
        try:
            voice=r.recognize_google(audio,language=('tr'))
        except sr.UnknownValueError:
            speak('\n Dediğinizi Anlayamadım Lütfen 2 Saniye Sonra Tekrardan Söyleyin')
        except sr.RequestError:
            speak('\n Yazılımda Hatalar Çıktı')
        return voice

def response(voice):
    if 'nasılsın wiks' in voice:
        speak('İyiyim Sen nasılsın')

    if 'tarayıcıyı aç' in voice:
        speak('Tarayıcıyı Açıyorum')
        url = 'https://www.google.com'
        webbrowser.get().open(url)
        speak('Senin İçin Tarayıcıyı açtım patron')

    if 'adın ne' in voice:
        speak('İsmim wiks')

    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))

    if 'arama yap' in voice:
        search = konusma('Ne aramak istiyorsun')
        url = 'https://www.google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + 'için bulduklarım')
        

    if 'kapat' in voice:
        speak('Görüşürüz')
        time.sleep(0.5)
        exit()
        
    if ('internet kontrol' in voice):
        IPaddress = socket.gethostbyname(socket.gethostname())
        if IPaddress == "127.0.0.1":
            speak("İnternet kontrol edildi Bağlı Değilsiniz " + IPaddress)
        else:
            speak("İnternet kontrol edildi IP Adresini söylüyorum " + IPaddress)
            print("İsterseniz buradan da bakabilirsiniz = " + IPaddress)


def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Merhaba Kemal Nasıl Yardımcı Olabilirim')
time.sleep(1)
while 1:
    voice = konusma()
    #print(voice,'Dedin')                
    response(voice)
