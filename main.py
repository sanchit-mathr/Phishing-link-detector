import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Load the data
data = pd.read_csv('phishing_links.csv')

# Perform preprocessing tasks
data = data.dropna()
X = data.drop('label', axis=1)
y = data['label']

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the algorithms
logreg = LogisticRegression()
dtree = DecisionTreeClassifier()
svm = SVC(probability=True)
rf = RandomForestClassifier()
xgb = XGBClassifier()
mlp = MLPClassifier()

# Train the algorithms
for clf in [logreg, dtree, svm, rf, xgb, mlp]:
    clf.fit(X_train, y_train)

# Evaluate the performance of each algorithm on the test set
for clf in [logreg, dtree, svm, rf, xgb, mlp]:
    y_pred = clf.predict(X_test)
    print("\n", clf.__class__.__name__)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1-score:", f1_score(y_test, y_pred))
    print("AUC-ROC:", roc_auc_score(y_test, y_pred))
