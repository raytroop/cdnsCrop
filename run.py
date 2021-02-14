import os
import shutil
import pyscreenshot as ImageGrab
import cv2
from detect import crop_save

FULLSCREEN = "fullscreen.png"
OUTDIR = "procimgdir"
if os.path.isdir(OUTDIR):
    shutil.rmtree(OUTDIR)
os.mkdir(OUTDIR)

def main():
    tagNum = input("please input the start ID: ")
    proc = input("capture now(y|q): ").strip()
    while proc == 'y' or proc == 'Y':
        # grab fullscreen
        im = ImageGrab.grab()
        # # save image file
        im.save(FULLSCREEN)
        crop_save(FULLSCREEN, os.path.join(OUTDIR, tagNum + '.png'))
        tagNum = str(int(tagNum) + 1)
        proc = input("capture now(y|q): ").strip()


if __name__ == "__main__":
    main()
