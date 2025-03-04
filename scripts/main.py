import os
import sys

import time
import requests

GROBID_URL = "http://grobid:8070/api/processFulltextDocument"
GROBID_ALIVE = "http://grobid:8070/api/isalive"

def check_grobid_alive():
    """Verifica si Grobid está activo antes de ejecutar el análisis."""
    print("Esperando a que Grobid esté listo...")
    while True:
        try:
            response = requests.get(GROBID_ALIVE)
            if response.status_code == 200:
                print("✅ Grobid está activo")
                break
            else:
                print("🔄 Grobid no está disponible aún, reintentando")
        except requests.exceptions.RequestException:
            print("⏳ No se pudo conectar con Grobid, reintentando en 5 segundos...")
        time.sleep(5)

check_grobid_alive()  # Llamar la función antes de empezar el análisis

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import process_papers as process
import extract_data as extract

def menu():

    process.process_papers()
    extract.extract_data()
    extract.plot_figures()
    extract.save_links()
    extract.generate_wordcloud()


if __name__ == "__main__":
    menu()
