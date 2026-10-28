from pdf2docx import Converter
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_pdf_to_word():
    # Open a window to select the PDF
    root = tk.Tk()
    root.withdraw()

    pdf_path = filedialog.askopenfilename(
        title="Select your PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_path:
        return

    # Save Word file in the same folder as the PDF
    folder = os.path.dirname(pdf_path)
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    word_path = os.path.join(folder, filename + ".docx")

    try:
        converter = Converter(pdf_path)
        try:
            converter.convert(word_path)
        finally:
            converter.close()

        messagebox.showinfo(
            "Success",
            f"PDF converted successfully!\n\nWord file saved at:\n{word_path}"
        )

    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

    finally:
        root.destroy()

if __name__ == "__main__":
    convert_pdf_to_word()
