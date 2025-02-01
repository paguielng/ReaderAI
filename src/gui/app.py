import tkinter as tk
from tkinter import filedialog, messagebox
from core.speech_to_text import ecouter_et_transcrire
from core.pdf_reader import extraire_texte_pdf

class ReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reader")
        self.root.geometry("400x300")

        # Boutons
        self.btn_ecouter = tk.Button(root, text="Dictée", command=self.dicter)
        self.btn_ecouter.pack(pady=10)

        self.btn_pdf = tk.Button(root, text="Ouvrir PDF", command=self.ouvrir_pdf)
        self.btn_pdf.pack(pady=10)

        self.btn_quitter = tk.Button(root, text="Quitter", command=root.quit)
        self.btn_quitter.pack(pady=10)

        # Zone de texte
        self.text_area = tk.Text(root, wrap="word")
        self.text_area.pack(fill="both", expand=True)

    def dicter(self):
        """Transcrit la parole en texte et l'affiche."""
        texte = ecouter_et_transcrire()
        if texte:
            self.text_area.insert("end", texte + "\n")

    def ouvrir_pdf(self):
        """Ouvre un fichier PDF et affiche son contenu."""
        fichier = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
        if fichier:
            texte = extraire_texte_pdf(fichier)
            self.text_area.insert("end", texte + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReaderApp(root)
    root.mainloop()
