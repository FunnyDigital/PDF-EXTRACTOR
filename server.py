from flask import Flask, request, jsonify
import google.generativeai as genai
import PyPDF2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your Gemini API key here
genai.configure(api_key="AIzaSyDc7t-_K2r1VnwejnrGwsSlfqXM3s3OF98")

def extract_text_from_pdf(file_stream):
    reader = PyPDF2.PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

@app.route('/extract', methods=['POST'])
def extract():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    pdf_text = extract_text_from_pdf(file.stream)
    prompt = (
        "Extract all tabular data from the following PDF text. "
        "Return ONLY a valid JSON array of objects, no explanation or extra text. "
        "If no table is found, return an empty array [].\n" + pdf_text
    )
    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
    raw_text = response.text
    print("Gemini raw response:\n", raw_text)  # For debugging
    try:
        import json, re
        # Try direct JSON parse
        data = json.loads(raw_text)
    except Exception:
        # Try to extract JSON array from text
        import re
        match = re.search(r'(\[.*?\])', raw_text, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
            except Exception:
                data = []
        else:
            data = []
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(port=5000, debug=True)