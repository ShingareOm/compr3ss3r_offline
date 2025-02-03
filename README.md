# PDF Compressor
![image](https://github.com/user-attachments/assets/72eef7c7-f42c-4c4e-a935-b5e36f25ca3f)

A lightweight and efficient PDF compression tool built with Python and Bottle. This tool allows users to upload multiple PDFs, compress them with different quality settings, and download the compressed files as a ZIP archive.

## Features
- **Drag & Drop** PDF uploads for easy file selection.
- **Multiple File Upload** support.
- **Compression Levels** controlled via a smooth slider.
- **Anonymous Hacker Theme** with dark UI.
- **Secure & Privacy-Focused** – No data is stored.

---

> [!WARNING]  
> This tool uses **Ghostscript** (`gs`) for PDF compression. Ensure Ghostscript is installed on your system.
> Large file uploads may be **resource-intensive**, depending on your system.
> **No Cloud Storage** – All compression is done locally for **privacy** and **security**.



## Installation
### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the Application
```sh

python3 app.py
```
The app will run on `http://0.0.0.0:1234/`.

### Build Platform-Independent Binaries
For **Linux & Windows**, use:
```sh
pyinstaller --onefile --name pdf-compressor app.py
```
The binary will be generated in the `dist/` folder.

## GitHub Actions for Auto-Release
Whenever a change is pushed to the repository, GitHub Actions will:
1. Build the binary for **Windows & Linux**.
2. Upload the compiled binaries as a **GitHub Release**.

## Author
**Om Shingare**  
GitHub: [ShingareOm](https://github.com/ShingareOm)  
YouTube: [@shingareom](https://www.youtube.com/@shingareom)  

---

> [!WARNING]  
> **"Privacy is not a privilege, it's a right!"** 🔥  
**This tool ensures your PDFs stay secure and private. No data leaks, no tracking – just pure compression!**
