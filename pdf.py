from PyPDF2 import PdfReader


def read_pdf(filename):
    reader = PdfReader(f"pdf_files/{filename}.pdf")
    all_text = ''
    for page in reader.pages:
        all_text += page.extract_text()
    return all_text


if __name__ == '__main__':
    read_pdf('O-Espírito_8Ed')
