import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Librerías cargadas correctamente.")
df = pd.read_csv('Life Expectancy Data.csv')
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas.")

# 2️⃣ Explorar los datos
df.head()
df.info()
df.describe()

# 3️⃣ Limpiar datos
df['Life expectancy'].fillna(df['Life expectancy'].mean(), inplace=True)
df.drop_duplicates(inplace=True)
df.info()


# 4️⃣ Filtrar y agrupar
df_ecuador = df[df['Country'] == 'Ecuador']
avg_life_by_region = df.groupby('Region')['Life expectancy'].mean().sort_values(ascending=False)

# 5️⃣ Visualizar
plt.figure(figsize=(10,6))
sns.lineplot(data=df_ecuador, x='Year', y='Life expectancy', marker='o')
plt.title('Esperanza de Vida en Ecuador')
plt.show()

# Barras (Regiones)
avg_life_by_region.plot(kind='bar', color=sns.color_palette('coolwarm', len(avg_life_by_region)))
plt.title('Esperanza de Vida Promedio por Región')
plt.show()


# Dispersión (PIB vs. Vida)
df_2014 = df[df['Year'] == 2014].dropna(subset=['GDP', 'Life expectancy'])
plt.figure(figsize=(10,7))
sns.scatterplot(data=df_2014, x='GDP', y='Life expectancy', hue='Region', alpha=0.7)
plt.xscale('log')
plt.title('PIB vs. Esperanza de Vida (2014)')
plt.show()
