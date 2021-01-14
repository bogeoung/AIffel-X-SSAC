import pandas as pd
import urllib.request
# % matplotlib inline
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from collections import Counter
from konlpy.tag import Mecab

train_data = pd.read_table('~/aiffel/sentiment_classification/ratings_train.txt')
test_data = pd.read_table('~/aiffel/sentiment_classification/ratings_test.txt')

# print(train_data.head())

tokenizer = Mecab()
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']


def load_data(train_data, test_data, num_words=10000):
    # [[YOUR CODE]]

    # 데이터의 중복 제거 및 NaN 결측치 제거
    train_data.drop_duplicates(subset=['document'], inplace=True)
    # subset은 중복데이터를 처리할 열을 입력, inplace는 메서드가 적용되는 원본 데이터를 변경할지 여부를 결정
    train_data = train_data.dropna(how='any')
    # how = 'any' -> NA(결측치)값이 존재하면 그 행이나 열을 drop함.
    # 참고 : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
    test_data.drop_duplicates(subset=['document'], inplace=True)
    test_data = test_data.dropna(how='any')

    # 한국어 토크나이저로 토큰화 및 불용어 제거
    X_train = []
    for sentence in train_data['document']:
        temp_X = tokenizer.morphs(sentence)
        # Mecab의 morphs 기능을 통해 형태소로 구문분석
        # 참고 : https://konlpy-ko.readthedocs.io/ko/v0.4.3/api/konlpy.tag/
        temp_X = [word for word in temp_X if not word in stopwords]
        # 구분한 형태소 중 stopwords에 존재하지 않는 것만 temp_X에 저장
        X_train.append(temp_X)
    # ("Xtrain", X_train) # 이거 잘 출력됨

    X_test = []
    for sentence in test_data['document']:
        temp_X = tokenizer.morphs(sentence)
        temp_X = [word for word in temp_X if not word in stopwords]
        X_test.append(temp_X)

    # ?? concatenate는 배열을 붙이는 거라는 데 하나로 어떻게 합치지?
    # ndarray클래스이 tolist() 메소드를 이용해 list 객체를 구하여 words에 저장.
    words = np.concatenate(X_train).tolist()
    # 리스트의 나온 횟수만큼 counter 리스트에 저장
    counter = Counter(words)
    # 데이터 개수가 많은 순으로 정렬된 배열을  리턴하는 most_common사용
    # 참고 : https://www.daleseo.com/python-collections-counter/
    counter = counter.most_common(10000 - 4)
    # 사전에 정의되 있던 인덱스 + 문자열에서 추출한 문자를
    vocab = ['<PAD>', '<BOS>', '<UNK>', '<UNUSED>'] + [key for key, _ in counter]

    # 리스트 컨프리헨션 사용헤서 사전 word_to_index구성
    # 참고 : https://wikidocs.net/16045, https://wikidocs.net/16, https://wikidocs.net/22797
    # word_to_index라는 리스트의 key로 word를 넣음.
    # for index, word in enumerate(vocab) -> vocab에 있는 index, word 만큼 반복
    word_to_index = {word: index for index, word in enumerate(vocab)}

    def wordlist_to_indexlist(wordlist):
        return [word_to_index[word] if word in word_to_index else word_to_index['<UNK>'] for word in wordlist]

    X_train = list(map(wordlist_to_indexlist, X_train))
    X_test = list(map(wordlist_to_indexlist, X_test))

    return X_train, np.array(list(train_data['label'])), X_test, np.array(list(test_data['label'])), word_to_index


X_train, y_train, X_test, y_test, word_to_index = load_data(train_data, test_data)

index_to_word = {index:word for word, index in word_to_index.items()}

# 문장 1개를 활용할 딕셔너리와 함께 주면, 단어 인덱스 리스트 벡터로 변환해 주는 함수입니다.
# 단, 모든 문장은 <BOS>로 시작하는 것으로 합니다.
def get_encoded_sentence(sentence, word_to_index):
    return [word_to_index['<BOS>']]+[word_to_index[word] if word in word_to_index else word_to_index['<UNK>'] for word in sentence.split()]

# 여러 개의 문장 리스트를 한꺼번에 단어 인덱스 리스트 벡터로 encode해 주는 함수입니다.
def get_encoded_sentences(sentences, word_to_index):
    return [get_encoded_sentence(sentence, word_to_index) for sentence in sentences]

# 숫자 벡터로 encode된 문장을 원래대로 decode하는 함수입니다.
def get_decoded_sentence(encoded_sentence, index_to_word):
    return ' '.join(index_to_word[index] if index in index_to_word else '<UNK>' for index in encoded_sentence[1:])  #[1:]를 통해 <BOS>를 제외

# 여러개의 숫자 벡터로 encode된 문장을 한꺼번에 원래대로 decode하는 함수입니다.
def get_decoded_sentences(encoded_sentences, index_to_word):
    return [get_decoded_sentence(encoded_sentence, index_to_word) for encoded_sentence in encoded_sentences]


# 3. 모델 구성을 위한 데이터 분석 및 가공
total_data_text = list(X_train) + list(X_test)
num_tokens = [len(tokens) for tokens in total_data_text]
num_tokens = np.array(num_tokens)
#print('문장길이 평균 : ', np.mean(num_tokens))
#print('문장길이 최대 : ', np.max(num_tokens))
#print('문장길이 표준편차 : ', np.std(num_tokens))
max_tokens = np.mean(num_tokens) + 2 * np.std(num_tokens)
maxlen = int(max_tokens)
#print('pad_sequences maxlen : ', maxlen)
#print('전체 문장의 {}%가 maxlen 설정값 이내에 포함됩니다. '.format(np.sum(num_tokens < max_tokens) / len(num_tokens)))
# 4. 모델 구성 및 validation set 구성
# 성능을 위해 post -> pre로 수정
x_train = keras.preprocessing.sequence.pad_sequences(X_train,
                                                        value=word_to_index["<PAD>"],
                                                        padding='pre', # 혹은 'pre'
                                                        maxlen=maxlen)

x_test = keras.preprocessing.sequence.pad_sequences(X_test,
                                                       value=word_to_index["<PAD>"],
                                                       padding='pre', # 혹은 'pre'
                                                       maxlen=maxlen)


# 5. 모델 훈련 개시
vocab_size = 10000    # 어휘 사전의 크기입니다(10,000개의 단어)
word_vector_dim = 16  # 워드 벡터의 차원수 (변경가능한 하이퍼파라미터)

# model 설계 - 딥러닝 모델 코드를 직접 작성해 주세요.
model = keras.Sequential()
# [[YOUR CODE]]
model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, word_vector_dim, input_shape=(None,)))
model.add(keras.layers.LSTM(8))
model.add(keras.layers.Dense(8, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))
# model.summary()
# validation set 10000건 분리
x_val = x_train[:10000]
y_val = y_train[:10000]

# validation set을 제외한 나머지 15000건
partial_x_train = x_train[10000:]
partial_y_train = y_train[10000:]

print(partial_x_train.shape)
print(partial_y_train.shape)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

epochs = 10  # 몇 epoch를 훈련하면 좋을지 결과를 보면서 바꾸어 봅시다.

history = model.fit(partial_x_train, partial_y_train, epochs=epochs,
                    batch_size=512, validation_data=(x_val, y_val), verbose=1)
results = model.evaluate(x_test,  y_test, verbose=2)

print(results)
# 6. Loss, Accuracy 그래프 시각화, # 7. 학습된 Embedding 레이어 분석
history_dict = history.history
print(history_dict.keys()) # epoch에 따른 그래프를 그려볼 수 있는 항목들

import matplotlib.pyplot as plt

acc = history_dict['acc']
val_acc = history_dict['val_acc']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

# "bo"는 "파란색 점"입니다
plt.plot(epochs, loss, 'bo', label='Training loss')
# b는 "파란 실선"입니다
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.clf()   # 그림을 초기화합니다

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()


# 8. 한국어 Word2Vec 임베딩 활용하여 성능 개선
