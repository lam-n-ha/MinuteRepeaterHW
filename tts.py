from gtts import gTTS
import os

mytext = 'The time at D A D is 12:21'
language = 'en'

myobj = gTTS(text = mytext, lang = language, slow = False)

myobj.save("info.mp3")


os.system("mpg321 info.mp3")

