from PyPDF2 import PdfReader

def extraire_texte_pdf(chemin_pdf):
    """Extrait le texte d'un fichier PDF."""
    reader = PdfReader(chemin_pdf)
    texte = ""
    for page in reader.pages:
        texte += page.extract_text()
    return texte
