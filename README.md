# AIR (AI for Radio)
This repository will have all my AI (Artificial intelligence) for SDR Radio.
This project will have all my code for testing some of the AI concepts.<br>
This will include Python code and shell scripts for Python 2.7 and 3.6
#Project Status
All my testing scrips will be here.<br>
# Installing voice recognition.
pip install SpeechRecognition<br>
# Testing voice recognition.
python -m speech_recognition<br>
Sy somthing on Microphone and you should see the resultd on screen.<br>
A moment of silence, please...
Set minimum energy threshold to 62.43497342075616
Say something!
Got it! Now to recognize it...
You said hello
# Testing FM sdr reception of local radio station.
sudo ./test_fm_sdr.sh<br>
This script will test to see if you can listen to a local radio station.<br>
# Testing Voice Regocnition with rtl
test_voice_recognition_with_rtl.sh<br>
This script will tune to a local FM radio stastion and will start decoding the voice of the presenters.<br>
# Generating voice from text to replay to Voice commands over radio.
This script will generatio voice from text to reply to Voice Recognition commands.<br>
# Text to Speach (gTTs)
Installing the gTTs library.<br>
sudo pip install gTTS==1.0.2<br>
# Testing the text to Speach.
Creating a Hello mp3<br>sudo pip install gTTS
gtts-cli.py -t “Hello” -l ‘en’ hello.mp3
gtts-cli 'hello' | play -t mp3 -
# Creating a voice assystint
I am using javis https://github.com/ajminich/Jarvis<br>
Here is an exsample of personal system<br>
sudo python3 ./persanal_asistant.py
