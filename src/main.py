#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_operations import split_pdf, copy_file_to_destinations

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
    button_add = tk.Button(root, text="Add Folder", command=lambda: add_folder_to_list(payslip_var.get(), folders_listbox))
    button_add.pack()

    # Button to remove folders
    def remove_selected_folder():
        selected = folders_listbox.curselection()  # Gets the index of the selected item
        if selected:
            folders_listbox.delete(selected)

    button_remove = tk.Button(root, text="Remove Folder", command=remove_selected_folder)
    button_remove.pack()

    # Button to perform the copy action
    button_copy = tk.Button(root, text="Copy to Selected Folders", command=lambda: copy_files_and_notify(payslip_var.get(), folders_listbox.get(0, tk.END)))
    button_copy.pack()

    def copy_files_and_notify(payslip, folders):
        success = copy_file_to_destinations(payslip, folders)
        if success:
            messagebox.showinfo("Success", "Files have been successfully copied!")
        else:
            messagebox.showerror("Error", "An error occurred while copying files.")

    def add_folder_to_list(payslip, folders_listbox):
        folder = filedialog.askdirectory(title="Select Folder")
        if folder:
            folders_listbox.insert(tk.END, folder)

    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()

if __name__ == "__main__":
    main()
