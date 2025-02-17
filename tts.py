import pyttsx3

def talking_tom_speak(text="Hello, I am Talking Tom!"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed
    engine.setProperty('pitch', 150) # Adjust pitch
    engine.say(text)
    engine.runAndWait()
