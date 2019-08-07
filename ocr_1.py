import os
from config import *

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

max_images = 10

tomo = "I"

indexfn = os.path.join(tomos_dir, output_prefix + tomo + ".csv")
with open(indexfn) as fin:
    for i,row in enumerate(fin):
        if i > max_images:
            break
        imagefn = row.strip().split(";")[0]
        imagepath = os.path.join(tomos_dir,tiffs_subdir_prefix+tomo,imagefn)
        txt = pytesseract.image_to_string(Image.open(imagepath), lang='spa')
        print("\n ---------------------- ")
        print(imagefn)
        print(txt)
