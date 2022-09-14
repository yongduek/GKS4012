import cv2  # opencv
import numpy as np 

print("Hello")  # powershell

im = cv2.imread("훈민정음.jpg")

print(im.shape, type(im), im.dtype) # uint8 : unsigned integer 8 bits
s = im.shape

while True:
    r = 100
    c = 200
    # im[r, c, 0] = 0 # blue
    # im[r, c, 1] = 0   # g
    # im[r, c, 2] = 255   # r
    im[r, 200:500, :] = (0, 0, 255)
    im[10:333, c, :] = (0, 255, 0)

    # random dots
    r = np.random.randint(s[0])
    c = np.random.randint(s[1])
    color = np.random.randint(0, 256, 3)
    im[r, c] = color 
    
    sr = np.random.randint(s[0])
    sc = np.random.randint(s[1])
    er = np.random.randint(s[0])
    ec = np.random.randint(s[1])
    thick = np.random.randint(2, 5)

    # cv2.line(im, (sr, sc), (er, ec), (color[0], color[1], color[2]), thick)
    # cv2.line(im, (sc, sr), (ec, er), (255, 0, 0), thick)
    cv2.line(im, (sc, sr), (ec, er), (int(color[0]), int(color[1]), int(color[2])), thick)

    cv2.imshow("window name", im)
    ch = cv2.waitKey(1) # 1000 mili second = 1 second
    if ch == 27: # ESC key
        break 
#