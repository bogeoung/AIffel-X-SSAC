import dlib
import cv2

def img2sticker_orig(img_orig, img_sticker, detector_hog, landmark_predictor):
    # preprocess
    start = cv2.getTickCount()
    img_rgb = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)
    preprocess_time = (cv2.getTickCount() - start) / cv2.getTickFrequency() * 1000

    # detector
    start = cv2.getTickCount()
    dlib_rects = detector_hog(img_rgb, 0)
    if len(dlib_rects) < 1:
        return img_orig
    detection_time = (cv2.getTickCount() - start) / cv2.getTickFrequency() * 1000

    # landmark
    start = cv2.getTickCount()
    list_landmarks = []
    for dlib_rect in dlib_rects:
        points = landmark_predictor(img_rgb, dlib_rect)
        list_points = list(map(lambda p: (p.x, p.y), points.parts()))
        list_landmarks.append(list_points)
    landmark_time = (cv2.getTickCount() - start) / cv2.getTickFrequency() * 1000

    # head coord
    start = cv2.getTickCount()
    for dlib_rect, landmark in zip(dlib_rects, list_landmarks):
        x = landmark[30][0] # nose
        y = landmark[30][1] - dlib_rect.width()//2
        w = dlib_rect.width()
        h = dlib_rect.width()
        # x,y,w,h = [ele*2 for ele in [x,y,w,h]]
        break
    coord_time = (cv2.getTickCount() - start) / cv2.getTickFrequency() * 1000

    # sticker
    start = cv2.getTickCount()
    img_sticker = cv2.resize(img_sticker, (w,h), interpolation=cv2.INTER_NEAREST)

    refined_x = x - w // 2
    refined_y = y - h

    if refined_y < 0:
        img_sticker = img_sticker[-refined_y:]
        refined_y = 0

    img_bgr = img_orig.copy()
    sticker_area = img_bgr[refined_y:refined_y+img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]

    img_bgr[refined_y:refined_y+img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]] = \
        cv2.addWeighted(sticker_area, 1.0, img_sticker, 0.7, 0)
    sticker_time = (cv2.getTickCount() - start) / cv2.getTickFrequency() * 1000

    print (f'p:{preprocess_time:.1f}ms, d:{detection_time:.1f}ms, l:{landmark_time:.1f}ms, c:{coord_time:.1f}ms, s:{sticker_time:.1f}ms')

    return img_bgr

detector_hog = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('./models/shape_predictor_68_face_landmarks.dat')

vc = cv2.VideoCapture('./images/video2.mp4')
img_sticker = cv2.imread('./images/king.png')

vlen = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
print (vlen) # 비디오 프레임의 총 개수


for i in range(vlen):
    ret, img = vc.read()
    if ret == False:
        break
		
    ## 추가된 부분
    start = cv2.getTickCount()
    img_result = img2sticker_orig(img, img_sticker.copy(), detector_hog, landmark_predictor)
    time = (cv2.getTickCount() - start) / cv2.getTickFrequency() * 1000
    print ('[INFO] time: %.2fms'%time)
    
    cv2.imshow('show', img_result)
    key = cv2.waitKey(1)
    if key == 27:
        break

