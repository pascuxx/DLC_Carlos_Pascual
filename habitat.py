import pandas as pd
import mataplotlib.pyplot as plt

df_mush = pd.read_csv("mushrooms.csv")
# gráfico de barras con los porcentajes de habtitats diferentes
df_mush['habitat'].value_counts().plot(kind='bar', color = "orange")
plt.xlabel("Habitat")
plt.ylabel("%")
plt.title("Porcentaje de cada habitat en el dataset")
plt.savefig("por_habitat.png", dpi=300, bbox_inches='tight') 
plt.show()
