# AIR (AI for Radio)
This repository will have all my AI (Artificial intelligence) for SDR Radio.
This project will have all my code for testing some of the AI concepts.<br>
This will include Python code and shell scripts for Python 2.7 and 3.6
#Project Status
All my testing scrips will be here.<br>
# Installing voice recognition.
sudo apt-get install rtl-sdr<br>
sudo apt-get install librtl-dev<br>
sudo apt-get install rtl-sdr<br>
sudo -H pip install SpeechRecognition<br>
sudo -H pip3 install speech_recognition<br>
python -m pip install pyaudio<br>
sudo -H pip install pyrtlsdr<br>
sudo -H pip3 install pyrtlsdr<br>
sudo -H pip3 install scipy<br>
sudo -H pip install scipy<br>
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
sudo pip install gTTS<br>
# Testing the text to Speach.
Text to speech without internet connection (using pyttsx3)<br>
Text to speech having internet connection (using gTTS)<br>

Creating a Hello mp3<br>sudo pip install gTTS<br>
gtts-cli.py -t “Hello” -l en hopen websiteello.mp3<br>
gtts-cli 'hello' | play -t mp3 -<br>
Testing creating mp3 python3<br>
python3 ./creating_hello_mp3.py
# Creating a voice assystint
sudo apt-get install -qq python python-dev python-pip build-essential swig libpulse-dev
sudo pip install pocketsphinx
sudo apt-get install mpg321
Reqierd libraries<br>
prerequ
certifi==2017.11.5
chardet==3.0.4
gTTS==1.2.2
gTTS-token==1.1.1
idna==2.6
mpg123==0.4
PyAudio==0.2.11
pytz==2017.3
requests==2.18.4
SpeechRecognition==3.8.1
urllib3==1.22
beautifulsoup4==4.6.0
weather-api==0.0.4
Here is an exsample of personal system<br>
sudo python3 ./persanal_asistant.py<br>
Comands that can be used<br>
1) open reddit<br>
2) open website<br>
3) what\'s up<br>
4) joke
5) current weather in .....
6) weather forecast in ....
7) email ....
8)
# Creating Google api keys
1. Sign Up for a Free Tier Account

Google Cloud offers a Free Tier plan, which will be used in this tutorial. An account is required to get an API key.
2. Generate an API Key

Follow these steps to generate an API key:

    Sign-in to Google Cloud Console https://console.cloud.google.com
    Click “API Manager”
    Click “Credentials”
    Click “Create Credentials”
    Select “Service Account Key”
    Under “Service Account” select “New service account”
    Name service (whatever you’d like)
    Select Role: “Project” -> “Owner”
    Leave “JSON” option selected
    Click “Create”
    Save generated API key file
    Rename file to api-key.json
