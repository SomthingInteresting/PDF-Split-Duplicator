<img src="resources/images/logo.png" width="300">

**PDFPorter** is a desktop application designed to ease the management of PDF files, specifically for splitting PDFs based on their content and assisting in the process of distributing these splits.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [How to Run](#how-to-run)
4. [Usage Guide](#usage-guide)
5. [Screenshots](#screenshots)
6. [Contributing](#contributing)

## Features

- **Split PDFs**: Breaks down a multi-page PDF into individual PDFs based on content.
- **Custom Naming**: Names individual PDFs using the content within the document (e.g., the first line of each page).
- **File Management**: Easily select destination folders for copying individual PDFs.
- **Group Management**: Save and load groups of destination folders to speed up the process of sending multiple PDFs to their respective folders.
- **Intuitive UI**: A simple and user-friendly interface built with `tkinter`.

## Installation

There are two routes for installation:

### 1. General Users

For most users who don't intend to develop or modify the software, the easiest route is to use the provided executables.

**Windows**:
- [Download the Windows Executable](https://drive.proton.me/urls/JQWYXHPB6G#WlA78E89knNO) and run it.

**Mac**:
- [Download the Mac Executable](https://drive.proton.me/urls/JQWYXHPB6G#WlA78E89knNO) and run it.

> **Note**: Depending on your system settings, you might need to allow the app to run from an unidentified developer. Always make sure you trust software before running it.

### 2. Developers

For those looking to develop, modify, or run the software from source:

1. **Prerequisites**: Ensure you have `Python 3` and `pip` installed on your machine.

2. **Clone the repository**:
    ```bash
    git clone https://github.com/SomthingInteresting/PDFPorter.git
    cd PDFPorter
    ```

3. **Install dependencies**:
    ```bash
    pip install PyPDF2 pdfminer.six tkinter
    ```

4. **Run the application**:
    ```bash
    python main.py
    # Or if you're using Python 3 explicitly:
    python3 main.py
    ```

## Usage Guide

- **Select PDF**: Start by selecting the multi-page PDF you wish to process.
- **View Individual PDFs**: The application will split the main PDF, and you can view individual PDFs using the dropdown menu.
- **Manage Destination Folders**: Use the "Add Folder" and "Remove Folder" buttons to manage where individual PDFs will be copied.
- **Folder Groups**: Save a set of destination folders as a group for easy access in the future. You can also load or remove previously saved groups.
- **Copy to Folders**: Once you've selected the desired PDF and destination folders, hit the "Copy to Selected Folders" button to distribute the PDF.

## Screenshots

### Main Interface
![Main Interface](path_to_screenshot_1.png)
_Main Interface of PDFPorter_

### PDF Selection
![PDF Selection](path_to_screenshot_2.png)
_PDF Selection and Management_

### Folder Management
![Folder Management](path_to_screenshot_3.png)
_Managing Destination Folders_

### Group Management
![Group Management](path_to_screenshot_4.png)
_Saving, Loading, and Removing Folder Groups_

## Future Improvements and Features

### 📅 To-Do Checklist

- [ ] **Optimized Splitting Algorithm**: Improve the speed and efficiency of the PDF splitting mechanism.
- [ ] **Drag-and-Drop Interface**: Implement drag-and-drop functionality for easier file and folder management.
- [ ] **PDF Preview**: Add an in-app PDF previewer to instantly view split PDFs.
- [ ] **Enhanced Group Management**: Implement nested folder groups and group annotations.
- [ ] **Cloud Integration**: Allow users to directly upload split PDFs to cloud services like Google Drive or Dropbox.
- [ ] **Error Logging**: Create an error log feature to track and resolve issues more efficiently.
- [ ] **User Profiles**: Implement user profiles with customizable settings and themes.
- [ ] **Batch Operations**: Allow users to process multiple master PDFs at once.
- [ ] **Localization**: Add support for multiple languages and regional settings.
- [ ] **Change Icon**: Create a custom icon for the application.
- [ ] **Split Page Pattern**: Option to split PDFs based on a pattern of pages (e.g., split every 3 pages).
- [ ] **PDF Naming**: Option to name split PDFs based on different lines or patterns within the document.

Feel free to suggest more improvements or report any issues you encounter!

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you would like to improve the application.

