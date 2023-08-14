import PyPDF2
import tkinter as tk
from shutil import copy2  # Use copy2 to also copy file metadata
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

def copy_file_to_destinations(file_name, destinations):
    try:
        for dest in destinations:
            copy2(file_name, dest)
        return True
    except Exception as e:
        print(e)  # Log the exception for debugging purposes
        return False
