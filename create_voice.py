import os       #will be on the top
import subprocess
from gtts import gTTS
os.chdir(r'/home/anton/Downloads/AIR/')
audio_file = "hello.mp3"
tts = gTTS(text="Hello World!", lang="en")
tts.save(audio_file)
#return_code = subprocess.call(["afplay", audio_file])
os.system('mpg321 hello.mp3 -quiet')
