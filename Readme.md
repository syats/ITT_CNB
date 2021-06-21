# Preprocesamiento de expendientes


## Para el caso de PDFs hechos de scanneres/cámaras, sin anotaciones (e.g. AGN)
Make sure you have installed the following ubuntu/debian packages
`sudo apt update ; sudo apt install imagemagick poppler-utils rename`

0. Create two directories: `Monopagina` and `Multipagina`

1. Put the multipage PDFs in `Multipagina`

2. Create directories for each
`ls *pdf | sed -e 's/ /_/g' | awk '{print "mkdir \"../Monopagina/" $0 "/\""}' | sed 's/.pdf//g' | bash`


3. Convert
`ls *pdf | sed 's/.pdf//g' | awk '{print "pdfimages -j \"" $0 ".pdf\"  \"../Monopagina/" $0 "/\""'} | bash`


4. Rename
`ls *pdf |   sed 's/.pdf//g' | awk '{print "cd \"../Monopagina/" $0 "\" ; for filename in *.jpg; do mv -- \"$filename\"  \"" $0 "_pg$filename\"; done;   cd -"   }' | bash`


5 Put into single folder. If you want all JPEGs to be in a single folder, do:
`ls *pdf |   sed 's/.pdf//g' | awk '{print "cd \"../Monopagina/" $0 "\" ; for filename in *.jpg; do mv -- \"$filename\"  ..; done;   cd -"   }' | bash`
5.1 Delete empty folders
`cd ../Monopagina ; find . -type d -empty -delete`


## Para el caso de PDFs con índices y anotaciones (e.g. del caso Radilla)

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