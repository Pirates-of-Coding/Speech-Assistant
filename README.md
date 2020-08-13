# Speech-Assistant
A voice based Assistant module written in Python using Pyttsx3.

Speech recognition system basically translates spoken languages into text.


## Requirements :-

To use all of the functionality of the library, you should have:
    - Python 2.6, 2.7, or 3.3+ (required)
    - PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
    - PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
    - Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
    - The first software requirement is Python 2.6, 2.7, or Python 3.3+.
    - PyAudio is required if and only if you want to use microphone input .
    - If not installed(PyAudio), everything in the library will still work, except attempting to instantiate a Microphone object will raise an AttributeError.

## Installing

The easiest way to install this is using  
- pip install SpeechRecognition.

How does Speech recognition work?
![Pyttsx3](pyttsx3.png)

**Pyttsx3 Module**

Pyttsx3  is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

**Installation**

- pip install pyttsx3

It supports three TTS engines :
    - sapi5 – SAPI5 on Windows
It is very simple to use, is very friendly and is free to use...
