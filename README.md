# Document Question-Answering AI

This project is a Streamlit-based AI application that allows users to upload various types of documents (PDFs, Word, text, or images) and ask questions about their content. The application processes unstructured data such as text, images, tables, and math equations, extracting information and providing intelligent answers using a question-answering model.

---

## Features

- **Document Upload:** Supports PDF, Word, text, and image files.
- **Text Extraction:** Extracts text from PDFs, including multi-column layouts.
- **OCR for Images:** Uses Tesseract OCR to extract text from images in PDFs or standalone image files.
- **Table Extraction:** Extracts tables from PDFs using `camelot`.
- **Question Answering:** Answers user queries based on the extracted document content.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR installed:
  - **Linux:** `sudo apt-get install tesseract-ocr`
  - **Mac:** `brew install tesseract`
  - **Windows:** [Download and install Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/doc_qa_ai.git
   cd doc_qa_ai
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## File Structure

```
doc_qa_ai/
|
├── venv/                      # Virtual environment
├── app.py                     # Main application code
├── requirements.txt           # Dependencies
├── utils/                     # Utility modules
│   ├── file_reader.py         # Handles file reading (PDFs, Word, etc.)
│   ├── text_preprocessor.py   # Handles text preprocessing
│   ├── faiss_indexer.py       # Handles vector indexing
│   ├── table_extractor.py     # Extracts tables from PDFs
│   ├── image_processor.py     # Extracts and processes images from PDFs
│   └── math_processor.py      # Processes math equations (placeholder)
```

---

## How It Works

1. **Upload Document:**
   - Upload a file (PDF, Word, text, or image) via the Streamlit interface.

2. **Extract Data:**
   - Text: Extracted using `pdfplumber` or `PyPDF2`.
   - Images: Extracted using `pdfplumber` and processed with Tesseract OCR.
   - Tables: Extracted using `camelot`.

3. **Combine Data:**
   - Combines extracted text, OCR text, and table data into a unified format.

4. **Question Answering:**
   - Uses a pre-trained transformer model (`deepset/roberta-base-squad2`) to answer user questions based on the extracted data.

---

## Dependencies

Key Python libraries used:
- `streamlit`
- `transformers`
- `sentence-transformers`
- `faiss-cpu`
- `nltk`
- `PyPDF2`
- `pdfplumber`
- `pillow`
- `pytesseract`
- `camelot-py[cv]`
- `tabulate`
- `requests`

Install them using:
```bash
pip install -r requirements.txt
```

---

## Example Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Upload a document via the web interface (e.g., a PDF containing text, images, or tables).

3. Ask a question about the document's content, such as:
   - "What is the title of the document?"
   - "What is the data in the table?"

4. The application will extract relevant context and provide an answer.

---

## Future Enhancements
- Add support for math equation recognition using MathPix API.
- Improve table parsing for complex layouts.
- Add multilingual support for non-English documents.
- Integrate advanced OCR models for better accuracy.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributions
Contributions are welcome! Please open an issue or submit a pull request on the GitHub repository.

---

## Contact
For any inquiries or issues, please contact [your-email@example.com].

