import speech_recognition as sr

# salvar seu audio em um arquivo
rec = sr.Recognizer()
with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('\033[1;32mfale alguma coisa\033[m')
    audio = rec.listen(microfone)
with open('audio.wav', 'wb') as arquivo:
    arquivo.write(audio.get_wav_data())
print('\033[1;32maudio salvo\033[m')