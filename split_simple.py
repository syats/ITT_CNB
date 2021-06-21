import os
from os.path import join as opj
from PyPDF2 import PdfFileReader, PdfFileWriter

tomos_dir = "./data/Multipagina/"
tiffs_dir = "./data/Monopagina/"

files = [opj(tomos_dir,x) for x in  os.listdir(tomos_dir) if x.endswith("pdf")]

for tomoname in files:

    tomo = tomoname.split("/")[-1].replace(" ","_").replace(".pdf","")
    # This is where the output files will be saved to
    out_dir = opj(tiffs_dir,tomo)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    with open(tomoname,"rb") as fp:
        pdf = PdfFileReader(fp)
        print(pdf.getNumPages(), "Found in PDF")
        numpages = pdf.getNumPages()
        for page in range(numpages):
            pdf_writer = PdfFileWriter()
            pagepdf = pdf.getPage(page)

            pdf_writer.addPage(pagepdf)
            output_filename = '{}_pg{:05d}.pdf'.format(
                tomo, page + 1)

            pdf_writer.write(output_filename)


