import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()
translator = Translator()

# Get user input for their language and the language they want to translate to
native_lang = input("Select your native language:\n")
target_lang = input("Select the language you want to translate to:\n")

# translate_speech function to translate to target language
def translate_speech(language):
    with sr.Microphone() as source:
        print(f"Speak something in {language}:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=language)
        print(f"You said in {language}: {text}")
        translation = translator.translate(text, dest=target_lang)
        print(f"Translation in {target_lang}: {translation.text}")
        return translation.text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

# Get user input for either one time translate or conversation
while True:
    choice = input("Enter '1' for one-time translation or '2' for conversation mode: ")
    if choice == '1':
        translate_speech(native_lang)
        break
    elif choice == '2':
        while True:
            # User speaks
            user_translation = translate_speech(native_lang)
            if user_translation is None:
                continue
            
            # Other person speaks or skip
            response = input("Press 'q' to quit or any other key to let the other person speak: ")
            if response == 'q':
                break
            
            # Have other person speak and translate to prior chosen native language
            other_translation = translate_speech(target_lang)
            if other_translation is not None:
                print(f"They said in {target_lang}: {other_translation}")
                translation = translator.translate(other_translation, dest=native_lang)
                print(f"Translation in {native_lang}: {translation.text}")
    else:
        print("Invalid input. Please try again.")

# pip install googletrans==4.0.0-rc1
# pip install SpeechRecognition


