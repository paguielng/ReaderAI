# Reader-v 0.1

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
```
---



