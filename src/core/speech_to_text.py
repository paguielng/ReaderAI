import speech_recognition as sr

def ecouter_et_transcrire():
    """Écoute l'utilisateur et transcrit la parole en texte."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        audio = recognizer.listen(source)

        try:
            texte = recognizer.recognize_google(audio, language="fr-FR")
            print(f"Vous avez dit : {texte}")
            return texte
        except sr.UnknownValueError:
            print("Désolé, je n'ai pas compris.")
            return ""
        except sr.RequestError:
            print("Erreur de connexion au service de reconnaissance vocale.")
            return ""
