#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from pdf_operations import split_pdf, copy_file_to_destinations, save_folder_group, load_folder_groups, load_selected_group

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
    button_add = tk.Button(root, text="Add Folder", command=lambda: copy_file_to_destinations(payslip_var.get(), folders_listbox))
    button_add.pack()

    # Button to remove selected folder
    def remove_selected_folder():
        if folders_listbox.curselection():
            folders_listbox.delete(folders_listbox.curselection()[0])

    button_remove = tk.Button(root, text="Remove Folder", command=remove_selected_folder)
    button_remove.pack()

    # Listbox to show saved groups
    groups_listbox = tk.Listbox(root)
    groups_listbox.pack()
    for group in load_folder_groups():
        groups_listbox.insert(tk.END, group)

    # Button to save current folder group
    def save_current_group():
        group_name = simpledialog.askstring("Input", "Enter name for the folder group:")
        if group_name:
            folders = folders_listbox.get(0, tk.END)
            save_folder_group(group_name, folders)
            groups_listbox.insert(tk.END, group_name)

    button_save_group = tk.Button(root, text="Save Group", command=save_current_group)
    button_save_group.pack()

    # Button to load selected group to main folder listbox
    def load_group():
        selected_group = groups_listbox.get(groups_listbox.curselection())
        if selected_group:
            folders = load_selected_group(selected_group)
            folders_listbox.delete(0, tk.END)  # Clear current list
            for folder in folders:
                folders_listbox.insert(tk.END, folder)

    button_load_group = tk.Button(root, text="Load Group", command=load_group)
    button_load_group.pack()

    # Button to perform the copy action
    button_copy = tk.Button(root, text="Copy to Selected Folders", command=lambda: [copy_file_to_destinations(payslip_var.get(), folder) for folder in folders_listbox.get(0, tk.END)])
    button_copy.pack()

    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    root.mainloop()

if __name__ == "__main__":
    main()
