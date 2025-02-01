def sauvegarder_texte(texte, chemin_fichier):
    """Sauvegarde le texte dans un fichier."""
    with open(chemin_fichier, "w", encoding="utf-8") as f:
        f.write(texte)
