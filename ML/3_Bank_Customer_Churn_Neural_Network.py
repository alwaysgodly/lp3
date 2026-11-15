"""
B3 - Bank Customer Churn Prediction using a Neural Network
Dataset expected: Churn_Modelling.csv
Target column: Exited (0 = stayed, 1 = churned)
Uses sklearn MLPClassifier as a feed-forward neural network.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

FILE = "Churn_Modelling.csv"
if not os.path.exists(FILE):
    raise FileNotFoundError("Place Churn_Modelling.csv in the same folder as this script.")

df = pd.read_csv(FILE)
print(df.head())
print("\nMissing values:\n", df.isnull().sum())

target = "Exited"
if target not in df.columns:
    raise ValueError("Dataset must contain target column 'Exited'.")

# Remove identifier/name columns if present.
df = df.drop(columns=[c for c in ["RowNumber", "CustomerId", "Surname"] if c in df.columns])
X = df.drop(columns=[target])
y = df[target]

categorical = X.select_dtypes(include=["object", "category"]).columns.tolist()
numeric = X.select_dtypes(include=["number", "bool"]).columns.tolist()

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric),
    ("categorical", categorical_pipeline, categorical)
])

model = Pipeline([
    ("preprocess", preprocessor),
    ("neural_network", MLPClassifier(
        hidden_layer_sizes=(16, 8),
        activation="relu",
        solver="adam",
        max_iter=300,
        random_state=42,
        early_stopping=True
    ))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("\nAccuracy:", round(accuracy_score(y_test, predictions), 4))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions, zero_division=0))

ConfusionMatrixDisplay.from_predictions(y_test, predictions)
plt.title("Bank Customer Churn - Confusion Matrix")
plt.tight_layout()
plt.show()
