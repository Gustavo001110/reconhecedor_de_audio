import speech_recognition as sr

# escrever seu audio
rec = sr.Recognizer()
with sr.AudioFile('audio.wav') as arquivo_audio:
    audio = rec.record(arquivo_audio)
    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)