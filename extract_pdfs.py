from PyPDF2 import PdfReader
import json

pdfs = [
    'Test/Test Final.pdf',
    'Test/Test Modulo 1.pdf', 
    'Test/Test Modulo 2.pdf',
    'Test/Test Modulo 3.pdf',
    'Test/Test Modulo 4.pdf'
]

for pdf_name in pdfs:
    print(f"\n{'='*60}")
    print(f"=== {pdf_name} ===")
    print('='*60)
    try:
        reader = PdfReader(pdf_name)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                print(f"--- Page {i+1} ---")
                print(text)
                print()
    except Exception as e:
        print(f"Error: {e}")