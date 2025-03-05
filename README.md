# Open Science AI Project

[![DOI](https://zenodo.org/badge/942804117.svg)](https://doi.org/10.5281/zenodo.14969304)

## 🚀 Descripción
Este proyecto utiliza **Grobid** y herramientas de análisis de datos en **Python** para extraer información de documentos científicos en formato PDF. Con Docker, se garantiza una ejecución reproducible y sin complicaciones.

---

## 📦 Instalación y Configuración

### **1️⃣ Requisitos Previos**
- Tener **Docker** y **Docker Compose** instalados.
  - [Descargar Docker](https://www.docker.com/get-started)
  - Abrir la aplicación de docker desktop
- (Opcional) Tener **Python 3.10+** y `pip` instalados si deseas correr el código sin Docker.

### **2️⃣ Clonar el Repositorio**
```bash
git clone https://github.com/algalindoc/open_science_ai_project.git
cd open_science_ai_project
```

---

## 🔄 Opciones de Ejecución

### **Opción 1: Ejecutar con Docker (Recomendada)**
```bash
docker-compose up --build
```
Esto iniciará **Grobid** y el análisis de documentos de forma automatizada. 

✅ **Los archivos de salida estarán en la carpeta `output/`.**

---

### **Opción 2: Ejecutar sin Docker**
Si prefieres no usar Docker, sigue estos pasos:

1️⃣ **Crear un entorno virtual**
```bash
python -m venv env
source env/bin/activate  # En Linux/Mac
env\Scripts\activate  # En Windows
```

2️⃣ **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3️⃣ **Ejecutar el análisis**
```bash
python scripts/main.py
```
✅ **Los archivos procesados se guardarán en `output/`**.

4️⃣ **Desactivar el entorno virtual (opcional)**
```bash
deactivate
```

---

## 🛠️ Uso del Proyecto

### **1️⃣ Agregar PDFs para Analizar**
Coloca los archivos **.pdf** en la carpeta `papers/`.

### **2️⃣ Revisar Resultados**
Los resultados se guardan en `output/`:
- `results.csv` 📝 → Tabla con títulos, resúmenes, figuras y enlaces extraídos.
- `figures_per_article.png` 📊 → Gráfico de número de figuras por artículo.
- `wordcloud.png` ☁️ → Nube de palabras basada en los resúmenes.
- `links_found.txt` 🔗 → Lista de enlaces extraídos de los documentos.

---

## ✅ Ejecutar Pruebas Unitarias
Si deseas verificar que todo funcione correctamente:
```bash
docker exec -it open_science_analysis pytest
```
Esto ejecutará las pruebas en `tests/` para validar la extracción de datos.

---

## 📌 Estructura del Proyecto
```
open_science_ai_project/
│── papers/              # Carpeta donde colocar los PDFs para analizar
│── output/              # Carpeta donde se guardan los resultados
│── scripts/             # Código fuente
│   ├─ main.py          # Script principal
│   ├─ process_papers.py # Procesa PDFs con Grobid
│   └─ extract_data.py  # Extrae y analiza datos de los documentos
│── tests/               # Pruebas unitarias
│── Dockerfile           # Configuración de Docker
│── docker-compose.yml   # Configuración de Docker Compose
│── requirements.txt     # Dependencias del proyecto
│── codemeta.json        # Archivo de metadatos JSON-LD
│── README.md            # Documentación principal
```

---

## 📝 Licencia
Este proyecto está bajo la licencia MIT.  
Puedes leer más en el archivo [`LICENSE`](LICENSE).


