#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from pdf_operations import split_pdf, copy_to_folders

def main():
    root = tk.Tk()

    # Create a drop-down list of payslips
    input_pdf = filedialog.askopenfilename(title="Select Payroll PDF", filetypes=[("PDF Files", "*.pdf")])
    payslips = split_pdf(input_pdf)

    payslip_var = tk.StringVar(root)
    payslip_var.set(payslips[0])
    dropdown = tk.OptionMenu(root, payslip_var, *payslips)
    dropdown.pack()

    # Listbox to show selected folders
    folders_listbox = tk.Listbox(root)
    folders_listbox.pack()

    # Button to add folders
    button_add = tk.Button(root, text="Add Folder", command=lambda: copy_to_folders(payslip_var.get(), folders_listbox))
    button_add.pack()

    # Button to perform the copy action
    button_copy = tk.Button(root, text="Copy to Selected Folders", command=lambda: [copy(payslip_var.get(), folder) for folder in folders_listbox.get(0, tk.END)])
    button_copy.pack()


    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    root.mainloop()

if __name__ == "__main__":
    main()
