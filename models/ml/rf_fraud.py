import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')

X = df[['premium', 'claim_amount']]
y = df['fraud_flag']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

with open('models/ml/rf_fraud.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Random Forest fraud model saved to models/ml/rf_fraud.pkl")