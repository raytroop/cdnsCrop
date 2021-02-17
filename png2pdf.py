import os
import glob
import shutil
from tqdm import tqdm
from PIL import Image


INPUTDIR = './procimgdir'
PDFDIR = './pdfsdir'
if os.path.isdir(PDFDIR):
    shutil.rmtree(PDFDIR)
os.mkdir(PDFDIR)

flist = glob.glob(os.path.join(INPUTDIR, '*'))
flist = [os.path.basename(x) for x in flist]
print(flist)
for fn in tqdm(flist):
    img = Image.open(os.path.join(INPUTDIR, fn))
    img_pdf = img.convert('RGB')
    fnpdf = os.path.splitext(fn)[0] + '.pdf'
    img_pdf.save(os.path.join(PDFDIR, fnpdf), quality=100)
