<img src="https://github.com/paguielng/Reader/blob/main/logo/Reader1.0-1%20cover_1.jpg" alt="Image 3"/>

---

# <img src="https://github.com/paguielng/Reader/blob/main/logo/Reader1.0-1.jpg" width="8%" alt="Image 2"/> Reader v1.0.0

**Reader** est un outil pour suivre la lecture en surlignant le texte et en lisant à haute voix. Il inclut des fonctionnalités de reconnaissance vocale et d'extraction de texte à partir d'images (OCR). Parfait pour améliorer la concentration et l'accessibilité.

---

## Fonctionnalités

- **Surbrillance linéaire** : Suivez votre lecture avec une surbrillance mot par mot.
- **Lecture vocale** : Écoutez le texte dans plusieurs langues.
- **Reconnaissance vocale** : Dictez et le programme transcrit pour vous.
- **OCR** : Extrayez du texte à partir d'images ou de photos.
  
### Prérequis
- Python 3.8 ou supérieur.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installé sur votre système.

### Étapes
1. Clonez ce dépôt :
```bash
   git clone https://github.com/paguielng/Reader.git
   cd Reader
   pip install -r requirements.txt
   python src/main.py
```
```plaintext
Reader/
├── .github/                # Configuration CI/CD
├── docs/                   # Documentation supplémentaire
├── src/                    # Code source principal
│   ├── core/               # Fonctionnalités principales
│   ├── utils/              # Utilitaires et fonctions helper
│   ├── tests/              # Tests unitaires et d'intégration
│   └── main.py             # Point d'entrée du programme
├── logo/                   # Logos et fichiers design des versions
```
---

# Documentation

1. **[Documentation Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** : **`Tesseract OCR`** un moteur de reconnaissance optique de caractères (OCR) open-source.

2. **[API Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text)** : **`API de Google Cloud`** permettant de convertir la parole en texte en temps réel.

3. **[API Microsoft Azure Speech](https://azure.microsoft.com/services/cognitive-services/speech-services/)** : **`API de Microsoft Azure`** pour la reconnaissance vocale, la synthèse de la parole et la traduction vocale.

4. **[Docu. pyttsx3](https://pyttsx3.readthedocs.io)** : **`pyttsx3`** une bibliothèque Python pour la conversion du texte en parole (TTS) qui fonctionne de manière offline.

---
<img src="https://github.com/paguielng/Reader/blob/main/logo/Reader1.0-2%20analog-cover_2.jpg" alt="Image 3"/>
