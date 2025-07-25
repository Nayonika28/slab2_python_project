import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("🎤 Speak something...")

    # Listen to audio
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google API
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand your voice.")
    except sr.RequestError:
        print("❌ Could not request results, check your internet connection.")
