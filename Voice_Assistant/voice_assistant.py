import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def process_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I don't understand that.")
    
    return True

def main():
    speak("Hello! I am your assistant. How can I help you?")
    while True:
        command = listen()
        if not process_command(command):
            break

main()
