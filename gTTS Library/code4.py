from gtts import gTTS
en = gTTS('hello world!', lang='en')
fr = gTTS('bonjour!', lang='fr')

with open('hello_bonjour.mp3', 'wb') as f:
    en.write_to_fp(f)
    fr.write_to_fp(f)