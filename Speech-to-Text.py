import speech_recognition as s

# Create an object of Recognizer
sr = s.Recognizer()

print("I am your script and listening to you...")

# Continuously listen for input
while True:
    with s.Microphone() as m:
        try:
            # Listen to the audio without timeout and phrase_time_limit
            audio = sr.listen(m)  # No time limit now
            query = sr.recognize_google(audio, language='en-IN')
            print(query)

        except Exception as e:
            print("Sorry, I couldn't understand that. Please try again.")
