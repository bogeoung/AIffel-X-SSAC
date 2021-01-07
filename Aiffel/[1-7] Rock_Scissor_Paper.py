from PIL import Image
import os, glob
import numpy as np
import tensorflow as tf
from tensorflow import keras

def resize_data():
    target_size = (28, 28)

    image_dir_path = os.getenv("HOME") + "/aiffel/rock_scissor_paper_merge_train/scissor"
    print("이미지 디렉토리 경로: ", image_dir_path)
    images = glob.glob(image_dir_path + "/*.jpg")
    for img in images:
        old_img = Image.open(img)
        new_img = old_img.resize(target_size, Image.ANTIALIAS)
        new_img.save(img, "JPEG")
    print("가위 이미지 resize 완료!\n")

    image_dir_path = os.getenv("HOME") + "/aiffel/rock_scissor_paper_merge_train/rock"
    print("이미지 디렉토리 경로: ", image_dir_path)
    images = glob.glob(image_dir_path + "/*.jpg")
    for img in images:
        old_img = Image.open(img)
        new_img = old_img.resize(target_size, Image.ANTIALIAS)
        new_img.save(img, "JPEG")
    print("바위 이미지 resize 완료!\n")

    image_dir_path = os.getenv("HOME") + "/aiffel/rock_scissor_paper_merge_train/paper"
    print("이미지 디렉토리 경로: ", image_dir_path)
    images = glob.glob(image_dir_path + "/*.jpg")
    for img in images:
        old_img = Image.open(img)
        new_img = old_img.resize(target_size, Image.ANTIALIAS)
        new_img.save(img, "JPEG")
    print("이미지 resize 완료!\n")

def load_data(img_path):
    # 가위 : 0, 바위 : 1, 보 : 2
    number_of_data = 3000  # 가위바위보 이미지 개수 총합에 주의하세요.
    img_size = 28
    color = 3
    # 이미지 데이터와 라벨(가위 : 0, 바위 : 1, 보 : 2) 데이터를 담을 행렬(matrix) 영역을 생성합니다.
    imgs = np.zeros(number_of_data * img_size * img_size * color, dtype=np.int32).reshape(number_of_data, img_size,
                                                                                          img_size, color)
    labels = np.zeros(number_of_data, dtype=np.int32)

    idx = 0
    for file in glob.iglob(img_path + '/scissor/*.jpg'):
        img = np.array(Image.open(file), dtype=np.int32)
        imgs[idx, :, :, :] = img  # 데이터 영역에 이미지 행렬을 복사
        labels[idx] = 0  # 가위 : 0
        idx = idx + 1

    for file in glob.iglob(img_path + '/rock/*.jpg'):
        img = np.array(Image.open(file), dtype=np.int32)
        imgs[idx, :, :, :] = img  # 데이터 영역에 이미지 행렬을 복사
        labels[idx] = 1  # 바위 : 1
        idx = idx + 1

    for file in glob.iglob(img_path + '/paper/*.jpg'):
        img = np.array(Image.open(file), dtype=np.int32)
        imgs[idx, :, :, :] = img  # 데이터 영역에 이미지 행렬을 복사
        labels[idx] = 2  # 보 : 2
        idx = idx + 1

    print("학습데이터(x_train)의 이미지 개수는", idx, "입니다.")
    return imgs, labels

def learning_design(model):
    n_channel_1 = 64
    n_channel_2 = 128
    n_dense = 32
    n_train_epoch = 10


    model.add(keras.layers.Conv2D(n_channel_1, (3, 3), activation='relu', input_shape=(28, 28, 3)))
    model.add(keras.layers.MaxPool2D(2, 2))
    model.add(keras.layers.Conv2D(n_channel_2, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(n_dense, activation='relu'))
    model.add(keras.layers.Dense(3, activation='softmax'))

    print('Model에 추가된 Layer 개수: ', len(model.layers))
    model.summary()

def learning(model, x_train_norm,y_train):
    print("Before Reshape - x_train_norm shape: {}".format(x_train_norm.shape))
    # print("Before Reshape - x_test_norm shape: {}".format(x_test_norm.shape))
    x_train_reshaped = x_train_norm.reshape(-1, 28, 28, 3)  # 데이터갯수에 -1을 쓰면 reshape시 자동계산됩니다.

    print("After Reshape - x_train_reshaped shape: {}".format(x_train_reshaped.shape))
    # print("After Reshape - x_test_reshaped shape: {}".format(x_test_reshaped.shape))
    keras.optimizers.Adam(lr=0.005, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
    model.compile(optimizer='Adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train_reshaped, y_train, epochs=10)

def test(model):
    image_dir_path = os.getenv("HOME") + "/aiffel/rock_scissor_paper_merge_test"
    (x_test, y_test) = load_data(image_dir_path)
    x_test_norm = x_test / 255.0  # 입력은 0~1 사이의 값으로 정규화

    print("x_test shape: {}".format(x_test.shape))
    print("y_test shape: {}".format(y_test.shape))

    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
    print("test_loss: {} ".format(test_loss))
    print("test_accuracy: {}".format(test_accuracy))

def main():
    image_dir_path = os.getenv("HOME") + "/aiffel/rock_scissor_paper"
    resize_data()
    (x_train, y_train) = load_data(image_dir_path)
    x_train_norm = x_train / 255.0  # 입력은 0~1 사이의 값으로 정규화

    print("x_train shape: {}".format(x_train.shape))
    print("y_train shape: {}".format(y_train.shape))

    model = keras.models.Sequential()
    learning_design(model)
    learning(model,x_train_norm,y_train)
    test(model)



if __name__ == "__main__":
    main()


