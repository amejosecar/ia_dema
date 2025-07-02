import markdown
import pdfkit

def convertir_md_a_pdf(input_md, output_pdf):
    with open(input_md, 'r', encoding='utf-8') as archivo:
        markdown_texto = archivo.read()

    # Convertir a HTML
    html = markdown.markdown(markdown_texto)

    # Envolver en un HTML más completo (opcional: personalizar estilos)
    html_final = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                margin: 40px;
                font-size: 14px;
                color: #333;
            }}
            h1, h2, h3 {{
                color: #003366;
            }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """

    # Convertir a PDF
    pdfkit.from_string(html_final, output_pdf)
    print(f"✅ PDF creado exitosamente: {output_pdf}")

# Ejecutar la conversión
convertir_md_a_pdf("cv_americo.md", "CV_Américo_Carrillo.pdf")
