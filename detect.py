import cv2


MINWIDTH = 500
MINHEIGHT = 500


def crop_save(srcimg, filename):
    img = cv2.imread(srcimg)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 254, 255, 0)
    contours, _ = cv2.findContours(thresh, 1, 2)

    maxArea = 0.0
    maxApprox = None

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            # print("square")
            # print(cnt)
            # print(approx)
            width = abs(approx[0][0][0] - approx[2][0][0])
            height = abs(approx[0][0][1] - approx[2][0][1])
            if width < MINWIDTH or height < MINHEIGHT:
                continue
            curArea = width * height
            # print(curArea)
            if curArea > maxArea:
                maxArea = curArea
                maxApprox = approx

    # print("max area: {}".format(maxArea))
    # print(maxApprox)
    x0, x1 = 489, 1750
    y0, y1 = 248, 956
    if maxApprox is not None:
        x0, y0 = maxApprox[0][0]
        x1, y1 = maxApprox[2][0]
    cv2.imwrite(filename, img[y0:y1, x0:x1, :])


if __name__ == "__main__":
    crop_save('shapes.png', 'shapes_crop.png')
