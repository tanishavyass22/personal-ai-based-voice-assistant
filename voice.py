import pyttsx3

def text_to_speech(text, voice_id=None):
    engine = pyttsx3.init()
    
    # Set voice properties
    if voice_id:
        engine.setProperty('voice', voice_id)
    
    # Set other properties (e.g., rate)
    engine.setProperty('rate', 150)  # Adjust the speech rate if needed
    
    # Say the text
    engine.say(text)
    engine.runAndWait()

# Example usage
text_to_speech("good good eveing", voice_id='english+m2')  # Specify voice ID as needed
