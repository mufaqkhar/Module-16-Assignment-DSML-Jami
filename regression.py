"""Educational simple linear regression baseline (BMI -> progression)."""
from pathlib import Path
import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

path = Path(__file__).parent / 'data' / 'diabetes_bmi.csv'
with path.open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
X = np.array([[float(r['bmi_standardized'])] for r in rows])
y = np.array([float(r['disease_progression']) for r in rows])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)
print(f'Rows: {len(y)}; training: {len(y_train)}; test: {len(y_test)}')
print(f'Intercept: {model.intercept_:.3f}; BMI coefficient: {model.coef_[0]:.3f}')
print(f'MAE: {mean_absolute_error(y_test, pred):.3f}')
print(f'RMSE: {np.sqrt(mean_squared_error(y_test, pred)):.3f}')
print(f'R2: {r2_score(y_test, pred):.3f}')
