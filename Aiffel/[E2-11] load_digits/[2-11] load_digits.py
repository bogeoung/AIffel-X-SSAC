#(1) 필요한 모듈 import 하기
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

#(2) 데이터 준비, (3) 데이터 이해하기
digits = load_digits()
digits_data = digits.data
digits_label = digits.target

# (4) train, test 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(digits_data,
                                                    digits_label,
                                                    test_size=0.2,
                                                    random_state=7)

# (5) 다양한 모델로 학습시켜 보기
# 1. Decision Tree
decision_tree = DecisionTreeClassifier(random_state=32)
decision_tree.fit(X_train, y_train)
y_pred = decision_tree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("decision tree:\n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy, "\n")

# 2. Random Forest
random_forest = RandomForestClassifier(random_state=32)
random_forest.fit(X_train, y_train)
y_pred = random_forest.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("random_forest:\n ", classification_report(y_test, y_pred))
print("accuracy : ", accuracy, "\n")

# 3. SVM
SupportVectorMachine = svm.SVC(kernel='linear')
SupportVectorMachine.fit(X_train, y_train)
y_pred = SupportVectorMachine.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("SupportVectorMachine: \n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy, "\n")

# 4. SGD Classifier
sgd_model = SGDClassifier()
sgd_model.fit(X_train, y_train)
y_pred = sgd_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("sgd_model: \n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy, "\n")

# 5. Logistic Regression
logistic_model = LogisticRegression(solver='lbfgs', max_iter=10000) #ConvergenceWarning: lbfgs failed to converge 에러가 나서 추가함.
logistic_model.fit(X_train, y_train)
y_pred = sgd_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("logistic_model: \n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy, "\n")

'''
필적 확인에 사용된다고 가정했을 때, 이 필적이 그 사람인지 맞는지 판단하는 것도 중요하지만 그 사람이 아니라는 것을 판단하는 것도 중요할 것이다.
따라서 얼만큼 Ture를 Ture라고 옳게 예측하고, False를 False라고 예측한 것인지를 보여주는 accuracy가 가장 적합한 지표라고 생각했다.
추가적으로 데이터의 편향이 있는 경우, F1 score이 더 적합할 것이다.
'''