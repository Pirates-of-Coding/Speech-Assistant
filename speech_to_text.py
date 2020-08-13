import speech_recognition as sr
r = sr.Recognizer()                                         # initialising the Recognizer
with sr.Microphone() as source:                             # using mic for receiving the audio
        print("Listening...")
        sr.energy_threshold = 100                           # minimum energy for recording
        sr.pause_threshold = 2                              # seconds of pause before a phrase is considered complete
        r.adjust_for_ambient_noise(source, duration=0.2)    # for noise adjustment
        audio = r.listen(source)                            # listening to user's input

try:                   
    
        print("Recognizing...")
        query = r.recognize_google(audio)                   # using google to recognize the voice
        print(query)   
except :                                                    # for handeling exceptions
        print("Say that again please...")
     
