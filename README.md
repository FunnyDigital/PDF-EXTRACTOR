# PDF to Excel Extractor (Gemini 2.5)

This web application allows you to upload a PDF file, extract tabular data using Google Gemini 2.5 API, view the data in a table, and download it as an Excel file.

## Features
- Upload PDF files from your computer
- Extracts tabular data using Gemini 2.5 (Google Generative AI)
- Displays extracted data in a web table
- Download extracted data as an Excel file

---

## Installation & Setup

### 1. Clone or Copy the Project
Copy all project files (including `index.html` and `server.py`) to a folder on your laptop.

### 2. Install Python (if not already installed)
Download and install Python 3.8 or newer from [python.org](https://www.python.org/downloads/).

### 3. Open a Terminal in the Project Folder
Navigate to the project folder using Command Prompt, PowerShell, or Terminal.

### 4. Create a Virtual Environment (Recommended)
```
python -m venv venv
```
Activate it:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Mac/Linux:
  ```
  source venv/bin/activate
  ```

### 5. Install Dependencies
Run the following command in your terminal:
```
pip install flask flask-cors google-generativeai PyPDF2
```

#### List of Required Python Packages
- flask
- flask-cors
- google-generativeai
- PyPDF2

### 6. Set Your Gemini API Key
Edit `server.py` and replace the value of `genai.configure(api_key=...)` with your own Gemini API key.

### 7. Start the Backend Server
```
python server.py
```
The server will start at `http://localhost:5000`.

### 8. Open the Frontend
Open `index.html` in your web browser (double-click or right-click and choose "Open with").

### 9. Usage
- Click "Choose File" to select a PDF.
- Click "Extract Data" to process the PDF.
- View the extracted data in the table.
- Click "Download Excel" to save the data as an Excel file.

---

## Troubleshooting
- If you see "No data extracted", check the terminal running `server.py` for Gemini API output and errors.
- Make sure your API key is valid and has access to Gemini 2.5.
- Ensure all dependencies are installed in your environment.

---

## Security Note
**Never share your Gemini API key publicly.**

---

## License
This project is for educational and demonstration purposes.
