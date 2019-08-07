try:
    from PIL import Image
except ImportError:
    import Image

import os
import numpy as np
from config import *
from matplotlib import pylab as pl

max_images = 125
sampleranges = [(200, 300, 0, -1), (-300, -200, 0, -1)]
tomo = "I"
bins = [i*8 for i in range(30)]
numbins = len(bins)-1

indexfn = os.path.join(tomos_dir, output_prefix + tomo + ".csv")
timeseries = np.zeros((max_images, numbins * len(sampleranges)))

with open(indexfn) as fin:
    for i, row in enumerate(fin):
        if i >= max_images:
            break
        imagefn = row.strip().split(";")[0]
        imagepath = os.path.join(tomos_dir, tiffs_subdir_prefix + tomo, imagefn)
        im = Image.open(imagepath)
        w, h = im.size
        arr = np.asarray(im)
        if w > h:
            arr = arr.T
        whovect = np.zeros(numbins * len(sampleranges))
        for ix, ra in enumerate(sampleranges):
            x0, x1, y0, y1 = ra
            sli = arr[x0:x1, y0:y1, :]
            histo = np.histogram(sli[:, :, 0], bins=bins)
            vect = histo[0]
            whovect[ix * numbins: (ix+1)*numbins] = vect
        timeseries[i, :] = whovect

tsdif = timeseries[1:, :] - timeseries[:-1, :]


pl.imshow(tsdif)  # diferencia


