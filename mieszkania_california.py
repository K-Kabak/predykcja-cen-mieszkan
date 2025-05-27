
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Wczytanie danych
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MedHouseVal'] = housing.target

# --- Wizualizacja danych ---
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Macierz korelacji cech (California Housing)')
plt.tight_layout()
plt.show()

# --- Przygotowanie danych ---
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- Trenowanie modelu ---
model = RandomForestRegressor(random_state=42)
model.fit(X_train_scaled, y_train)

# --- Predykcje ---
y_pred = model.predict(X_test_scaled)

# --- Wykres predykcji ---
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel('Wartości rzeczywiste (MedHouseVal)')
plt.ylabel('Wartości przewidywane')
plt.title('Porównanie rzeczywistych i przewidywanych cen mieszkań (California)')
plt.tight_layout()
plt.show()

# --- Ocena modelu ---
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n📊 Metryki modelu:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# --- Podsumowanie ---
print("\n✅ Podsumowanie:")
print("- Algorytm: Random Forest Regressor")
print("- Dane: California Housing Dataset")
print(f"- MAE ~ {round(mae, 2)} | R² ~ {round(r2, 2)}")
print("- Model dobrze dopasowany. Można dodatkowo poprawić jakość przez tunowanie parametrów.")
