import speech_recognition as sr
from time import sleep

def tratar_audio(rec, audio):
    global acabou
    try:
        texto = rec.recognize_google(audio, language='pt-BR')
        print(texto)
        if 'cala a boca' in texto:
            acabou = True
    except:
        print('\033[1;33mnão ouvi direito. tente novamete\033[m')

acabou = False
# usando comando por voz
rec = sr.Recognizer()
with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    rec.pause_threshold = 0.5
    print('\033[1;32mfala alguma coisa\033[m')

parar_de_ouvir = rec.listen_in_background(microfone, tratar_audio)
while True:
    sleep(0.1)
    if acabou == True:
        break
parar_de_ouvir(wait_for_stop=False)