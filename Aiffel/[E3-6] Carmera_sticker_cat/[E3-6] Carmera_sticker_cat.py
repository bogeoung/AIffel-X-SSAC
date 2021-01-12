import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import dlib

# 이미지 처리를 위해 opencv와 노트북에 이미지 출력을 위한 matplogli을 읽어옴
my_image_path = os.getenv('HOME')+'/aiffel/camera_sticker/images/image.jpg'
img_bgr = cv2.imread(my_image_path)    #- OpenCV로 이미지를 읽어서
img_bgr = cv2.resize(img_bgr, (640, 360))    # 640x360의 크기로 Resize
img_show = img_bgr.copy()      #- 출력용 이미지 별도 보관

#언 opencv의 BGR설정
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# face detection을 위한 hog detector을 선언
# cv2.cvtColor(원본이미지, 색상변환코드) -> 이미지의 색상 공간을 변경
detector_hog = dlib.get_frontal_face_detector()   #- detector 선언

#detector을 이용해 얼굴의 bounding box추출
dlib_rects = detector_hog(img_rgb, 1)   #- (image, num of img pyramid)

# 찾은 얼굴 영역의 좌표를 띄우기
for dlib_rect in dlib_rects:
    l = dlib_rect.left()
    t = dlib_rect.top()
    r = dlib_rect.right()
    b = dlib_rect.bottom()

    cv2.rectangle(img_show, (l,t), (r,b), (0,255,0), 2, lineType=cv2.LINE_AA)

# 저장한 랜드마크 모델을 불러옴
model_path = os.getenv('HOME')+'/aiffel/camera_sticker/models/shape_predictor_68_face_landmarks.dat'
landmark_predictor = dlib.shape_predictor(model_path)

# landmakr_predictor을 통해 RGB 이미지와 dlib.rectangle을 입력받아 dlib.full_object_detection을 반환
list_landmarks = []
for dlib_rect in dlib_rects:
    points = landmark_predictor(img_rgb, dlib_rect)
    list_points = list(map(lambda p: (p.x, p.y), points.parts()))
    list_landmarks.append(list_points)

# 랜드마크를 출력
for landmark in list_landmarks:
    for idx, point in enumerate(list_points):
        cv2.circle(img_show, point, 2, (0, 255, 255), -1) # yellow

img_show_rgb = cv2.cvtColor(img_show, cv2.COLOR_BGR2RGB)

# 스티커 적용하기 위한 좌표 확인
for dlib_rect, landmark in zip(dlib_rects, list_landmarks):
    print (landmark[30]) # nose center index : 30
    x = landmark[30][0]
    y = landmark[30][1]
    w = dlib_rect.width()
    h = dlib_rect.width()
    print ('(x,y) : (%d,%d)'%(x,y))
    print ('(w,h) : (%d,%d)'%(w,h))


# 스티커를 resize함
sticker_path = os.getenv('HOME') + '/aiffel/camera_sticker/images/cat.png'
img_sticker = cv2.imread(sticker_path)    # cv2.imread("경로", mode)를 이용하여 이미지를 불러와 변수에 저장.
img_sticker = cv2.resize(img_sticker, (w, h))
print("이미지의 크기" , img_sticker.shape)

# 원본 이미지에 스티커 이미지 추가 위해서 x,y 좌표 조정
refined_x = x - w // 2  # left
refined_y = y - h // 2    # top
print ('refinded (x,y) : (%d,%d)'%(refined_x, refined_y))


# -y만큼 스티커를 crop하고, top의 y좌표를 원본 이미지의 경계 값으로 수정

# 원본 이미지에 스티커를 적용  & 출력
# 검정색 출력 위해 img_sticker == 1 을 지정 ?? 다른 숫자로 바꿔야 할듯
# np.where(조건식, x, y) -> 조건식과 일치하는 경우에는 x값을 반환, 일치하지 않은 경우에는 y값을 반환
sticker_area = img_show[refined_y:refined_y+img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]
img_show[refined_y : refined_y+img_sticker.shape[0], refined_x : refined_x+img_sticker.shape[1]] = \
    np.where(img_sticker==255,sticker_area,img_sticker).astype(np.uint8)

'''
unit8 : 양수만 표현 가능 0~255
pd.astype(dtype) # 모든 열의 데이터 타입을 변경

'''

# bounding box와 landmark 제거
sticker_area = img_bgr[refined_y:refined_y+img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]
img_bgr[refined_y:refined_y+img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]] = \
    np.where(img_sticker==255,sticker_area,img_sticker).astype(np.uint8)
plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
plt.show()
