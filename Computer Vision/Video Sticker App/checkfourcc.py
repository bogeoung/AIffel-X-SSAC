import cv2

vc = cv2.VideoCapture('./images/video2.mp4')

fourcc = int(vc.get(cv2.CAP_PROP_FOURCC))
fourcc_str = "%c%c%c%c"%(fourcc & 255, (fourcc >> 8) & 255, (fourcc >> 16) & 255, (fourcc >> 24) & 255)
print ("CAP_PROP_FOURCC: ", fourcc_str)


