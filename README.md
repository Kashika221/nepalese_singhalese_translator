# Nepalese-Singhalese Translator

A Python-based translation toolkit for converting text between Nepalese and Sinhalese languages with support for extracting text from PDF and PNG image files.

## Overview

This project provides a complete solution for translating content between Nepalese and Sinhalese languages. It includes specialized modules for extracting text from different document formats (PDFs and images) and translating the extracted text seamlessly. The toolkit is designed to handle both digital text and scanned documents.

## Features

- **PDF Text Extraction**: Extract text content from PDF documents
- **Image Text Extraction**: Extract text from PNG images using OCR
- **Nepalese to Sinhalese Translation**: Convert Nepalese text to Sinhalese
- **Sinhalese to Nepalese Translation**: Convert Sinhalese text to Nepalese
- **Batch Processing**: Process multiple files efficiently
- **Support for Documents**: Handle both native text and scanned documents
- **Result Storage**: Save translated output to organized directories

## Project Structure

```
nepalese_singhalese_translator/
├── pdf_extractor.py      # PDF text extraction module
├── png_extractor.py      # PNG/Image OCR extraction module
├── translator.py         # Translation engine
├── requirements.txt      # Project dependencies
├── test_data/           # Sample input files for testing
│   ├── sample.pdf
│   └── sample.png
└── result_data/         # Output directory for translated results
    ├── translations.txt
    └── results.csv
```

## Technology Stack

- **Python 3.7+**: Core programming language
- **PDF Processing**: PyPDF2, pdf2image, pdfplumber
- **OCR (Optical Character Recognition)**: Tesseract, pytesseract
- **Translation**: Google Translate API or similar translation service
- **Text Processing**: NLTK, regex
- **Data Handling**: pandas (for CSV output)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Tesseract OCR engine (for PNG extraction)
- poppler utilities (for PDF processing)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Kashika221/nepalese_singhalese_translator.git
   cd nepalese_singhalese_translator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install system dependencies (Ubuntu/Debian):
   ```bash
   # For Tesseract OCR
   sudo apt-get install tesseract-ocr tesseract-ocr-nep tesseract-ocr-sin
   
   # For poppler
   sudo apt-get install poppler-utils
   ```

   **On macOS**:
   ```bash
   brew install tesseract
   brew install poppler
   ```

   **On Windows**:
   - Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
   - Download poppler binaries and add to PATH

5. Verify installation:
   ```bash
   python -c "import pytesseract; print('Tesseract installed successfully')"
   ```

## Usage

### Extracting Text from PDF

```python
from pdf_extractor import extract_pdf_text

# Extract text from a PDF file
pdf_path = "test_data/sample.pdf"
extracted_text = extract_pdf_text(pdf_path)
print(extracted_text)
```

### Extracting Text from PNG Images

```python
from png_extractor import extract_image_text

# Extract text from a PNG image
image_path = "test_data/sample.png"
extracted_text = extract_image_text(image_path)
print(extracted_text)
```

### Translating Text

```python
from translator import translate_text

# Translate Nepalese to Sinhalese
nepali_text = "नेपाल एक सुन्दर देश हो"
sinhalese_text = translate_text(nepali_text, source_lang='nepali', target_lang='sinhalese')
print(sinhalese_text)

# Translate Sinhalese to Nepalese
sinhalese_text = "ශ්‍රී ලංකා ලස්සන රට වේ"
nepali_text = translate_text(sinhalese_text, source_lang='sinhalese', target_lang='nepali')
print(nepali_text)
```

### Complete Pipeline: PDF to Translation

```python
from pdf_extractor import extract_pdf_text
from translator import translate_text

# Extract text from PDF
pdf_path = "test_data/sample.pdf"
nepali_text = extract_pdf_text(pdf_path)

# Translate to Sinhalese
sinhalese_result = translate_text(nepali_text, source_lang='nepali', target_lang='sinhalese')

# Save results
with open('result_data/translated_document.txt', 'w', encoding='utf-8') as f:
    f.write(sinhalese_result)
```

### Complete Pipeline: Image to Translation

```python
from png_extractor import extract_image_text
from translator import translate_text

# Extract text from image
image_path = "test_data/sample.png"
nepali_text = extract_image_text(image_path)

# Translate to Sinhalese
sinhalese_result = translate_text(nepali_text, source_lang='nepali', target_lang='sinhalese')

# Save results
with open('result_data/image_translation.txt', 'w', encoding='utf-8') as f:
    f.write(sinhalese_result)
```

## Module Descriptions

### pdf_extractor.py

Handles extraction of text from PDF documents.

**Key Functions**:
- `extract_pdf_text(pdf_path)`: Extract all text from a PDF file
- `extract_pdf_page(pdf_path, page_num)`: Extract text from a specific page
- `extract_pdf_with_layout(pdf_path)`: Preserve document layout during extraction

### png_extractor.py

Performs OCR on PNG images to extract text.

**Key Functions**:
- `extract_image_text(image_path)`: Extract text from a PNG/image file
- `extract_text_with_preprocessing(image_path)`: Extract with image preprocessing
- `batch_extract_images(image_folder)`: Process multiple images in a folder

### translator.py

Translates text between Nepalese and Sinhalese languages.

**Key Functions**:
- `translate_text(text, source_lang, target_lang)`: Translate text between languages
- `batch_translate(texts, source_lang, target_lang)`: Translate multiple texts
- `detect_language(text)`: Detect the language of input text
- `get_supported_languages()`: List supported languages

## Configuration

### Language Codes

- `nepali` or `ne`: Nepalese language
- `sinhalese` or `si`: Sinhalese language

### Output Formats

Results can be saved in multiple formats:
- `.txt`: Plain text files
- `.csv`: Comma-separated values
- `.json`: JSON format with metadata

## Examples

### Example 1: Translate a Nepalese Document

```bash
python translator.py --input test_data/nepalese_document.pdf --output result_data/sinhalese_output.txt --from nepali --to sinhalese
```

### Example 2: Extract and Translate from Image

```bash
python translator.py --input test_data/nepali_text.png --output result_data/translation.txt --from nepali --to sinhalese --source-type image
```

### Example 3: Batch Processing

```bash
python translator.py --input test_data/ --output result_data/ --from nepali --to sinhalese --batch
```

## Performance Tips

- Use high-quality PDF files for better extraction accuracy
- For images, ensure text is clear and well-lit
- Preprocessing images can improve OCR accuracy
- Use batch processing for multiple files
- Store API credentials securely

## Supported Languages

| Language | Code | Direction |
|----------|------|-----------|
| Nepalese | ne, nepali | Both ways |
| Sinhalese | si, sinhalese | Both ways |

## Limitations

- OCR accuracy depends on image quality and text clarity
- Translation quality depends on the underlying translation API
- Complex document layouts may not be perfectly preserved
- Handwritten text recognition is limited
- Best results with printed, standard fonts

## Troubleshooting

### Issue: "Tesseract is not installed or not in PATH"
**Solution**: Install Tesseract following system-specific instructions above, or set the path explicitly:
```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Issue: "PDF extraction returns empty text"
**Solution**: Ensure PDF is not image-based. For scanned PDFs, use image extraction method instead.

### Issue: "Poor OCR accuracy on images"
**Solution**: 
- Improve image quality
- Preprocess images (contrast, brightness adjustment)
- Use higher resolution images

### Issue: "Translation API errors"
**Solution**: Check API credentials, rate limits, and internet connectivity.

## Future Enhancements

- Support for additional South Asian languages
- Improved OCR accuracy with custom training models
- Document layout preservation in translations
- Web-based user interface
- REST API for remote processing
- Real-time streaming translation
- Handwriting recognition support
- Multi-language document support

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Make your changes and test thoroughly
4. Commit your changes (`git commit -m 'Add YourFeature'`)
5. Push to the branch (`git push origin feature/YourFeature`)
6. Open a Pull Request

## Testing

Run tests to ensure functionality:

```bash
# Test PDF extraction
python -m pytest tests/test_pdf_extractor.py -v

# Test image extraction
python -m pytest tests/test_png_extractor.py -v

# Test translation
python -m pytest tests/test_translator.py -v
```

## License

This project is open source and available under the MIT License - see LICENSE file for details.

## Acknowledgments

- Tesseract OCR Project
- Google Translate API
- NLTK (Natural Language Toolkit)
- PyPDF2 and related libraries

## References

- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)
- [pytesseract Documentation](https://pytesseract.readthedocs.io/)
- [Google Translate API](https://cloud.google.com/translate/docs)
- [NLTK Documentation](https://www.nltk.org/)

## Contact & Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Check documentation and examples
- Review test cases for usage patterns

## Disclaimer

This project is intended for educational and commercial purposes. Ensure compliance with translation service terms of use and respect language and cultural nuances when translating between languages.

---

**Bridging languages between Nepal and Sri Lanka** 