# Rationale - Open Science AI Project

## 📌 Introducción
Este documento explica las decisiones técnicas detrás del **Open Science AI Project**, detallando por qué se eligieron ciertas herramientas y cómo se estructuró el código. También se incluyen los métodos utilizados para validar cada paso del proceso.

---

## 🔹 Elección de Tecnologías

### **1️⃣ Grobid - Procesamiento de Documentos Científicos**
Grobid (GeneRation Of BIbliographic Data) es una de las herramientas más avanzadas para la extracción estructurada de datos a partir de PDFs científicos. Se eligió porque:
- ✅ Proporciona una API accesible para extraer metadatos, resúmenes y figuras.
- ✅ Es altamente configurable y extensible para futuras mejoras.
- ✅ Es compatible con procesamiento en lote, ideal para análisis masivos.

### **2️⃣ Python - Lenguaje de Programación**
Python es el lenguaje ideal para este proyecto debido a:
- ✅ Su extensa comunidad científica y ecosistema de bibliotecas (pandas, matplotlib, requests, pytest, etc.).
- ✅ Su facilidad de integración con Grobid mediante solicitudes HTTP.
- ✅ Su compatibilidad con herramientas de análisis de datos y aprendizaje automático para futuras mejoras.

### **3️⃣ Docker - Reproducibilidad y Entorno Controlado**
El uso de **Docker** asegura que el código pueda ejecutarse en cualquier máquina sin problemas de dependencias:
- ✅ Asegura que Grobid y el código de análisis corran en un ambiente aislado.
- ✅ Permite compartir el proyecto sin necesidad de instalar paquetes manualmente.
- ✅ Facilita la implementación en servidores o en la nube sin cambios en la configuración.

### **4️⃣ Docker Compose - Orquestación de Contenedores**
Se eligió **Docker Compose** para simplificar la ejecución de Grobid y el análisis:
- ✅ Define y administra múltiples servicios en un solo archivo (`docker-compose.yml`).
- ✅ Facilita la ejecución con un solo comando (`docker-compose up --build`).
- ✅ Garantiza que el análisis solo se ejecute cuando Grobid esté listo.

---

## 🔹 Validación de Respuestas

### **1️⃣ Verificación de Extracción de Datos**
Para validar que Grobid extrae correctamente los datos de los PDFs, se implementaron pruebas unitarias en `tests/test_extract.py`. Estas pruebas verifican:
- ✅ Que los archivos XML generados contienen títulos y resúmenes correctos.
- ✅ Que el número de figuras extraídas coincide con la cantidad presente en el documento.
- ✅ Que los enlaces dentro de los documentos sean correctamente detectados y almacenados.

### **2️⃣ Validación de Análisis de Datos**
Se implementaron verificaciones para garantizar que los análisis generen resultados coherentes:
- ✅ **Resultados esperados:** La nube de palabras (`wordcloud.png`) debe reflejar palabras clave relevantes de los resúmenes.
- ✅ **Gráficos de figuras:** Se comparó manualmente con los documentos para asegurar que el número de figuras sea correcto.
- ✅ **Resultados en CSV:** Se verificó que `results.csv` contenga la estructura correcta y los datos extraídos sean consistentes.

### **3️⃣ Pruebas de Integración en Docker**
Para validar que el proyecto funciona correctamente en un entorno controlado:
- ✅ Se ejecutó `docker-compose up --build` en múltiples sistemas para asegurar compatibilidad.
- ✅ Se verificó que los archivos en `output/` se generen correctamente sin errores.
- ✅ Se probó la ejecución manual dentro del contenedor para validar que `main.py` se ejecuta correctamente.

### **4️⃣ Manejo de Errores y Robustez**
Para garantizar que el sistema es resistente a fallos:
- ✅ Se agregó una función en `main.py` que espera a que Grobid esté disponible antes de ejecutar el análisis.
- ✅ Se capturan excepciones en el procesamiento de documentos para evitar que errores individuales detengan todo el análisis.
- ✅ Se agregó control de errores en `process_papers.py` para manejar PDFs corruptos o vacíos.

---

## 🔹 Estructura del Código

📌 **El proyecto sigue una estructura modular para facilitar la escalabilidad:**

```
open_science_ai_project/
│── papers/              # PDFs a analizar
│── output/              # Resultados generados
│── scripts/             # Código fuente
│   ├── main.py          # Script principal que ejecuta todo
│   ├── process_papers.py # Procesa PDFs con Grobid
│   ├── extract_data.py  # Extrae y analiza datos
│── tests/               # Pruebas unitarias con pytest
│── Dockerfile           # Definición de la imagen de Docker
│── docker-compose.yml   # Configuración de Docker Compose
│── requirements.txt     # Dependencias de Python
│── README.md            # Documentación de uso
│── RATIONALE.md         # Justificación técnica del proyecto
```

✅ **Se separaron claramente las responsabilidades** entre la extracción de datos y el procesamiento de PDFs.
✅ **Se incluyeron pruebas unitarias** para asegurar que la extracción de datos funciona correctamente.
✅ **Se definió una estructura de directorios** clara y escalable para futuras expansiones.

---

## 🔹 Mejoras Futuras
Algunas mejoras que podrían implementarse:
- 📌 **Soporte para análisis de gráficos y tablas dentro de los PDFs.**
- 📌 **Optimización del preprocesamiento de texto con NLP (Procesamiento de Lenguaje Natural).**
- 📌 **Mejor integración con herramientas de visualización de datos interactivas.**
- 📌 **Paralelización del procesamiento de múltiples documentos para mayor eficiencia.**

---

## 📄 Conclusión
Este documento explica el razonamiento detrás de las elecciones técnicas del proyecto. Con Grobid, Python y Docker, el sistema es **modular, escalable y fácil de ejecutar en cualquier entorno**. Además, se implementaron validaciones para garantizar la exactitud de los datos extraídos y la robustez del sistema.

