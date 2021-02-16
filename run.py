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
    tagNum = int(input("please input the start ID: "))
    tag0 = tagNum
    procNow = input("Start Capture ? (Q to quit): ").strip()

    while procNow != 'q' or procNow != 'Q':
        # grab fullscreen
        im = ImageGrab.grab()
        # # save image file
        im.save(FULLSCREEN)
        crop_save(FULLSCREEN, os.path.join(OUTDIR, str(tagNum) + '.png'))
        capCont = input("capture now(Q to quit): ").strip()
        if capCont in ('q', 'Q'):
            break
        tagNum = tagNum + 1
    print('total images: {}'.format(tagNum - tag0 + 1))

if __name__ == "__main__":
    main()
