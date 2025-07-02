import pdfkit
import os

# Rutas absolutas
base = r"C:\americo\ia_dema\mi_carpeta_cv"
html_archivo = os.path.join(base, "cv_americo.html")
pdf_salida = os.path.join(base, "CV_Américo_Carrillo_Visual.pdf")

# Opciones de estilo para formato A4
opciones = {
    'page-size': 'A4',
    'encoding': 'UTF-8',
    'margin-top': '15mm',
    'margin-bottom': '15mm',
    'margin-left': '18mm',
    'margin-right': '18mm',
}

try:
    pdfkit.from_file(html_archivo, pdf_salida, options=opciones)
    print(f"✅ PDF generado correctamente: {pdf_salida}")
except Exception as e:
    print("❌ Error al generar el PDF:")
    print(e)
