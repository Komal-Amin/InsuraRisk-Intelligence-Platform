import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import pickle


# Load dataset
df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')


# Features and target
X = df[['claim_amount', 'fraud_flag']]
y = df['premium']


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create GLM-style regression model
model = LinearRegression()

model.fit(X_train, y_train)


# Predictions
predictions = model.predict(X_test)


# Metrics
print("R2 Score:", r2_score(y_test, predictions))
print("MAE:", mean_absolute_error(y_test, predictions))


# Save model
with open('models/ml/glm_pricing.pkl', 'wb') as f:
    pickle.dump(model, f)

print("GLM pricing model saved.")