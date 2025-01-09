from utils.image_processor import read_pdf_with_images
from utils.table_extractor import extract_tables_from_pdf
import pdfplumber

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_unstructured_pdf(file):
    # Extract text
    text = read_pdf(file)

    # Extract images and process with OCR
    images_text = read_pdf_with_images(file)

    # Extract tables
    tables = extract_tables_from_pdf(file)

    return {
        "text": text,
        "images_text": images_text,
        "tables": tables
    }
