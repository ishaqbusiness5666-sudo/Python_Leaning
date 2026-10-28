import os
import queue
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


class PdfToWordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to Word Converter")
        self.root.geometry("520x250")
        self.root.resizable(False, False)

        self.messages = queue.Queue()
        self.is_converting = False
        self.output_folder = None

        self.status_text = tk.StringVar(
            value="Choose a PDF file to create a Word document."
        )
        self.file_text = tk.StringVar(value="No PDF selected")

        content = ttk.Frame(root, padding=20)
        content.pack(fill="both", expand=True)

        ttk.Label(
            content,
            text="Convert a PDF file to Microsoft Word",
            font=("Segoe UI", 14, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            content,
            text="The Word document will be saved next to your PDF.",
        ).pack(anchor="w", pady=(4, 12))

        ttk.Label(content, textvariable=self.file_text, wraplength=470).pack(
            anchor="w", pady=(0, 12)
        )

        buttons = ttk.Frame(content)
        buttons.pack(anchor="w")

        self.select_button = ttk.Button(
            buttons, text="Select PDF", command=self.select_pdf
        )
        self.select_button.pack(side="left")

        self.open_folder_button = ttk.Button(
            buttons,
            text="Open Output Folder",
            command=self.open_output_folder,
            state="disabled",
        )
        self.open_folder_button.pack(side="left", padx=(8, 0))

        self.progress = ttk.Progressbar(
            content, mode="indeterminate", length=475
        )
        self.progress.pack(fill="x", pady=(18, 8))
        ttk.Label(content, textvariable=self.status_text, wraplength=470).pack(
            anchor="w"
        )

        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.after(100, self.check_worker_messages)

    def select_pdf(self):
        pdf_name = filedialog.askopenfilename(
            parent=self.root,
            title="Select a PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )
        if not pdf_name:
            self.status_text.set("No PDF selected. Choose a PDF file to begin.")
            return

        pdf_path = Path(pdf_name)
        if not pdf_path.is_file():
            messagebox.showerror(
                "Invalid file",
                "The selected file could not be found. Please select an existing PDF.",
                parent=self.root,
            )
            self.status_text.set("The selected file is not available.")
            return
        if pdf_path.suffix.lower() != ".pdf":
            messagebox.showerror(
                "Invalid file",
                "Please select a file with the .pdf extension.",
                parent=self.root,
            )
            self.status_text.set("Please select a PDF file.")
            return

        self.file_text.set(str(pdf_path))
        self.open_folder_button.configure(state="disabled")
        self.output_folder = None
        self.start_conversion(pdf_path)

    def start_conversion(self, pdf_path):
        if self.is_converting:
            return

        self.is_converting = True
        self.select_button.configure(state="disabled")
        self.status_text.set("Converting PDF to Word. Please wait...")
        self.progress.start(10)

        worker = threading.Thread(
            target=self.convert_pdf, args=(pdf_path,), daemon=True
        )
        worker.start()

    def convert_pdf(self, pdf_path):
        converter = None
        docx_path = None
        conversion_error = None
        try:
            if not pdf_path.is_file():
                raise FileNotFoundError(
                    "The selected PDF no longer exists. Please select it again."
                )

            try:
                from pdf2docx import Converter
            except ImportError as error:
                raise RuntimeError(
                    "The pdf2docx package is not installed. Install it from "
                    "Command Prompt with: py -m pip install pdf2docx"
                ) from error

            docx_path = pdf_path.with_suffix(".docx")
            converter = Converter(str(pdf_path))
            converter.convert(str(docx_path))

            if not docx_path.is_file() or docx_path.stat().st_size == 0:
                raise RuntimeError(
                    "Conversion finished without creating a valid Word document."
                )
        except Exception as error:
            conversion_error = error
        finally:
            if converter is not None:
                try:
                    converter.close()
                except Exception as error:
                    if conversion_error is None:
                        conversion_error = error

        if conversion_error is not None:
            self.messages.put(("error", str(conversion_error)))
        elif docx_path is not None:
            self.messages.put(("success", str(docx_path)))
        else:
            self.messages.put(
                ("error", "Conversion ended without producing a Word document.")
            )

    def check_worker_messages(self):
        try:
            while True:
                message_type, details = self.messages.get_nowait()
                if message_type == "success":
                    self.is_converting = False
                    self.progress.stop()
                    self.select_button.configure(state="normal")
                    self.output_folder = str(Path(details).parent)
                    self.open_folder_button.configure(state="normal")
                    self.status_text.set("Conversion complete.")
                    messagebox.showinfo(
                        "Conversion complete",
                        f"Your Word document was saved here:\n\n{details}",
                        parent=self.root,
                    )
                elif message_type == "error":
                    self.is_converting = False
                    self.progress.stop()
                    self.select_button.configure(state="normal")
                    self.status_text.set("Conversion failed.")
                    messagebox.showerror(
                        "Conversion error", details, parent=self.root
                    )
        except queue.Empty:
            pass

        self.root.after(100, self.check_worker_messages)

    def open_output_folder(self):
        if not self.output_folder or not os.path.isdir(self.output_folder):
            messagebox.showerror(
                "Folder unavailable",
                "The output folder could not be found.",
                parent=self.root,
            )
            self.open_folder_button.configure(state="disabled")
            return

        try:
            os.startfile(self.output_folder)
        except OSError as error:
            messagebox.showerror(
                "Could not open folder",
                f"Windows could not open the output folder:\n\n{error}",
                parent=self.root,
            )

    def close_window(self):
        if self.is_converting:
            messagebox.showwarning(
                "Conversion in progress",
                "Please wait for the conversion to finish before closing the app.",
                parent=self.root,
            )
            return
        self.root.destroy()


def main():
    root = tk.Tk()
    PdfToWordApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
