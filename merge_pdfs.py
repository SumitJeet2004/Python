from PyPDF2 import PdfWriter, PdfReader
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    with open(pdf, "rb") as f:
        reader = PdfReader(f)
        merger.append(reader)

with open("merged-pdf.pdf", "wb") as f_out:
    merger.write(f_out)