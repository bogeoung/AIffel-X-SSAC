#(1) 필요한 모듈 import 하기
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

#(2) 데이터 준비, (3) 데이터 이해하기
wine = load_wine()
wine_data = wine.data
wine_label = wine.target



# (4) train, test 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(wine_data,
                                                    wine_label,
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

'''
참고 : https://www.javaer101.com/ko/article/1011753.html
y_test에 있는 레이블이 y_pred에 없는 경우, UndefinedMetricWarning가 나옴.
따라서 없는 레이블에 대해서 계산할 F-score가 없어 F-score가 0.0으로 간주됨. 
하지만 출력된 avg에 F-score가 0인 것이 포함되어 있기 때문에 이를 고려해야한다고 경고를 표시하는 것임.

이 알림을 받고 싶지 않으면 다음 2줄을 추가 하면 됨
import warnings 
warnings.filterwarnings('always')  # "error", "ignore", "always", "default", "module" or "once"
'''


# 5. Logistic Regression
logistic_model = LogisticRegression(solver='lbfgs', max_iter=10000) #ConvergenceWarning: lbfgs failed to converge 에러가 나서 추가함.
logistic_model.fit(X_train, y_train)
y_pred = sgd_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("logistic_model: \n", classification_report(y_test, y_pred))
print("accuracy : ", accuracy, "\n")

'''
참고 : https://datascienceschool.net/03%20machine%20learning/09.01%20%EB%B6%84%EB%A5%98%EC%9A%A9%20%EC%98%88%EC%A0%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0.html
와인 데이터를 찾아보니 와인의 화학성분이 데이터 내에 포함되어 있었다.
그 중 알콜을 마시면 안되는 사람이 (ex. 미성년자) 알콜을 마시게 되는 것처럼
음성을 양성으로 잘못판단하면 안된다 생각하여 precision이 높은 분류기가 좋은 것이라 생각한다.
'''
