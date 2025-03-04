import os
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib

# backend sin GUI para evitar errores de `tkinter`
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
XML_FOLDER = os.path.join(BASE_DIR, "..", "output")
RESULTS_FILE = os.path.join(XML_FOLDER, "results.csv")
NS = {"tei": "http://www.tei-c.org/ns/1.0"}

def extract_data():
    """Extrae título, resumen, #figuras y enlaces de los XMLs en 'output/'."""
    if not os.path.exists(XML_FOLDER):
        print(f"ERROR: La carpeta {XML_FOLDER} no existe.")
        return

    xml_files = [os.path.join(XML_FOLDER, f) for f in os.listdir(XML_FOLDER) if f.endswith(".xml")]

    if not xml_files:
        print("No se encontraron archivos XML en la carpeta 'output/'.")
        return
    
    extracted_data = []
    for xml_file in xml_files:
        print(f"Procesando archivo: {xml_file}")

        try:
            arbol = ET.parse(xml_file)
            raiz = arbol.getroot()
        except Exception as e:
            print(f"ERROR: No se pudo leer {xml_file}. Detalles: {e}")
            continue

        title = raiz.find(".//tei:titleStmt/tei:title", NS)
        abstract = raiz.find(".//tei:abstract/tei:div/tei:p", NS)
        num_figures = len(raiz.findall(".//tei:figure", NS))
        links = [ptr.get("target") for ptr in raiz.findall(".//tei:ptr", NS) if ptr.get("target")]

        extracted_data.append({
            "archivo": os.path.basename(xml_file),
            "título": title.text.strip() if title is not None else "Título no encontrado",
            "resumen": abstract.text.strip() if abstract is not None else "Resumen no encontrado",
            "num_figuras": num_figures,
            "enlaces": ", ".join(links) if links else "No se encontraron enlaces"
        })

    # Verificar si extracted_data tiene información
    if not extracted_data:
        print("No se extrajo ninguna información de los XMLs.")
        return

    # Guardar los resultados
    try:
        df = pd.DataFrame(extracted_data)
        df.to_csv(RESULTS_FILE, index=False)
        print(f"Archivo 'results.csv' guardado en {RESULTS_FILE}")
    except Exception as e:
        print(f"ERROR: No se pudo escribir en {RESULTS_FILE}. Detalles: {e}")


def plot_figures():
    """Genera gráfico de número de figuras por artículo."""
    df = pd.read_csv(RESULTS_FILE)
    plt.bar(df["archivo"], df["num_figuras"], color="skyblue")
    plt.xticks(rotation=90)
    plt.xlabel("Artículo")
    plt.ylabel("Número de Figuras")
    plt.title("Número de Figuras por Artículo")
    plt.savefig(os.path.join(XML_FOLDER, "figures_per_article.png"))
    plt.show()
    print(" Gráfico de figuras generado.")

def save_links():
    """Guarda una lista de los enlaces encontrados."""
    df = pd.read_csv(RESULTS_FILE)
    links_file = os.path.join(XML_FOLDER, "links_found.txt")
    
    with open(links_file, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            f.write(f" {row['archivo']}:\n")
            if row['enlaces'] != 'No se encontraron enlaces':
                f.write(row['enlaces'] + '\n\n')
            else:
                f.write('    No se encontraron enlaces' + '\n\n')
    
    print(f"Lista de enlaces guardada en '{links_file}'.")

def generate_wordcloud():
    """Genera nube de palabras basada en los abstracts."""
    df = pd.read_csv(RESULTS_FILE)
    text = " ".join(df["resumen"].dropna())

    if text.strip():
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Nube de Palabras basada en Abstracts")
        plt.savefig(os.path.join(XML_FOLDER, "wordcloud.png"))
        plt.show()
        print("Nube de palabras generada.")
    else:
        print("No hay suficientes abstracts para generar una nube de palabras.")
