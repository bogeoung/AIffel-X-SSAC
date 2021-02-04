from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix

breast = load_breast_cancer()
breast_data = breast.data
breast_label = breast.target

# (3) train, test 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(breast_data,
                                                    breast_label,
                                                    test_size=0.2,
                                                    random_state=7)

# (4) 모델 학습 및 예측
decision_tree = DecisionTreeClassifier(random_state=32)
decision_tree.fit(X_train, y_train)
y_pred = decision_tree.predict(X_test)
print("decision tree:\n", confusion_matrix(y_test, y_pred),"\n")


random_forest = RandomForestClassifier(random_state=32)
random_forest.fit(X_train, y_train)
y_pred = random_forest.predict(X_test)
print("random_forest:\n ", confusion_matrix(y_test, y_pred),"\n")

SupportVectorMachine = svm.SVC(kernel='linear')
SupportVectorMachine.fit(X_train, y_train)
y_pred = SupportVectorMachine.predict(X_test)
print("SupportVectorMachine: \n", confusion_matrix(y_test, y_pred),"\n")


sgd_model = SGDClassifier()
sgd_model.fit(X_train, y_train)
y_pred = sgd_model.predict(X_test)
print("sgd_model: \n", confusion_matrix(y_test, y_pred),"\n")


'''
실제 암환자 인데 아니라고 판단하는 비율이 적어야 한다고 생각하기 때문에, recall이 가장 적합한 지표라고 생각한다.
'''