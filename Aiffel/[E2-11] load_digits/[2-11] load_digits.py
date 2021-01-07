from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

digits = load_digits()
digits_data = digits.data
digits_label = digits.target

# (3) train, test 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(digits_data,
                                                    digits_label,
                                                    test_size=0.2,
                                                    random_state=7)

# (4) 모델 학습 및 예측
decision_tree = DecisionTreeClassifier(random_state=32)
decision_tree.fit(X_train, y_train)
y_pred = decision_tree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("decision tree:\n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy)

random_forest = RandomForestClassifier(random_state=32)
random_forest.fit(X_train, y_train)
y_pred = random_forest.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("random_forest:\n ", classification_report(y_test, y_pred))
print("accuracy : ", accuracy)

SupportVectorMachine = svm.SVC(kernel='linear')
SupportVectorMachine.fit(X_train, y_train)
y_pred = SupportVectorMachine.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("SupportVectorMachine: \n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy)

sgd_model = SGDClassifier()
sgd_model.fit(X_train, y_train)
y_pred = sgd_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("sgd_model: \n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy)

'''
가장 성능이 좋은 분류기는 0.96의 정확도를 낸 random_forest라고 생각한다.
이진 분류가 아닌이상 오차행렬로 정확도를 판단하긴 어렵다 생각해서, 
classification_report 값이 가장 성능이 좋다고 판단함.
'''