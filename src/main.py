import pyttsx3
import pytesseract
from PIL import Image
import time
import keyboard

# Configuration de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialisation de la synthèse vocale
engine = pyttsx3.init()

def lire_texte(texte, vitesse=150):
    """Lit un texte à haute voix."""
    engine.setProperty('rate', vitesse)
    engine.say(texte)
    engine.runAndWait()

def surligner_texte(texte, delai=0.1):
    """Surligne le texte mot par mot."""
    mots = texte.split()
    for i, mot in enumerate(mots):
        texte_surligne = ' '.join(mots[:i] + [f"\033[1;31m{mot}\033[0m"] + mots[i+1:])
        print(texte_surligne, end='\r')
        time.sleep(delai)
    print()

def extraire_texte_image(chemin_image):
    """Extrait le texte d'une image avec OCR."""
    image = Image.open(chemin_image)
    texte = pytesseract.image_to_string(image, lang='fra')  # 'fra' pour le français
    return texte

def main():
    print("Bienvenue dans Reader !")
    print("1. Lire un texte")
    print("2. Extraire du texte d'une image")
    choix = input("Choisissez une option (1 ou 2) : ")

    if choix == '1':
        texte = input("Entrez le texte à lire : ")
        vitesse = int(input("Entrez la vitesse de lecture (100-200) : "))
        print("Appuyez sur 'Espace' pour commencer la lecture...")
        keyboard.wait('space')
        lire_texte(texte, vitesse)
        surligner_texte(texte)
    elif choix == '2':
        chemin_image = input("Entrez le chemin de l'image : ")
        texte = extraire_texte_image(chemin_image)
        print(f"Texte extrait : {texte}")
        lire_texte(texte)
    else:
        print("Option invalide.")

if __name__ == "__main__":
    main()
