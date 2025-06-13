import speech_recognition as sr
from googletrans import Translator
from playsound import playsound

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language='en')
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Error: Could not request results; {0}".format(e))
        return ""

def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ta')
    return translated_text.text

def text_to_speech(text, lang='ta'):
    translator = Translator()
    translated_audio = translator.translate(text, src='en', dest=lang)
    translated_text = translated_audio.text
    translator.save_to_file(translated_text, 'translated_audio.mp3')
    playsound('translated_audio.mp3')

if __name__ == "__main__":
    while True:
        # Recognize speech
        english_text = recognize_speech()
        
        if english_text:
            print("English:", english_text)
            
            # Translate text to Tamil
            tamil_text = translate_text(english_text)
            print("Tamil:", tamil_text)
            
            # Convert text to speech
            text_to_speech(tamil_text)
