import docx2txt
import PyPDF2

def extract_text(path):
    if path.endswith(".pdf"):
        with open(path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif path.endswith(".docx"):
        return docx2txt.process(path)
    else:
        raise ValueError("Unsupported file type")
