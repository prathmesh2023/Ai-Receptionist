from gtts import gTTS
from playsound import playsound
text='माझा नाव सीताबाई मला इन्फॉर्मशन टेकनॉलॉजि च्या पोरांनी बनवलाय '
text2='I am Your Virtual receptionist Created By Kedar, Aniket and Prathmesh As An Final Year Project'

tts = gTTS(text,lang='mr',tld='co.in')

tts.save('play.mp3')

playsound('play.mp3')