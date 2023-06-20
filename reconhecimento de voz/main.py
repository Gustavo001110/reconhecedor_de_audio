import speech_recognition as sr

# capturar sua voz
rec = sr.Recognizer()
with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('\033[1;32mfale alguma coisa\033[m')
    rec.pause_threshold = 1
    audio = rec.listen(microfone)
    try:
        texto = rec.recognize_google(audio, language='pt-BR')
        print(texto)
    except:
        print('\033[1;33mnão ouvi direito. tente novamente\033[m')