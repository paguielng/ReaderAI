from docx import Document

def extraire_texte_word(chemin_word):
    """Extrait le texte d'un fichier Word."""
    doc = Document(chemin_word)
    texte = ""
    for para in doc.paragraphs:
        texte += para.text + "\n"
    return texte
