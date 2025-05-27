# 🧠 Projekt ML: Predykcja cen mieszkań (California Housing)

Projekt wykonany w ramach nauki uczenia maszynowego. Celem było stworzenie modelu regresyjnego, który przewiduje ceny mieszkań w Kalifornii na podstawie cech demograficznych i geograficznych.

---

## 📌 Cel projektu

Zbudowanie modelu regresji, który na podstawie danych wejściowych (np. średni dochód, liczba pokoi, lokalizacja) potrafi oszacować cenę mieszkania.

---

## 🗂️ Zbiór danych

- `California Housing Dataset` – wbudowany w `scikit-learn`
- Zawiera informacje o:
  - średnich dochodach (`MedInc`)
  - liczbie pokoi i sypialni
  - gęstości zaludnienia
  - współrzędnych geograficznych (`Latitude`, `Longitude`)
  - oraz kolumnie docelowej `MedHouseVal` – mediana wartości domów

---

## 🧰 Użyte technologie i biblioteki

| Biblioteka | Zastosowanie |
|------------|--------------|
| `pandas`, `numpy` | manipulacja i analiza danych |
| `matplotlib`, `seaborn` | wizualizacja danych |
| `scikit-learn` | podział danych, skalowanie, model Random Forest, metryki |

---

## ⚙️ Przebieg projektu

1. **Wczytanie i analiza danych**
2. **Wizualizacja zależności (macierz korelacji)**
3. **Podział danych i standaryzacja**
4. **Trenowanie modelu: `RandomForestRegressor`**
5. **Predykcja i wykres porównania**
6. **Ocena modelu metrykami:**
   - Mean Absolute Error (MAE)
   - R² Score

---

## 📈 Wyniki modelu

- **Mean Absolute Error (MAE):** ~0.5
- **R² Score:** ~0.8
- Model dobrze odwzorowuje dane testowe i nadaje się do praktycznych zastosowań regresyjnych.

---

## 📊 Wizualizacje

### 🔹 Macierz korelacji
Pokazuje zależności między cechami i ceną mieszkań.

![Macierz korelacji](images/macierz_korelacji.png)

---

### 🔹 Predykcja vs rzeczywistość
Porównanie przewidywanych i rzeczywistych cen.

![Predykcja vs rzeczywistość](images/scatter_pred_vs_actual.png)

---

## 📁 Pliki w repozytorium

| Plik | Opis |
|------|------|
| `mieszkania_california.py` | Skrypt do uruchomienia lokalnie |
| `projekt_california_colab.ipynb` | Notebook gotowy do użycia w Google Colab |
| `README.md` | Opis projektu |
| `images/` | Folder z grafikami do wizualizacji wyników |

---

## 👨‍💻 Autor

**Kacper Kabak**  
Student zainteresowany sztuczną inteligencją i analizą danych.

---

## 📎 Możliwe ulepszenia

- Grid Search / Randomized Search do tunowania modelu
- Porównanie z innymi modelami (XGBoost, GradientBoosting)
- Zastosowanie innych zbiorów danych (np. Ames Housing)

---

## ✅ Status

✔️ Projekt zakończony i gotowy do prezentacji / publikacji

