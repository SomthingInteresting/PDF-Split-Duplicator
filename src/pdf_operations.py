import PyPDF2
from shutil import copy
from tkinter import filedialog

def split_pdf(input_pdf):
    with open(input_pdf, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        payslips = []

        for i in range(num_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])

            output_pdf = f"payslip_{i}.pdf"  
            with open(output_pdf, "wb") as output_file:
                writer.write(output_file)

            payslips.append(output_pdf)

    return payslips

def copy_to_folders(payslip, folders_listbox):
    folder = filedialog.askdirectory(title="Select Folder")
    if folder:
        folders_listbox.insert(tk.END, folder)
