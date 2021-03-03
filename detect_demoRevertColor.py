""" https://stackoverflow.com/a/11427501/8037585 """

import os
from glob import glob
import cv2
from tqdm import tqdm

OUTDIR = "cropimgdir"

def cropImage(srcimg, filename):
    img = cv2.imread(srcimg)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, 1)

    contours, _ = cv2.findContours(thresh, 1, 2)

    maxArea = 0.0
    maxApprox = None

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            curArea = abs(approx[0][0][0] - approx[2][0][0]) * \
                abs(approx[0][0][1] - approx[2][0][1])
            # print(curArea)
            if curArea > maxArea:
                maxArea = curArea
                maxApprox = approx
        else:
            continue



    if maxApprox is not None:
        x0, y0 = maxApprox[0][0]
        x1, y1 = maxApprox[2][0]
        print(x0, y0, x1, y1)

    if  x1 - x0 < 700 or y1 - y0 < 400:
        cv2.imwrite(filename, img)
    else:
        cv2.imwrite(filename, img[y0:y1, x0:x1, :])

if __name__ == '__main__':
    if not os.path.isdir(OUTDIR):
        os.mkdir(OUTDIR)
    flist = glob("procimgdir/*png")
    for imgpath in tqdm(flist):
        fn = os.path.basename(imgpath)
        cropfn = os.path.join(OUTDIR, fn)
        cropImage(imgpath, cropfn)

