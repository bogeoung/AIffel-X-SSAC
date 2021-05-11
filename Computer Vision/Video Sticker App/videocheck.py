import cv2

vc = cv2.VideoCapture('./images/video2.mp4')

vlen = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
print (vlen) # video length

for i in range(vlen):
    ret, img = vc.read()
    if ret == False:
        break

    cv2.imshow('show', img)
    key = cv2.waitKey(1)
    if key == 27:
        break
