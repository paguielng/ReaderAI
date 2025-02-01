from core.pdf_reader import extraire_texte_pdf

texte_pdf = extraire_texte_pdf("exemple.pdf")
print(f"Texte extrait du PDF : {texte_pdf}")
