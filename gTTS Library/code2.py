from gtts import gTTS
tts = gTTS('hello', lang='en', tld='com.au')
tts.save('hello.mp3')