import os
import pyscreenshot as ImageGrab
from detect import crop_save
"""
Enter -> continue
q|Q -> exit
 """

FULLSCREEN = "fullscreen.png"
OUTDIR = "procimgdir"
#if os.path.isdir(OUTDIR):
#    shutil.rmtree(OUTDIR)
os.makedirs(OUTDIR, exist_ok=True)

def main():
    tagNum = int(input("start #: "))
    tag0 = tagNum
    autoRect = True
    while True:
        capCont = input("Q[quit] | EZ[hard] {:>3}: ".format(tagNum)).strip()
        if capCont in ('q', 'Q'):
            break
        elif capCont in ('ez', 'EZ'):
            autoRect = False
        else:
            autoRect = True

        # grab fullscreen
        im = ImageGrab.grab()
        # # save image file
        im.save(FULLSCREEN)
        if capCont == 'ez':
            autoRect = False
        crop_save(FULLSCREEN, os.path.join(OUTDIR, str(tagNum) + '.png'), auto=autoRect)
        tagNum = tagNum + 1

    print('total images: {}'.format(tagNum - tag0 + 1))

if __name__ == "__main__":
    main()
