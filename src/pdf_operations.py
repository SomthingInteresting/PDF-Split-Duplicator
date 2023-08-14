import PyPDF2
import json
import os
import tkinter as tk
from shutil import copy2
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

def copy_file_to_destinations(payslip, folders_listbox):
    folder = filedialog.askdirectory(title="Select Folder")
    if folder:
        folders_listbox.insert(tk.END, folder)

FOLDER_GROUPS_FILE = "folder_groups.json"

def save_folder_group(group_name, folders):
    data = {}
    if os.path.exists(FOLDER_GROUPS_FILE):
        with open(FOLDER_GROUPS_FILE, "r") as f:
            data = json.load(f)
    data[group_name] = folders
    with open(FOLDER_GROUPS_FILE, "w") as f:
        json.dump(data, f)

def load_folder_groups():
    if os.path.exists(FOLDER_GROUPS_FILE):
        with open(FOLDER_GROUPS_FILE, "r") as f:
            data = json.load(f)
        return list(data.keys())
    return []

def load_selected_group(group_name):
    if os.path.exists(FOLDER_GROUPS_FILE):
        with open(FOLDER_GROUPS_FILE, "r") as f:
            data = json.load(f)
        return data.get(group_name, [])
    return []
