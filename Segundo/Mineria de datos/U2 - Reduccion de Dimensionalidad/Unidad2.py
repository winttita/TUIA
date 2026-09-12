# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:54:17 2023
@author: flavio

UNIDAD 2 - Minería de Datos (TUIA, UNR)
Tema: técnicas de REDUCCIÓN DE DIMENSIONALIDAD (PCA, Isomap, t-SNE, UMAP)
aplicadas al dataset "wheat" (semillas de trigo, 3 variedades).

IDEA GENERAL DEL SCRIPT:
El dataset tiene varias columnas numéricas (features) que describen cada
semilla (área, perímetro, compacidad, etc.) más una columna 'category' que
indica la variedad (Kama, Rosa, Canadian). Como no podemos "ver" un espacio
de más de 3 dimensiones, usamos técnicas de reducción de dimensionalidad
para proyectar esos datos a 2D o 3D y así poder graficarlos y explorar
visualmente si las 3 variedades se separan en grupos reconocibles.

Este es un caso de USO NO SUPERVISADO de exploración/visualización: no se
entrena ningún clasificador; 'category' solo se usa para colorear los
puntos en el gráfico y ver si la estructura que encuentra el algoritmo
(sin mirar la etiqueta) coincide con las clases reales.
"""

# ---------------------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------------------
import numpy as np                      # operaciones numéricas / arrays
import pandas as pd                     # manejo de datos tabulares (DataFrame)
import time                             # medir cuánto tarda t-SNE (es lento)
import matplotlib.pyplot as plt         # graficos 2D/3D
from mpl_toolkits.mplot3d import Axes3D # habilita proyección 3D en matplotlib
import seaborn as sns                   # gráficos estadísticos "más lindos" sobre matplotlib

from sklearn.preprocessing import StandardScaler  # estandarizar features (media 0, var 1)
from sklearn.manifold import TSNE, Isomap         # métodos NO lineales de reducción
from sklearn.decomposition import PCA             # método LINEAL de reducción
from umap import UMAP                             # método NO lineal, más moderno que t-SNE/Isomap

# ---------------------------------------------------------------------------
# CARGA Y PREPARACIÓN DE DATOS
# ---------------------------------------------------------------------------

# Diccionario para traducir el código numérico de clase a un nombre legible.
# El dataset trae 'category' como 1/2/3; esto es solo para que los gráficos
# y leyendas se entiendan mejor (en vez de leyenda "1,2,3" tenemos nombres).
target_names = {
    1: 'Kama',
    2: 'Rosa',
    3: 'Canadian'
}

dataWheat = pd.read_csv("wheat.csv")
# .map() reemplaza cada valor de la columna 'category' usando el diccionario.
dataWheat['category'] = dataWheat['category'].map(target_names)

# Separamos FEATURES (X) de la ETIQUETA (y).
# axis=1 en drop() significa "borrar una columna" (axis=0 sería borrar filas).
xWheat = dataWheat.drop('category', axis=1)
yWheat = dataWheat['category']

# Chequeo rápido de BALANCE DE CLASES: cuántas semillas hay de cada variedad.
# Esto es un paso importante en minería de datos: si una clase tuviera muchas
# más muestras que otra, hay que tenerlo en cuenta (podría sesgar análisis
# posteriores, ej. modelos que "aprenden" a favorecer la clase mayoritaria).
sns.countplot(
    x='category',
    data=dataWheat)
plt.title('Wheat targets value count')
plt.show()

# ESTANDARIZACIÓN: StandardScaler transforma cada columna para que tenga
# media 0 y desvío estándar 1: z = (x - media) / desvío.
# ¿POR QUÉ es necesario? PCA, t-SNE, UMAP e Isomap se basan en DISTANCIAS
# o VARIANZAS entre puntos. Si una columna está en una escala mucho más
# grande que otra (ej. área en mm² vs. compacidad entre 0 y 1), esa columna
# dominaría el cálculo de distancias/varianza solo por su escala, no porque
# sea más "importante". Estandarizar pone a todas las variables en pie de
# igualdal antes de aplicar estos métodos.
xWheatScaled = StandardScaler().fit_transform(xWheat)

""" PCA """
# PCA (Principal Component Analysis / Análisis de Componentes Principales)
# es un método LINEAL: busca nuevas direcciones (combinaciones lineales de
# las variables originales) que capturen la MÁXIMA VARIANZA posible de los
# datos. La primera componente (PC1) es la dirección de mayor varianza, la
# segunda (PC2) la siguiente dirección de mayor varianza que sea ortogonal
# (perpendicular) a la primera, y así sucesivamente.
#
# n_components=3 le decimos que nos quedamos con las 3 primeras componentes
# principales (en vez de las 7 columnas originales del dataset).
pca = PCA(n_components=3)

# fit_transform() hace dos cosas en un solo paso:
#  1) fit: calcula las direcciones principales a partir de los datos
#  2) transform: proyecta los datos originales sobre esas direcciones
pcaFeatures = pca.fit_transform(xWheatScaled)

print('Shape before PCA: ', xWheatScaled.shape)  # (n_muestras, n_features_original)
print('Shape after PCA: ', pcaFeatures.shape)    # (n_muestras, 3) -> redujimos dimensiones

# Armamos un DataFrame con las 3 componentes para poder graficar y explorar
pcaWheat = pd.DataFrame(
    data=pcaFeatures,
    columns=['PC1', 'PC2', 'PC3'])

# Volvemos a agregar la etiqueta real (solo para VISUALIZAR, no para entrenar)
pcaWheat['category'] = yWheat.to_numpy()

pcaWheat

# explained_variance_: cuánta varianza (en unidades absolutas) captura cada
# componente. Nos dice "cuánta información conserva" cada nueva dimensión.
pca.explained_variance_

# singular_values_: valores singulares de la descomposición SVD que PCA usa
# internamente (están relacionados matemáticamente con explained_variance_).
pca.singular_values_

# SCREE PLOT: gráfico de barras con la varianza explicada por cada
# componente, más una curva de varianza EXPLICADA ACUMULADA (cumsum).
# Sirve para decidir CUÁNTAS componentes conviene conservar: se busca el
# "codo" de la curva, o el punto donde la acumulada ya cubre, por ejemplo,
# el 90-95% de la varianza total.
plt.bar(
    range(1, len(pca.explained_variance_) + 1), pca.explained_variance_)

plt.plot(
    range(1, len(pca.explained_variance_) + 1),
    np.cumsum(pca.explained_variance_),
    c='red',
    label='Cumulative Explained Variance')

plt.legend(loc='upper left')
plt.xlabel('Number of components')
plt.ylabel('Explained variance (eignenvalues)')
plt.title('Scree plot')

plt.show()

# Graficamos las semillas en el plano PC1-PC2 (2 primeras componentes),
# coloreando por variedad real, para ver si PCA ya alcanza a separar clases
# usando solo 2 dimensiones en vez de las 7 originales.
sns.set()
sns.lmplot(
    x='PC1',
    y='PC2',
    data=pcaWheat,
    hue='category',
    fit_reg=False,   # no queremos la recta de regresión, solo los puntos
    legend=True
)

plt.title('2D PCA Graph')
plt.show()

""" Isomap """
# Isomap es un método NO LINEAL de reducción de dimensionalidad (a
# diferencia de PCA). En vez de mirar distancias "en línea recta" entre
# todos los puntos, construye un GRAFO de vecinos cercanos (n_neighbors)
# y aproxima la distancia entre dos puntos como el camino más corto sobre
# ese grafo (distancia geodésica). Esto permite capturar estructuras
# curvas o "en forma de variedad" (manifold) que PCA, al ser lineal, no
# puede representar bien.
#
# n_neighbors=6: cada punto se conecta con sus 6 vecinos más cercanos para
# construir el grafo.
# n_components=2: queremos el resultado final en 2 dimensiones.
isomapWheat = Isomap(n_neighbors=6, n_components=2)
isomapWheat.fit(xWheatScaled)
manifold_2Da = isomapWheat.transform(xWheatScaled)
manifold_2D = pd.DataFrame(manifold_2Da, columns=['Component 1', 'Component 2'])
manifold_2D['category'] = yWheat.to_numpy()

# Agrupamos por categoría para graficar cada variedad con su propio color
# y etiqueta (en vez de usar seaborn, acá se hace "a mano" con matplotlib).
groups = manifold_2D.groupby('category')
plt.title('2D Isomap Graph')
for name, group in groups:
    plt.plot(group['Component 1'], group['Component 2'], marker='o', linestyle='', markersize=5, label=name)
plt.legend()

# Vista rápida de las primeras filas del resultado (ya con 2 dimensiones)
manifold_2D.head()

""" t-SNE """
# t-SNE (t-distributed Stochastic Neighbor Embedding) es otro método NO
# LINEAL, pensado específicamente para VISUALIZACIÓN. A diferencia de PCA
# e Isomap, no busca preservar distancias globales sino preservar
# relaciones de VECINDAD LOCAL: puntos que son cercanos en el espacio
# original deben seguir siendo cercanos en 2D; no le importa tanto si
# grupos alejados en el espacio original quedan más o menos alejados en
# el gráfico final.
#
# perplexity=40: controla aproximadamente cuántos vecinos "efectivos" se
#   consideran para cada punto (equilibrio entre estructura local y global).
#   Valores típicos: 5 a 50; hay que probar varios en la práctica.
# n_iter=300: cantidad de iteraciones del algoritmo de optimización.
# verbose=1: muestra información de progreso mientras corre.
time_start = time.time()
tsneWheat = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsneWheatResults = tsneWheat.fit_transform(xWheatScaled)

print('t-SNE done! Time elapsed: {} seconds'.format(time.time() - time_start))
# Se mide el tiempo porque t-SNE es notablemente más lento que PCA,
# sobre todo con datasets grandes (no escala tan bien).

subsetWheatTSNE = pd.DataFrame(yWheat)
subsetWheatTSNE['tsne-2d-one'] = tsneWheatResults[:, 0]
subsetWheatTSNE['tsne-2d-two'] = tsneWheatResults[:, 1]

plt.figure(figsize=(16, 10))
sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    hue="category",
    palette=sns.color_palette("hls", 15),  # paleta de colores para las clases
    data=subsetWheatTSNE,
    legend="full",
    alpha=0.8   # transparencia de los puntos, ayuda a ver zonas superpuestas
)

""" UMAP """
# UMAP (Uniform Manifold Approximation and Projection) es también NO
# LINEAL y conceptualmente similar a t-SNE (preserva vecindades locales),
# pero suele ser mucho más RÁPIDO y, a diferencia de t-SNE, intenta
# preservar mejor también parte de la estructura GLOBAL de los datos
# (las distancias relativas entre clusters tienen algo más de sentido).
#
# init='random': cómo se inicializan las posiciones de los puntos antes
#   de optimizar (en vez de usar, por ejemplo, una inicialización basada
#   en espectros).
# random_state=0: fija la semilla aleatoria para que el resultado sea
#   reproducible (correr el script de nuevo da el mismo resultado).
umap_2d = UMAP(n_components=2, init='random', random_state=0)
umap_3d = UMAP(n_components=3, init='random', random_state=0)

# Nota: acá se usa xWheat (SIN escalar) en vez de xWheatScaled, a diferencia
# de PCA/Isomap/t-SNE. En la práctica sería más consistente escalar también
# antes de UMAP, por la misma razón explicada arriba (sensibilidad a escala).
proj_2d = umap_2d.fit_transform(xWheat)

umapProj2D = pd.DataFrame(proj_2d, columns=['Component 1', 'Component 2'])
umapProj2D['category'] = yWheat.to_numpy()

groups = umapProj2D.groupby('category')
plt.title('2D Unamp Graph')
for name, group in groups:
    plt.plot(group['Component 1'], group['Component 2'], marker='o', linestyle='', markersize=5, label=name)
plt.legend()

# Repetimos el proceso pero pidiendo 3 componentes, para poder graficar
# en un espacio 3D y comparar visualmente contra la versión 2D.
proj_3d = umap_3d.fit_transform(xWheat)
umapProj3D = pd.DataFrame(proj_3d, columns=['Component 1', 'Component 2', 'Component 3'])
umapProj3D['category'] = yWheat.to_numpy()

# Creamos una figura 3D "a mano" con matplotlib:
fig = plt.figure(figsize=(10, 6))
ax = Axes3D(fig, auto_add_to_figure=False)  # instancia de ejes 3D
fig.add_axes(ax)                            # la agregamos a la figura

# Buscamos las clases únicas y les asignamos un color distinto de una
# paleta ("husl" da colores bien distinguibles entre sí).
labels = np.unique(umapProj3D['category'])
palette = sns.color_palette("husl", len(labels))

# Graficamos cada clase por separado (un scatter 3D por variedad),
# así cada una queda con su propio color y su propia entrada en la leyenda.
for label, color in zip(labels, palette):
    df1 = umapProj3D[umapProj3D['category'] == label]
    ax.scatter(df1['Component 1'], df1['Component 2'], df1['Component 3'],
               s=40, marker='o', color=color, alpha=1, label=label)
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')

# bbox_to_anchor mueve la leyenda fuera del área del gráfico para que no
# tape los puntos.
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()
