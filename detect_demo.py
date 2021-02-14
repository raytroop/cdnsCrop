import numpy as np
import cv2

img = cv2.imread('shapes.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 254, 255, 0)
contours, h = cv2.findContours(thresh, 1, 2)

maxArea = 0.0
maxApprox = None

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        print("square")
        print(cnt)
        print(approx)
        curArea = abs(approx[0][0][0] - approx[2][0][0]) * \
            abs(approx[0][0][1] - approx[2][0][1])
        # print(curArea)
        if curArea > maxArea:
            maxArea = curArea
            maxApprox = approx
    else:
        continue

print("max area: {}".format(maxArea))
print(maxApprox)
x0, y0 = maxApprox[0][0]
x1, y1 = maxApprox[2][0]
# cv2.drawContours(img, [maxApprox], 0, (0, 0, 255), -1)

print(img.shape)
cv2.imshow('img', img[y0:y1, x0:x1, :])
cv2.waitKey(0)
cv2.destroyAllWindows()

