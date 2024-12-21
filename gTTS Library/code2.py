from gtts import gTTS
tts = gTTS('hello world!', lang='en', tld='com.au')
tts.save('hello_aus.mp3')