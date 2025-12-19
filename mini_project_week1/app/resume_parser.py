"""
PDF → Text parser
"""

from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF resume.

    Args:
        pdf_path (str): Path to resume PDF

    Returns:
        str: Extracted text
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        if not text.strip():
            raise ValueError("PDF contains no readable text")

        return text.strip()

    except Exception as e:
        raise RuntimeError(f"Failed to parse PDF: {e}")
