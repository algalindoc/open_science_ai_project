# Open Science AI Project

## 🚀 Descripción
Este proyecto utiliza **Grobid** y herramientas de análisis de datos en **Python** para extraer información de documentos científicos en formato PDF. Con Docker, se garantiza una ejecución reproducible y sin complicaciones.

---

## 📦 Instalación y Configuración

### **1️⃣ Requisitos Previos**
- Tener **Docker** y **Docker Compose** instalados.
  - [Descargar Docker](https://www.docker.com/get-started)
- (Opcional) Tener **Python 3.10+** y `pip` instalados si deseas correr el código sin Docker.

### **2️⃣ Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/open_science_ai_project.git
cd open_science_ai_project
```

### **3️⃣ Ejecutar el Proyecto con Docker**
Para ejecutar el proyecto con **Docker Compose**:
```bash
docker-compose up --build
```
Esto iniciará **Grobid** y el análisis de documentos.

✅ **Los archivos de salida estarán en la carpeta `output/`**.


---

## 🛠️ Uso del Proyecto

### **1️⃣ Agregar PDFs para Analizar**
Coloca los archivos **.pdf** en la carpeta `papers/`.

### **2️⃣ Ejecutar el Análisis Manualmente**
Si ya tienes Docker en ejecución pero quieres ejecutar el script manualmente dentro del contenedor:
```bash
docker exec -it open_science_analysis python scripts/main.py
```

### **3️⃣ Revisar Resultados**
Los resultados se guardan en `output/`:
- `results.csv` 📄 → Tabla con títulos, resúmenes, figuras y enlaces extraídos.
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
│   ├── main.py          # Script principal
│   ├── process_papers.py # Procesa PDFs con Grobid
│   ├── extract_data.py  # Extrae y analiza datos de los documentos
│── tests/               # Pruebas unitarias
│── Dockerfile           # Configuración de Docker
│── docker-compose.yml   # Configuración de Docker Compose
│── requirements.txt     # Dependencias del proyecto
│── README.md            # Documentación principal
```

---

## 💡 Futuras Mejoras
📌 **Agregar soporte para análisis de gráficos y tablas.**
📌 **Optimizar el preprocesamiento de texto con NLP.**
📌 **Integrar visualización interactiva de los resultados.**

---

## 📄 Licencia
Este proyecto está bajo la licencia MIT. ¡Siéntete libre de contribuir! 😊

