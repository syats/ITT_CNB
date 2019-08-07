# Preprocesamiento de expendientes guerra sucia

### Input: 
1. archivos pdf con muchos documentos y bookmarks por documento
2. un archivo pdf por cada página (extraido con adobe acrobat)

### Prerequisitos:
``` sudo snap install pdftk ```

### Extraer índice del PDF:
```pdftk "Tomo III.pdf" dump_data_^Cf8 > in_III.info```

### Crear TIFFs del PDF:
Convertir a tiffs 
1. Crear script ``` ls *pdf | awk '{print "convert -density 300 \"" $0 "\" TOMO_II_" $5 ".tiff"}' | sed 's/pdf\.tiff/tiff/g' > convert.sh ```
2. Ejecutar script ```sh  convert.sh```

# Pruebas rápidas de OCR

### Instalar tesseract

1. Los binarios de tesseract :```apt-get install tesseract-ocr libtesseract-dev tesseract-ocr-spa```
2. Los paquetes de python ```pip install -r requirements.txt```