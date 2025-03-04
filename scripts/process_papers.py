import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(BASE_DIR, "..", "papers")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "..", "output")
GROBID_URL = os.getenv("GROBID_URL", "http://localhost:8070/api/processFulltextDocument")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_papers():
    """Envía todos los PDFs en 'papers/' a Grobid y guarda los XMLs en 'output/'."""
    all_files = os.listdir(PDF_FOLDER)
    pdf_files = [file for file in all_files if file.endswith(".pdf")]

    if not pdf_files:
        print("No se encontraron archivos PDF.")
        return

    for pdf in pdf_files:
        pdf_path = os.path.join(PDF_FOLDER, pdf)
        output_path = os.path.join(OUTPUT_FOLDER, pdf.replace(".pdf", ".xml"))

        with open(pdf_path, "rb") as pdf_file:
            response = requests.post(GROBID_URL, files={"input": pdf_file})

        if response.status_code == 200:
            with open(output_path, "w", encoding="utf-8") as output_file:
                output_file.write(response.text)
            print(f"Procesado: {pdf} -> Guardado en {output_path}")
        else:
            print(f"Error con {pdf}: {response.status_code}")
