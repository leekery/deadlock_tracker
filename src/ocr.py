import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_text(image):
    text = pytesseract.image_to_string(image, config='--psm 7 digits')
    return text.strip()
