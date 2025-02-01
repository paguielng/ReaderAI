import sys
import os
import unittest

# Ajouter le répertoire racine du projet à sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from core.pdf_reader import extraire_texte_pdf

class TestPdfReader(unittest.TestCase):
    def test_extraire_texte_pdf(self):
        # Chemin relatif vers un fichier PDF de test dans le dossier 'tests'
        chemin_pdf = os.path.join(os.path.dirname(__file__), "test.pdf")
        
        # Appeler la fonction à tester
        texte = extraire_texte_pdf(chemin_pdf)
        
        # Vérifier que le texte est une chaîne non vide
        self.assertIsInstance(texte, str)
        self.assertGreater(len(texte), 0)

if __name__ == "__main__":
    unittest.main()
