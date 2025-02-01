from PIL import Image, ImageEnhance, ImageFilter

def pretraiter_image(chemin_image):
    """Prétraite une image pour améliorer la précision de l'OCR."""
    image = Image.open(chemin_image)

    # Convertir en niveaux de gris
    image = image.convert("L")

    # Améliorer le contraste
    enhance = ImageEnhance.Contrast(image)
    image = enhance.enhance(2.0)

    # Réduire le bruit
    image = image.filter(ImageFilter.SMOOTH)

    return image
