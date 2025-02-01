import unittest
from core.pdf_reader import extraire_texte_pdf

class TestPdfReader(unittest.TestCase):
    def test_extraire_texte_pdf(self):
        texte = extraire_texte_pdf("test.pdf")
        self.assertIsInstance(texte, str)
        self.assertGreater(len(texte), 0)

if __name__ == "__main__":
    unittest.main()
