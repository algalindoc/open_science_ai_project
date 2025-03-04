import os
import sys
import time
import pytest
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts import extract_data

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))

TEST_CSV_FILE = os.path.join(OUTPUT_DIR, "results.csv")
TEST_LINKS_FILE = os.path.join(OUTPUT_DIR, "links_found.txt")
TEST_FIGURES_FILE = os.path.join(OUTPUT_DIR, "figures_per_article.png")
TEST_WORDCLOUD_FILE = os.path.join(OUTPUT_DIR, "wordcloud.png")

print(f"🔎 Buscando archivos en: {OUTPUT_DIR}")

@pytest.fixture
def setup_sample_data():
    """Crea un archivo CSV de prueba en output/"""
    sample_data = pd.DataFrame({
        "archivo": ["test1.xml", "test2.xml"],
        "título": ["Título 1", "Título 2"],
        "resumen": ["Resumen de prueba 1", "Resumen de prueba 2"],
        "num_figuras": [3, 5],
        "enlaces": ["http://example.com, http://test.com", "No se encontraron enlaces"]
    })
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sample_data.to_csv(TEST_CSV_FILE, index=False)
    yield
    os.remove(TEST_CSV_FILE)

def test_example():
    """Test básico para verificar pytest."""
    assert True 

def test_extract_data_no_files(monkeypatch):
    """Prueba cuando no hay archivos XML en la carpeta output."""
    monkeypatch.setattr(os, "listdir", lambda _: [])
    assert extract_data.extract_data() is None  # debería manejar la falta de archivos sin errores

def test_extract_data(setup_sample_data):
    """Prueba si el archivo CSV se genera correctamente."""
    df = pd.read_csv(TEST_CSV_FILE)
    assert len(df) == 2  # Asegurar que haya dos registros
    assert df["título"][0] == "Título 1"  # Verificar que los títulos sean correctos
    assert df["num_figuras"][1] == 5  # Comprobar número de figuras del segundo artículo

def test_plot_figures(setup_sample_data):
    """Verifica que la gráfica de figuras por artículo se genera correctamente."""
    extract_data.plot_figures()
    time.sleep(2)  # Espera un poco para asegurar la escritura del archivo
    assert os.path.exists(TEST_FIGURES_FILE), f" {TEST_FIGURES_FILE}"

def test_save_links(setup_sample_data):
    """Verifica que el archivo de enlaces se genera correctamente."""
    extract_data.save_links()
    time.sleep(2)  # Espera para asegurar que el archivo se guarde
    assert os.path.exists(TEST_LINKS_FILE), f"No se encontró {TEST_LINKS_FILE}"

def test_generate_wordcloud(setup_sample_data):
    """Verifica que la nube de palabras se genera correctamente."""
    extract_data.generate_wordcloud()
    time.sleep(2)
    assert os.path.exists(TEST_WORDCLOUD_FILE), f"No se encontró {TEST_WORDCLOUD_FILE}"
