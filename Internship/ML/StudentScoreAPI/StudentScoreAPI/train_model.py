import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load the dataset
df = pd.read_csv("student_performance_dataset.csv")

# 2. Remove ID column; it is not useful for prediction
df = df.drop(columns=["student_id"])

# 3. Separate inputs and target
X = df.drop(columns=["final_exam_score"])
y = df["final_exam_score"]

# 4. Convert gender categories into numeric columns
X = pd.get_dummies(X, columns=["gender"], dtype=int)

# 5. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train Multiple Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Evaluate the model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

metrics = {
    "MAE": round(float(mae), 2),
    "MSE": round(float(mse), 2),
    "RMSE": round(float(rmse), 2),
    "R2": round(float(r2), 4)
}

print("Model Evaluation")
print("MAE:", metrics["MAE"])
print("MSE:", metrics["MSE"])
print("RMSE:", metrics["RMSE"])
print("R2 Score:", metrics["R2"])

# 8. Save model, column names, and metrics
joblib.dump(
    {
        "model": model,
        "columns": X.columns.tolist(),
        "metrics": metrics
    },
    "student_model.joblib"
)

print("Model saved as student_model.joblib")
