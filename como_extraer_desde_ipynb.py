import json

# Rutas usando raw strings
archivo_ipynb = r'C:\americo\ia_dema\10_Valores Perdidos\00_Teoría\Tratamiento_valores_perdidos copy.ipynb'
archivo_txt = r'C:\americo\ia_dema\10_Valores Perdidos\00_Teoría\\contenido_extraido.txt'

# Leer el archivo .ipynb
with open(archivo_ipynb, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Extraer contenido
contenido = []
for celda in notebook['cells']:
    if 'source' in celda:
        contenido.append(''.join(celda['source']))
        contenido.append('\n' + '-'*80 + '\n')  # Separador

# Guardar como .txt
with open(archivo_txt, 'w', encoding='utf-8') as f:
    f.writelines(contenido)

print(f'✅ Contenido guardado en: {archivo_txt}')
