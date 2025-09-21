import pytesseract
from PIL import Image

# Set Tesseract path (Windows only, adjust if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def extract_nepali_sinhala_text(image_path, isNepali : bool):
    """
    Extracts text in Nepali and Sinhala from an image using pytesseract.
    """
    try:
        img = Image.open(image_path)
        if isNepali:
            nepali_text = pytesseract.image_to_string(img, lang="nep")
            return nepali_text.strip()
        else:
            sinhala_text = pytesseract.image_to_string(img, lang="sin")
            return sinhala_text.strip()

    except Exception as e:
        return {"error": str(e)}


# Example usage:
isNepalese = False
#result = extract_nepali_sinhala_text("sample2.png", isNepalese)

result = extract_nepali_sinhala_text("sample4.png", isNepalese)

if "error" in result:
    print("Error:", result["error"])
else:
    if isNepalese:
        print("Nepali Text:", result)
    else:
        print("Sinhala Text:", result)