from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "edad": [25, 45, 35, 50, 23, 40, 60, 48, 33, 55, 29, 44, 38, 22, 36, 52, 31, 49, 58, 27],
    "ingresos": [3000, 6000, 4000, 8000, 2500, 5000, 10000, 7200, 4200, 9000, 3100, 5800, 4700, 2400, 4500, 8500, 3300, 7600, 9800, 2800],
    "hijos": [0, 2, 1, 3, 0, 2, 4, 3, 1, 2, 0, 2, 1, 0, 1, 3, 1, 2, 3, 0],
    "deuda": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    "aprobado": [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df.drop("aprobado", axis=1)
y = df["aprobado"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

muestra = x_test.iloc[0].values.reshape(1, -1)
y_pred = model.predict(muestra)
print("Real:", y_test.iloc[0])
print("Predicción:", y_pred[0])

y_pred_all = model.predict(x_test)
print("--- REALES ---")
print(y_test.values)
print("--- PREDICCIONES ---")
print(y_pred_all)

print("Métricas del modelo")
print("Accuracy:", accuracy_score(y_test, y_pred_all))
print(classification_report(y_test, y_pred_all))

edades = [22, 25, 30, 35, 40, 45, 50, 55, 60, 62, 64, 70, 75, 80, 85]
ingresos = [1500, 1800, 2500, 3000, 3500, 3800, 4000, 4200, 4500, 4700, 5000, 5200, 5400, 5600, 6000]

plt.hist(edades, bins=8, edgecolor='black')

plt.show()

sns.scatterplot(x=edades, y=ingresos)

plt.show()

