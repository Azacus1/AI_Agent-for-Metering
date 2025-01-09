from PIL import Image
import pytesseract
import pdfplumber
import io

def extract_images_from_pdf(file_path):
    images = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.images:
                for img in page.images:
                    # Extract the image's bounding box
                    x0, top, x1, bottom = img['x0'], img['top'], img['x1'], img['bottom']
                    # Extract the image as a cropped region
                    image = page.to_image().original.crop((x0, top, x1, bottom))
                    images.append(image)
    return images

def read_pdf_with_images(file_path):
    text = ""
    images = extract_images_from_pdf(file_path)
    for image in images:
        # Convert image to text using OCR
        text += pytesseract.image_to_string(image)
    return text
