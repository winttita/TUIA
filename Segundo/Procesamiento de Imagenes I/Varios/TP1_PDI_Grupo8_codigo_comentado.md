# TP1 PDI — Grupo 8: estado del repo, explicación de cada punto y código comentado

Repositorio: https://github.com/valentinocivetta04/Procesamiento_Imagenes_Grupo8
Materia: Procesamiento de Imágenes I (IA 4.4), TUIA, FCEIA-UNR — 2° cuatrimestre 2026
Autores: Civetta, Frank, Fucci, Winter
Revisado sobre el commit `c5240f7` (06/10/2026), rama `main`.

## 0. Cómo está armado este documento

Junta tres cosas:

1. **Revisión del repo** (sección 1): qué hay, si corre y qué diferencias encontré.
2. **Resumen del trabajo** (sección 2).
3. **Explicación de cada punto + código final comentado** (secciones 3 y 4). Para esto integré los cinco `.md` explicativos del grupo (`Problema1a`, `Problema1bc`, `Problema2a`, `Problema2b`, `Problema2cd`), que son material local (están en el `.gitignore`, no en el repo).

Cuando una explicación y el código del repo no coinciden, **manda el código del repo**. Las diferencias están listadas en la sección 1.4.

---

## 1. Estado actual del repositorio

### 1.1 Resumen

**El TP1 está completo y funciona.** Cloné el repo, ejecuté ambos scripts y los resultados coinciden con las tablas del informe.

| Aspecto | Estado |
|---|---|
| Problema 1 (a, b, c) | Implementado en `problema1.py`. Corre en ~5 s y reporta los 5 detalles ocultos. |
| Problema 2 (a, b, c, d) | Implementado en `problema2.py`. Procesa las 4 planillas y genera imágenes y CSV. |
| Informe | `Informe_TP1_PDI_Grupo8.pdf` (18 páginas): descripción, análisis, técnicas, pasos, resultados y conclusiones. Fecha 05/10/2026. |
| README | Completo: autores, estructura, requisitos, instalación y ejecución. |
| Ramas | `main` es la principal. `prueba/simplificacion-problema2` no tiene commits que `main` no tenga (quedó atrás). |
| Último movimiento | Correcciones de datos y redacción del informe (06/10). Antes: README, PDF y limpieza de archivos (04/10). |

### 1.2 Verificación que hice (ejecución real)

Problema 1, ventana 21x21:

```
> Superior izquierda: Un cuadrado pequeño
> Superior derecha: Una línea diagonal (de abajo-izq. hacia arriba-der.)
> Centro: La letra "a" minúscula
> Inferior izquierda: Cuatro líneas horizontales paralelas
> Inferior derecha: Un círculo
```

Problema 2:

| Planilla | Registros correctos | Campos MAL (Legajo / Nombre / P1 / P2 / P3 / Cond.) | No aprobados |
|---|---|---|---|
| `grade_sheet_1.png` | 15 de 20 | 5 / 5 / 5 / 5 / 5 / 5 | 4 R, 6 L |
| `grade_sheet_2.png` | 3 de 20 | 8 / 9 / 7 / 4 / 7 / 8 | 0 R, 3 L |
| `grade_sheet_3.png` | 0 de 20 | 10 / 9 / 7 / 5 / 8 / 8 | 0 R, 0 L |
| `grade_sheet_4.png` | 6 de 20 | 6 / 7 / 4 / 5 / 5 / 6 | 2 R, 2 L |

Lo corrí con versiones distintas a las del README (opencv 4.13.0, numpy 2.4.4, matplotlib 3.10.8) y anduvo igual, así que no depende de versiones exactas.

### 1.3 Observaciones menores (nada que rompa el TP)

1. **Referencias a archivos que no están en el repo.** Un comentario de `problema1.py` remite a `Problema1bc_explicacion.md` y `problema2.py` cita `PDI_U1_p1_Letras.py` (archivo de la cátedra). Quien clone el repo no los encuentra.
2. **Nombre de la imagen de entrada.** La consigna dice `Imagen_con_objetos_ocultos.tiff`; el repo usa `Imagen_con_detalles_escondidos.tif`. El informe ya lo aclara.
3. **`requirements.txt` sin versiones fijas.** El README explica cómo instalar las versiones exactas.
4. **Valores calibrados a mano.** Las posiciones de `ZONAS` y los umbrales (150, 0.8, 0.6, 6 px) salen de medir estas imágenes. El informe lo reconoce como limitación.

### 1.4 Diferencias entre las explicaciones `.md` y el código/informe finales

Los `.md` se escribieron punto por punto, a medida que se avanzaba, y algunas partes quedaron viejas:

| Dónde | Qué dice | Qué hay en realidad |
|---|---|---|
| `Problema2b_explicacion.md`, verificación | "56 celdas" de Condición Final con un solo caracter | **53** (24 L, 10 R, 19 A). Lo recalculé corriendo el código sobre las 4 planillas y coincide con el informe. |
| `Problema1a_explicacion.md`, bloque 4 | Un `__main__` con 5 ventanas (3, 7, 15, 31, 61) en grilla 2x3 | El script final tiene 4 figuras (puntos B y C) y 7 ventanas cuadradas + 4 rectangulares. Usá el código de la sección 3.7. |
| `Problema1a_explicacion.md` y `Problema1bc_explicacion.md`, "Estado" | Casilleros de punto B, C y Problema 2 sin tildar | Todo está hecho (ver `Problema2cd_explicacion.md`). |
| `Problema2a_explicacion.md` y `Problema2b_explicacion.md`, "Próximos pasos" | Describen b, c y d como pendientes | Los tres están implementados. Se resuelven distinto a lo planeado: el CSV usa `open`/`write` y no el módulo `csv`, y A/R/L se separan con la columna izquierda llena + agujero. |
| `Problema2a_explicacion.md`, punto b | Para separar A de R se pensaba en área o bounding box | Se resolvió con la columna izquierda llena (ver 4.4). |

---

## 2. Resumen general del trabajo

### Problema 1 — Ecualización local de histograma

**Idea.** La ecualización global usa el histograma de toda la imagen. En esta imagen los detalles ocultos difieren de su fondo en apenas unos niveles de gris, y como los píxeles oscuros son casi un tercio de la imagen, la global no los resalta. La **local** calcula el histograma solo dentro de una ventana MxN que se mueve píxel a píxel y usa esa ecualización para decidir el valor del píxel central.

**Qué se resuelve.**
- **a)** Función `ecualizacion_local(img, M, N)`.
- **b)** Aplicarla con ventana 21x21 y listar los detalles: cuadrado, línea diagonal, letra "a", cuatro líneas horizontales y círculo.
- **c)** Comparar tamaños de ventana: 3x3 y 7x7 llenan el fondo de manchas; de 15x15 a 31x31 los detalles se ven bien; 61x61 y 101x101 los apagan.

**Limitación.** La ecualización local también amplifica ruido: los píxeles de nivel 226 del fondo quedan negros (2,5 % del fondo) con cualquier ventana.

### Problema 2 — Validación de planillas de calificaciones

**Idea.** Cada planilla es una imagen con una tabla de 20 registros y 6 campos. El script **no lee texto**: cuenta caracteres y palabras a partir de la geometría de lo dibujado y chequea que cada campo cumpla su regla.

**Flujo.**
1. Umbralar (`img < 150`): texto y líneas quedan en `True`.
2. Sumar por filas y columnas: las líneas de la tabla sobresalen y dan las coordenadas de la grilla.
3. Recortar cada celda (sin las líneas).
4. Componentes conectadas por celda: cada caracter es una componente. La separación horizontal entre componentes permite contar palabras.
5. Aplicar la regla de cada campo → OK / MAL.
6. Con los registros 100 % OK y condición L o R, armar una imagen (recorte del nombre + letra roja R / azul L).
7. Guardar un CSV por planilla y repetir con las cuatro.

---

## 3. Problema 1 — Ecualización local de histograma

### 3.1 Qué pide la consigna

- **a.** Función de ecualización local que reciba la imagen y el tamaño de ventana MxN (M, N ∈ Z⁺).
- **b.** Usarla para analizar `Imagen_con_detalles_escondidos.tif` e informar los detalles ocultos de cada zona.
- **c.** Analizar la influencia del tamaño de ventana usando distintos tamaños.

**Ayuda de la consigna:** `cv2.copyMakeBorder(img, top, bottom, left, right, borderType)` para agregar píxeles alrededor de la imagen; con `cv2.BORDER_REPLICATE` se replican los valores del borde.

### 3.2 Marco teórico

**Histograma.** Cuenta cuántos píxeles hay de cada nivel de intensidad r_k (k = 0 … L−1, con L = 256 en uint8):

- `h(r_k) = n_k`
- Normalizado (probabilidad de cada nivel): `p(r_k) = n_k / (total de píxeles)`

La cátedra lo calcula de tres maneras: `cv2.calcHist()` (la más rápida), `np.histogram()` (velocidad media, sin máscaras ni varios canales) y `plt.hist()` (la más lenta, solo para visualizar).

**Ecualización global.** Redistribuye las intensidades para que el histograma quede lo más uniforme posible y aumente el contraste. La transformación es la función de distribución acumulada (CDF) escalada al rango de salida:

```
s_k = T(r_k) = (L − 1) · Σ_{j=0..k} p(r_j)
```

En la cátedra: `histn = hist / img.size`, `cdf = histn.cumsum()`, y `cv2.equalizeHist(img)` la aplica.

**Limitación de la global.** El histograma se calcula con todos los píxeles. Si un detalle tiene una intensidad casi igual a la de su fondo local y ocupa pocos píxeles, casi no pesa y no se resalta: se pierde la información local.

**Ecualización local.**
1. Se define una ventana MxN.
2. Se centra en un píxel.
3. Se calcula el histograma solo de los píxeles de la ventana y su transformación de ecualización.
4. Esa transformación se aplica solo al píxel central.
5. La ventana se desplaza un píxel y se repite hasta recorrer toda la imagen.

Como la CDF sale de los vecinos, diferencias mínimas dentro de una zona casi uniforme se estiran a todo el rango [0, 255]. Por eso aparecen los detalles escondidos.

**Por qué M y N son impares.** Para que haya un único píxel central, la ventana necesita la misma cantidad de píxeles a cada lado: M = 2m + 1 y N = 2n + 1. Con un tamaño par el centro quedaría entre dos píxeles.

**Bordes.** Cuando el píxel central está cerca del borde, parte de la ventana cae fuera de la imagen. Por eso se agregan m = M//2 filas arriba y abajo y n = N//2 columnas a los costados. Tipos de borde de OpenCV:

```
BORDER_REPLICATE:     aaaaaa|abcdefgh|hhhhhhh
BORDER_REFLECT:       fedcba|abcdefgh|hgfedcb
BORDER_REFLECT_101:   gfedcb|abcdefgh|gfedcba
BORDER_WRAP:          cdefgh|abcdefgh|abcdefg
BORDER_CONSTANT:      iiiiii|abcdefgh|iiiiiii  (con algún valor 'i')
```

Se usa `BORDER_REPLICATE` porque copia el valor del borde y no agrega niveles de intensidad que no existen. Rellenar con ceros metería píxeles negros artificiales en el histograma de las ventanas del borde y alteraría la ecualización.

### 3.3 La imagen de entrada

`Imagen_con_detalles_escondidos.tif` es de 256x256 (uint8) y tiene solo 15 niveles de gris, en dos grupos:

| Región | Niveles | Píxeles |
|---|---|---|
| Fondo claro | 226, 227, 228 | 1175 / 43946 / 1195 |
| 5 cuadrados oscuros de 62x62 px | 0 a 11 | 5 × 3844 = 19.220 |

- El fondo claro no es uniforme: tiene píxeles sueltos de 226 y 228 sobre un fondo de 227.
- Adentro de cada cuadrado el fondo es 0 (con algunos píxeles sueltos de nivel 1) y el detalle está dibujado con niveles entre 1 y 11. Como la diferencia es de 5 a 10 niveles sobre 255, a simple vista no se ve nada.
- Rango por zona: 0–11 (sup. izq.), 0–7 (sup. der.), 0–6 (centro), 0–9 (inf. izq.), 0–11 (inf. der.).

**Por qué falla la global.** Los 19.220 píxeles oscuros son el 29 % de la imagen y quedan juntos al principio de la CDF. Al ecualizar, casi todos se mapean a valores muy bajos y los detalles siguen sin verse.

### 3.4 Punto A — `ecualizacion_local`

```python
import cv2                         # OpenCV: bordes y ecualización
import numpy as np                 # arrays
import matplotlib.pyplot as plt    # figuras
from pathlib import Path           # rutas independientes del sistema operativo


# --- Problema 1.a - Ecualización local de histograma ---------------------------
def ecualizacion_local(img, M, N):
    # img : imagen en grises (2D, uint8)
    # M   : alto de la ventana (entero positivo impar)
    # N   : ancho de la ventana (entero positivo impar)
    # Devuelve una imagen uint8 del mismo tamaño que img.

    # Validación de parámetros: enteros positivos...
    if not (isinstance(M, (int, np.integer)) and isinstance(N, (int, np.integer)) and M > 0 and N > 0):
        raise ValueError('M y N deben ser enteros positivos.')
    # ...e impares: con tamaño impar la ventana tiene un píxel exacto en el centro.
    if M % 2 == 0 or N % 2 == 0:
        raise ValueError('M y N deben ser impares para que la ventana tenga un píxel central.')

    # Problema de los bordes: si el píxel central está en el borde de la imagen,
    # la ventana se sale. Solución: agrandar la imagen con M//2 filas arriba y abajo
    # y N//2 columnas a los costados, replicando el valor del borde.
    m, n = M // 2, N // 2
    img_borde = cv2.copyMakeBorder(img, m, m, n, n, cv2.BORDER_REPLICATE)

    # Imagen de salida vacía, mismo tamaño y tipo que la entrada.
    y = np.zeros_like(img)

    # Se recorre la imagen original píxel a píxel (ventana deslizante).
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Como img_borde está corrida m filas y n columnas respecto de img,
            # el slice [i:i+M, j:j+N] es exactamente la ventana MxN centrada en (i, j).
            ventana = img_borde[i:i + M, j:j + N]
            # Ecualización de histograma, pero calculada solo con esta ventana.
            ventana_eq = cv2.equalizeHist(ventana)
            # De toda la ventana ecualizada solo se conserva el píxel central,
            # que está en (m, n) dentro de la ventana.
            y[i, j] = ventana_eq[m, n]
    return y
```

**Explicación por bloques**

| Bloque | Concepto | De dónde sale | Adaptación al TP |
|---|---|---|---|
| Validación | La consigna pide M, N ∈ Z⁺ y, para tener píxel central, impares. | `cv2`, `numpy`, `matplotlib` y el estilo de comentar parámetros salen de `PI_U2_Transformacion_y_Filtrado_p1.py` (`imadjust`); `pathlib.Path` de `PDI_U2_p2_stain.py`. | También acepta enteros de NumPy (`np.int64`), útil si los tamaños se generan con `np.arange` en el punto C. |
| Bordes | Se agregan m filas y n columnas para que la ventana nunca se salga. `BORDER_REPLICATE` no inventa intensidades. | AYUDA de la consigna y tipos de borde de `PI_U2_Transformacion_y_Filtrado_p2.py` (líneas 12–20). | M es el alto (top/bottom) y N el ancho (left/right), así que también sirven ventanas rectangulares. |
| Recorrido | Por el padding, el píxel (i, j) original queda en (i+m, j+n) de `img_borde`. Por eso `img_borde[i:i+M, j:j+N]` es la ventana centrada en (i, j) y su centro está en `[m, n]`. | `cv2.equalizeHist` de `PI_U2_Transformacion_y_Filtrado_p1.py`; ecualizar un recorte con slicing es lo que hace `PDI_U2_p2_stain.py`. | En vez de un recorte fijo, la ventana se desliza por toda la imagen. |

### 3.5 Punto B — detalles ocultos

**Procedimiento**
1. **Ubicar las zonas.** Las coordenadas de los 5 cuadrados (62x62 px) se midieron a mano y están en la tabla `ZONAS`, junto con el detalle observado. La consigna pide analizar una sola imagen, así que no hace falta detectarlas automáticamente.
2. **Ecualizar localmente** toda la imagen con la ventana elegida en el punto C: 21x21.
3. **Mostrar** la imagen completa (original, global y local) y un zoom de cada zona antes y después.
4. **Informar** por consola el detalle de cada zona.

**Resultado**

| Zona | Posición (x, y) | Detalle oculto |
|---|---|---|
| Superior izquierda | (6, 6) | Un cuadrado pequeño, centrado |
| Superior derecha | (187, 6) | Una línea diagonal, de abajo-izquierda hacia arriba-derecha |
| Centro | (97, 97) | La letra "a" minúscula |
| Inferior izquierda | (6, 188) | Cuatro líneas horizontales paralelas |
| Inferior derecha | (187, 188) | Un círculo relleno |

La descripción de cada detalle sale de mirar la figura de zonas: el script no la calcula, la muestra como título de cada recorte y la imprime.

### 3.6 Punto C — influencia del tamaño de ventana

**Cómo se analizó.** Comparación visual de la imagen ecualizada con distintas ventanas:
- Figura 3: ventanas cuadradas de 3, 7, 15, 21, 31, 61 y 101, junto a la original y la ecualización global.
- Figura 4: ventanas rectangulares 3x31, 31x3, 1x61 y 61x1, con la de 21x21 como referencia.

Las dos comparten ejes (`sharex`/`sharey`), así que al hacer zoom se ve la misma región con todas las ventanas.

**Ventanas muy chicas (3x3 y 7x7): resaltan bordes y amplifican el ruido.**
- Con 3x3 los detalles grandes aparecen huecos: solo se ve el contorno del cuadrado pequeño y del círculo. Cuando la ventana cae entera adentro del detalle, todos sus píxeles tienen casi el mismo nivel y no hay nada que estirar. Solo en el borde, donde la ventana mezcla detalle y fondo, aparece contraste. Los detalles finos (líneas de 2 px, la "a") sí se ven bien, porque la ventana siempre toca el borde.
- El fondo claro se llena de ruido: en una ventana del fondo hay solo 227 y 228 (o solo 226 y 227), y `cv2.equalizeHist` lleva el nivel más bajo presente a 0, de modo que una diferencia de 1 nivel pasa a ser negro contra blanco. Con 7x7 se forman manchas negras grandes.
- A medida que la ventana crece, el interior de los detalles se va rellenando.

**Ventanas intermedias (15x15 a 31x31): el mejor resultado.**
- Los 5 detalles se ven completos y nítidos.
- En el fondo quedan solo puntos negros sueltos: casi todas las ventanas incluyen algún píxel de 226, el nivel más bajo del fondo. Son los 1175 píxeles de 226 de la imagen original (2,5 % del fondo): ruido de la imagen, no del método, y aparecen oscuros incluso con la ecualización global. El informe lo comprobó: los píxeles oscuros del fondo claro coinciden 100 % con esos.
- Se eligió 21x21 porque el fondo ya no tiene manchas, los cinco detalles se ven bien y dentro de los cuadrados quedan menos puntos sueltos que con 15x15.

**Ventanas grandes (61x61 en adelante): el resultado se parece a la global.**
- Los detalles se apagan: con 61x61 se ven grises y con 101x101 casi no se distinguen.
- **Por qué:** cuando la ventana se sale del cuadrado de 62x62 entran píxeles del fondo claro (226–228), que ocupan la parte de arriba de la CDF. Todos los niveles oscuros (0 a 11) quedan comprimidos en `[0, 255·p]`, donde `p` es la fracción de píxeles oscuros en la ventana. Cuanto más grande es la ventana, más chico es `p` y más oscuro queda el detalle.
- **Regla práctica:** cada zona empieza a apagarse cuando la mitad de la ventana (M//2) es mayor que la distancia del detalle al borde de su cuadrado. Distancias medidas en el informe (imagen ecualizada con 21x21): 24 px (sup. izq.), 16 (sup. der.), 20 (centro), **10 (inf. izq.)** y 14 (inf. der.). Por eso las cuatro líneas de abajo a la izquierda ya se ven apagadas con 31x31, mientras que el cuadrado pequeño (24 px) recién se apaga con 61x61.
- Con 61x61 aparece un efecto de viñeta: el centro del detalle queda más claro que los bordes, porque la ventana centrada en el borde del detalle incluye más fondo claro.

**Ventanas rectangulares: la orientación importa.**
- Con 3x31 (ventana horizontal) las líneas horizontales se mantienen nítidas. Con 31x3 (vertical) se degradan: la ventana sale del cuadrado por arriba y por abajo y toma fondo claro.
- Con 1x61 y 61x1 el problema es mayor: la ventana sale del cuadrado en una dirección y apaga los detalles, sobre todo la diagonal.
- En el fondo aparece ruido en forma de rayas orientadas como la ventana (horizontales con 3x31, verticales con 31x3).
- Si el detalle tiene una dirección conocida, conviene una ventana alargada en esa dirección. Si no se sabe, lo más seguro es una cuadrada.

**Costo computacional.** El tiempo crece con el tamaño de la ventana, porque en cada píxel se calcula el histograma de M·N valores. Con ventanas chicas domina el costo del recorrido píxel a píxel.

**Conclusión.** El tamaño de ventana tiene que estar entre dos límites que dependen de la imagen:
- **Mínimo:** lo bastante grande para que casi siempre la ventana tome a la vez parte del detalle y parte de su fondo. Si no, solo se ven bordes y el ruido del fondo se amplifica.
- **Máximo:** lo bastante chico para no salirse de la zona donde está el detalle. Si no, el fondo claro domina el histograma y el resultado se acerca al de la ecualización global.

En esta imagen el rango útil es **15x15 a 31x31**, y 21x21 da el mejor equilibrio.

### 3.7 Bloque principal (puntos B y C) — código comentado

```python
# --- Problema 1.b - Zonas de la imagen y detalles ocultos -----------------------
# Cada fila: (nombre, x, y, detalle observado).
# (x, y) = esquina superior izquierda de cada cuadrado oscuro de 62x62 px,
# medida a mano sobre la imagen. El detalle es lo que se ve en cada cuadrado
# después de aplicar la ecualización local.
ZONAS = [('Superior izquierda', 6, 6, 'Un cuadrado pequeño'),
         ('Superior derecha', 187, 6, 'Una línea diagonal (de abajo-izq. hacia arriba-der.)'),
         ('Centro', 97, 97, 'La letra "a" minúscula'),
         ('Inferior izquierda', 6, 188, 'Cuatro líneas horizontales paralelas'),
         ('Inferior derecha', 187, 188, 'Un círculo')]
L = 62   # lado de cada cuadrado oscuro, en píxeles


# Este bloque solo corre si se ejecuta el archivo directamente (no al importarlo).
if __name__ == '__main__':
    # La imagen se busca al lado del script, así funciona desde cualquier carpeta.
    ruta = Path(__file__).parent / 'Imagen_con_detalles_escondidos.tif'
    img = cv2.imread(str(ruta), cv2.IMREAD_GRAYSCALE)
    if img is None:   # imread no tira error si no encuentra el archivo: devuelve None
        raise FileNotFoundError(f'No se pudo cargar la imagen desde {ruta}')

    # =========================================================================
    # Punto B - Análisis de la imagen con la ecualización local
    # =========================================================================
    M_b, N_b = 21, 21                      # ventana elegida mirando el análisis del punto C
    img_heq = cv2.equalizeHist(img)        # ecualización GLOBAL, para comparar
    img_eq_local = ecualizacion_local(img, M_b, N_b)   # ecualización LOCAL 21x21

    # Figura 1: original vs. global vs. local (ejes compartidos: al hacer zoom
    # en una, se amplía la misma región en las tres).
    plt.figure('Punto B - Global vs. local')
    ax1 = plt.subplot(131)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)   # vmin/vmax fijos para comparar parejo
    plt.title('Imagen Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132, sharex=ax1, sharey=ax1)
    plt.imshow(img_heq, cmap='gray', vmin=0, vmax=255)
    plt.title('Ecualización global')
    plt.xticks([]), plt.yticks([])
    plt.subplot(133, sharex=ax1, sharey=ax1)
    plt.imshow(img_eq_local, cmap='gray', vmin=0, vmax=255)
    plt.title(f'Ecualización local ({M_b}x{N_b})')
    plt.xticks([]), plt.yticks([])

    # Figura 2: cada zona recortada, original (fila de arriba) y ecualizada
    # localmente (fila de abajo), más el informe de detalles por consola.
    print(f'\n--- Punto B: detalles ocultos (ventana {M_b}x{N_b}) ---')
    plt.figure('Punto B - Detalles por zona')
    for k, (nombre, x, y, detalle) in enumerate(ZONAS):
        plt.subplot(2, 5, k + 1)                       # fila 1: original
        plt.imshow(img[y:y + L, x:x + L], cmap='gray', vmin=0, vmax=255)   # recorte [filas, columnas]
        plt.title(f'{nombre}\n(original)', fontsize=9)
        plt.xticks([]), plt.yticks([])
        plt.subplot(2, 5, k + 6)                       # fila 2: ecualizada
        plt.imshow(img_eq_local[y:y + L, x:x + L], cmap='gray', vmin=0, vmax=255)
        plt.title(detalle, fontsize=9)
        plt.xticks([]), plt.yticks([])
        print(f'> {nombre}: {detalle}')

    # =========================================================================
    # Punto C - Influencia del tamaño de la ventana (comparación visual)
    # =========================================================================
    # Figura 3: imagen completa con distintas ventanas cuadradas
    cuadradas = [(3, 3), (7, 7), (15, 15), (21, 21), (31, 31), (61, 61), (101, 101)]
    plt.figure('Punto C - Ventanas cuadradas')
    ax1 = plt.subplot(331)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title('Imagen Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(332, sharex=ax1, sharey=ax1)
    plt.imshow(img_heq, cmap='gray', vmin=0, vmax=255)
    plt.title('Ecualización global')
    plt.xticks([]), plt.yticks([])
    for k, (M, N) in enumerate(cuadradas):
        plt.subplot(3, 3, k + 3, sharex=ax1, sharey=ax1)   # k+3: los dos primeros lugares ya están usados
        plt.imshow(ecualizacion_local(img, M, N), cmap='gray', vmin=0, vmax=255)
        plt.title(f'Ecualización local ({M}x{N})')
        plt.xticks([]), plt.yticks([])

    # Figura 4: ventanas rectangulares (la orientación de la ventana importa).
    # M es el alto y N el ancho: 3x31 es una ventana baja y ancha; 31x3, alta y angosta.
    rectangulares = [(3, 31), (31, 3), (1, 61), (61, 1)]
    plt.figure('Punto C - Ventanas rectangulares')
    ax1 = plt.subplot(231)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.title('Imagen Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232, sharex=ax1, sharey=ax1)
    plt.imshow(img_eq_local, cmap='gray', vmin=0, vmax=255)
    plt.title(f'Referencia ({M_b}x{N_b})')
    plt.xticks([]), plt.yticks([])
    for k, (M, N) in enumerate(rectangulares):
        plt.subplot(2, 3, k + 3, sharex=ax1, sharey=ax1)
        plt.imshow(ecualizacion_local(img, M, N), cmap='gray', vmin=0, vmax=255)
        plt.title(f'Ecualización local ({M}x{N})')
        plt.xticks([]), plt.yticks([])

    plt.show()   # muestra las 4 figuras; el script termina al cerrarlas
```

Resumen de lo que genera el script:

| Figura | Punto | Contenido |
|---|---|---|
| 1 | B | Original, ecualización global y local 21x21 |
| 2 | B | Zoom de cada cuadrado antes y después |
| 3 | C | Imagen completa con ventanas 3, 7, 15, 21, 31, 61 y 101 |
| 4 | C | Ventanas rectangulares 3x31, 31x3, 1x61 y 61x1 |

`vmin=0, vmax=255` en todos los `imshow` evita que matplotlib reescale el contraste automáticamente, lo que confundiría la comparación (tema de la Unidad 1).

### 3.8 Verificación y observaciones

Pruebas hechas por el grupo sobre `ecualizacion_local` (de `Problema1a_explicacion.md`):

| Prueba | Resultado |
|---|---|
| Imagen del TP (256x256), ventana 15x15 | Corre sin errores, ~0,14 s; salida uint8 del mismo tamaño |
| Ventanas 3x3, 3x7 (rectangular) y 1x1 | Salida del mismo tamaño que la entrada |
| M, N como `np.int64` | Aceptados |
| M par (4x3), M = 0, M = 3.0 (float) | Lanzan `ValueError` |
| Imagen sintética: cuadrado oculto con 5 niveles de diferencia respecto del fondo | Tras la ecualización local la diferencia pasa a 255 |
| Imagen del TP: global vs. local | La global casi no cambia nada; la local deja ver el contenido de los 5 cuadrados |

**Observaciones**
- **Ruido en zonas uniformes.** En el fondo claro aparecen puntitos. Es el comportamiento esperado: en una ventana casi constante, diferencias de 1–2 niveles se estiran a todo el rango. No es un error del código.
- **Costo computacional.** Se hace una ecualización por píxel: 65.536 llamadas a `equalizeHist` para 256x256. Corre rápido porque cada ventana es chica.

---

## 4. Problema 2 — Validación de planillas de calificaciones

### 4.1 Qué pide la consigna

Una planilla es una imagen con una tabla de 20 registros, cada uno con 6 campos. El script recibe solo la imagen y tiene que:

- **a.** Mostrar por pantalla, para cada registro, qué campos están OK y cuáles MAL, con el formato del ejemplo (`> Registro 1:`, `> Legajo: OK`, ...).
- **b.** Generar una única imagen con los alumnos que no aprobaron (Condición Final "L" o "R"), solo de registros bien cargados, con el recorte de Nombre y Apellido y un indicador que diferencie R de L.
- **c.** Generar un CSV con una fila por registro: ID en la primera columna (orden de la planilla) y una columna por campo con OK o MAL.
- **d.** Aplicar todo de forma cíclica a las cuatro planillas e informar resultados.

**Reglas de validación**

| Campo | Regla |
|---|---|
| Legajo | 8 caracteres, una sola palabra |
| Nombre y apellido | al menos 2 palabras y como mucho 12 caracteres |
| Parcial 1, 2 y 3 | 1 o 2 caracteres seguidos, sin espacios |
| Condición Final | un solo caracter |

No hay que leer qué dice cada campo ni verificar si el dato es válido: alcanza con contar caracteres y palabras.

### 4.2 Punto A — cómo está resuelto, paso a paso

**1. Binarizar.** Se pasa la planilla a grises y se arma una matriz booleana con `img < 150`: texto y líneas quedan en `True`, el fondo en `False`.
- *De dónde sale:* AYUDA del enunciado (`img_th = img < th`), umbral manual de `PDI_U3_Segmentacion.py` y la matriz booleana `gray_image < 5` de `PDI_U2_p2_stain.py`.
- *Por qué 150:* se eligió mirando los valores de la imagen. Los bordes grises de la hoja valen entre 178 y 201, así que con 150 no se cuelan como si fueran líneas; el texto y las líneas son casi negros.

**2. Líneas horizontales.** Se suman los `True` de cada fila (`np.sum(img_th, 1)`). Las filas con línea de tabla tienen muchísimos más píxeles oscuros que el resto; se toman las que superan el 80 % del máximo.
- *De dónde sale:* AYUDA del enunciado y `PDI_U2_p2_stain.py` (`np.sum(..., axis=1)` comparando contra `sum_rows.max()`).
- *Por qué relativo al máximo:* las cuatro planillas tienen tamaños distintos (1107, 1029, 1106 y 917 px de ancho), así que un umbral fijo no sirve. La línea debajo de "Notas" es más corta y queda afuera, que es lo que se quiere.
- *Margen:* según el informe, las filas que no son línea llegan como máximo a 412 píxeles y el umbral de detección va de 666 a 786 según la planilla.

Para pasar de "filas en `True`" a "dónde empieza y termina cada línea" se usa la técnica de pulsos: `np.diff` marca los cambios, `np.argwhere` da sus índices, a los inicios se les suma 1 y se agrupan de a pares con `reshape(-1, 2)`.
- *De dónde sale:* `PDI_U1_p1_Letras.py`, sección "Encontrar inicio/fin de pulsos" y el armado de `r_idxs`. La AYUDA avisa que las líneas pueden tener más de 1 píxel de ancho.

En las cuatro planillas aparecen **22 líneas**: borde superior de la tabla, línea bajo el encabezado y una bajo cada uno de los 20 registros. Cada registro queda entre dos líneas seguidas.

**3. Líneas verticales.** Igual, pero con las columnas (`np.sum(img_th, 0)`) y un umbral propio, más bajo: 60 % del máximo. Las divisiones entre Parcial 1, 2 y 3 son más cortas (arrancan en el sub-encabezado). Medido en las cuatro planillas, las líneas verticales llegan como mínimo al 83 % del máximo y ninguna otra columna pasa del 37 %, así que el 60 % las toma a las 8 con margen de los dos lados. Las 8 líneas definen 7 columnas; la primera es "Nro." y no se valida.
- *De dónde sale:* AYUDA del enunciado ("un umbral acorde, uno para horizontales y otro para verticales").

**4. Recortar cada celda.** Es el rectángulo entre dos líneas horizontales y dos verticales seguidas, sin incluir las líneas (desde el fin de una línea + 1 hasta el inicio de la siguiente). Mismo recorte por índices que `PDI_U1_p1_Letras.py` usa para sacar renglones y letras.

**5. Contar caracteres.** Sobre cada celda se aplica `cv2.connectedComponentsWithStats(celda, 8, cv2.CV_32S)`: cada caracter es una componente conectada.
- *De dónde sale:* `PDI_U3_Segmentacion.py` (sección "Componentes conectadas") y la segunda AYUDA del TP.
- La etiqueta 0 es el fondo, así que se descarta.
- Se filtra por área (`stats[:, -1] > th_area`). Se usa `th_area = 1`: solo se descartan píxeles sueltos. Como la celda se recorta sin las líneas, no quedan restos de la tabla, y un umbral más alto se comía caracteres reales: el guion mide 4 a 5 px de área y el punto de "1.0" mide 3.

**6. Contar palabras.** Se ordenan las componentes de izquierda a derecha y se mide cuántas columnas vacías hay entre el final de un caracter y el comienzo del siguiente. Si hay más de 6 px, hay un espacio. **Palabras = espacios + 1.**
- *De dónde sale la idea:* `PDI_U1_p1_Letras.py` separa letras buscando columnas vacías; acá es lo mismo un nivel más arriba: los huecos cortos separan letras y los largos separan palabras.
- *El 6:* medido en las cuatro planillas. Entre letras de una misma palabra hay de 0 a 4 px (992 separaciones) y un espacio mide de 10 a 13 px (61 separaciones). El 6 queda en el medio.

**7. Aplicar las reglas e imprimir.** Con caracteres y palabras de cada celda se aplica la regla del campo y se imprime OK o MAL.

### 4.3 Punto A — código comentado

```python
import cv2
import numpy as np
from pathlib import Path


# --- Problema 2.a - Validación de los campos de una planilla -------------------
# Cada campo tiene una regla expresada como función de (c = cantidad de caracteres,
# p = cantidad de palabras). Con lambda, la regla queda escrita junto al nombre del campo.
CAMPOS = [('Legajo',            lambda c, p: c == 8 and p == 1),         # 8 caracteres, una palabra
          ('Nombre y apellido', lambda c, p: p >= 2 and c <= 12),        # 2+ palabras, máx. 12 caracteres
          ('Parcial 1',         lambda c, p: 1 <= c <= 2 and p == 1),    # 1 o 2 caracteres pegados
          ('Parcial 2',         lambda c, p: 1 <= c <= 2 and p == 1),
          ('Parcial 3',         lambda c, p: 1 <= c <= 2 and p == 1),
          ('Condición Final',   lambda c, p: c == 1)]                    # un solo caracter


def pulsos(v):
    # v : vector booleano (por ejemplo "esta fila/columna supera el umbral").
    # Devuelve una fila [inicio, fin] por cada tramo seguido de valores True.
    # Sirve aunque una línea de la tabla tenga más de 1 píxel de ancho.
    #
    # np.diff(v) marca dónde el valor cambia (True<->False). argwhere da esos índices.
    # Los cambios vienen alternados: subida (empieza un tramo), bajada (termina el tramo).
    #   - Subida en i  -> el tramo empieza en i+1  (por eso idx[0::2] += 1)
    #   - Bajada en i  -> el último True es i      (se deja igual)
    # reshape(-1, 2) agrupa de a pares -> [[inicio, fin], [inicio, fin], ...]
    idx = np.argwhere(np.diff(v))
    idx[0::2] += 1
    return idx.reshape(-1, 2)


def celda(m, filas, cols, i, j):
    # Recorta la celda del registro i, columna j, SIN incluir las líneas de la tabla:
    # desde el final de la línea i (+1) hasta el comienzo de la línea siguiente.
    # filas[i, 1] = fin de la línea horizontal i; filas[i+1, 0] = inicio de la siguiente.
    return m[filas[i, 1] + 1:filas[i + 1, 0], cols[j, 1] + 1:cols[j + 1, 0]]


def validar_planilla(ruta, th=150, th_area=1, th_espacio=6):
    # ruta       : imagen de la planilla (grade_sheet_<id>.png)
    # th         : umbral de intensidad; por debajo = texto o línea (True)
    # th_area    : área mínima de una componente para contarla como caracter
    # th_espacio : separación horizontal mínima (px) para considerar que hay un espacio
    # Devuelve   : img, img_th, filas, cols y, por registro, la lista de OK/MAL por campo.
    img = cv2.imread(str(ruta), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f'No se pudo cargar la imagen desde {ruta}')

    # 1) Umbralado: True donde hay tinta (texto y líneas). Los márgenes grises quedan en False.
    img_th = img < th

    # 2) Líneas horizontales: sumar por filas. Una línea de la tabla ocupa casi todo el ancho,
    #    así que su suma es altísima. Umbral relativo al máximo (0.8) porque cada planilla
    #    tiene distinto tamaño. Resultado: 22 líneas (borde sup., bajo encabezado, una por registro).
    img_rows = np.sum(img_th, 1)
    filas = pulsos(img_rows > 0.8 * img_rows.max())

    # 3) Líneas verticales: sumar por columnas, con umbral más bajo (0.6) porque las
    #    divisiones entre Parcial 1/2/3 son más cortas que el resto. Resultado: 8 líneas.
    img_cols = np.sum(img_th, 0)
    cols = pulsos(img_cols > 0.6 * img_cols.max())

    registros = []
    # Cada registro está entre dos líneas horizontales (se saltean la línea 0 y el encabezado).
    for i in range(1, len(filas) - 1):
        print(f'> Registro {i}:')
        oks = []
        # j = 0 es la columna "Nro.", no se valida; los 6 campos son las columnas 1 a 6.
        for j, (campo, regla) in enumerate(CAMPOS, start=1):
            # 4) Componentes conectadas de la celda: cada caracter es una componente.
            #    astype(uint8) porque la función no acepta booleanos.
            _, _, stats, _ = cv2.connectedComponentsWithStats(
                celda(img_th, filas, cols, i, j).astype(np.uint8), 8, cv2.CV_32S)
            stats = stats[1:]                                  # la etiqueta 0 es el fondo: se descarta
            stats = stats[stats[:, -1] > th_area, :]           # se descartan componentes de área mínima
            stats = sorted(stats, key=lambda s: s[0])          # ordenadas de izquierda a derecha (x)
            # stats[k] = [x, y, ancho, alto, área]. El hueco entre caracteres consecutivos es
            # x del siguiente menos el borde derecho (x + ancho) del anterior.
            gaps = [b[0] - (a[0] + a[2]) for a, b in zip(stats, stats[1:])]
            n_car = len(stats)                                 # cantidad de caracteres
            # Palabras = espacios + 1. Entre letras de una palabra el hueco es de 0 a 4 px;
            # entre palabras, 10 a 13 px. El umbral de 6 queda en el medio.
            n_pal = 1 + sum(g > th_espacio for g in gaps)
            oks.append(regla(n_car, n_pal))                    # se aplica la regla del campo
            print(f'> {campo}: {"OK" if oks[-1] else "MAL"}')
        print('>')
        registros.append(oks)
    return img, img_th, filas, cols, registros
```

### 4.4 Punto B — distinguir L, R y A y armar la imagen

**El problema nuevo.** En el punto a solo se contaban caracteres; ahora hay que saber qué letra hay en Condición Final. El material de la cátedra no tiene nada para reconocer letras, así que se usaron dos propiedades de forma que se pueden medir con herramientas ya vistas.

**Propiedad 1: columna izquierda llena.** La L y la R arrancan con un trazo vertical, así que la primera columna de su bounding box está llena de arriba a abajo. La A arranca en diagonal y en esa columna tiene muy pocos píxeles. Se mide sumando por columnas la letra recortada a su bounding box y mirando si la primera suma es igual al alto.
- La suma por columnas es la de la AYUDA del TP y de `PDI_U2_p2_stain.py`; el bounding box sale de `stats` de `connectedComponentsWithStats` (`PDI_U3_Segmentacion.py`).

**Propiedad 2: agujero.** La R tiene uno (la panza cerrada) y la L no. Se usa `cv2.findContours` con `cv2.RETR_TREE`, que devuelve la jerarquía `[Next, Previous, First_Child, Parent]`. El contorno de un agujero queda dentro del contorno exterior de la letra, así que tiene madre (`Parent != -1`). Si hay algún contorno con madre, hay agujero.
- Sale de `PDI_U3_Segmentacion.py` ("Contornos por jerarquía" y "Contornos que no tienen madres/padres"), solo que ahí se filtra con `hierarchy[0][ii][3] == -1` y acá se cuentan los que no lo cumplen.

**Reglas juntas**

| Columna izquierda | Agujero | Resultado |
|---|---|---|
| Incompleta | — | A (u otro caracter): se descarta |
| Llena | Sí | R |
| Llena | No | L |

**Validación de la regla.** Antes de escribirla se midieron todas las celdas de Condición Final con un solo caracter en las cuatro planillas: son **53** (24 L, 10 R, 19 A; la explicación original decía 56, ver 1.4). En todas las L y R la primera columna mide exactamente el alto de la letra (12 px, o 10 en la planilla 4), en las A mide entre 1 y 3 px, y los agujeros dan 0 en las L y 1 en las R. No hubo ningún caso dudoso.

**Armar la imagen de salida.** Cada alumno es una fila:
- Al recorte de Nombre y Apellido se le agrega margen blanco con `cv2.copyMakeBorder` (40 px a la izquierda para el indicador y 5 px en los otros lados), con `BORDER_CONSTANT` y valor 255.
- Se escribe la letra de la condición en ese margen con `cv2.putText`: **R en rojo, L en azul**. Los colores van en BGR porque se guarda con `cv2.imwrite`.
- El recorte sale de la imagen en grises, así que se pasa a 3 canales con `cv2.cvtColor` para poder dibujar en color (como hace `PDI_U3_Segmentacion.py` con `COLOR_GRAY2RGB`).
- Las filas se apilan con `np.vstack`, así no hace falta calcular el tamaño de la imagen ni la posición de cada recorte.
- Si no queda ningún alumno L o R, igual se genera una imagen chica (con `np.full`) con el texto "Sin alumnos L/R". Hace falta porque `np.vstack` de una lista vacía da error y la planilla 3 no tiene ningún alumno L o R.

*Fuentes:* `cv2.putText` de `PI_U2_ej_video_face_detection_and_blur.py`; `np.full` y el orden BGR de `PI_U2_ej_blurred_face.py`; `cv2.imwrite` de `PDI_U1_Fundamentos_p1.py`; `np.vstack` es NumPy básico (no está en el material).

### 4.5 Punto B — código comentado

```python
# --- Problema 2.b - Imagen con los alumnos que no aprobaron --------------------
def condicion(letra):
    # letra : celda binaria (uint8) de Condición Final con un único caracter.
    # Devuelve 'L', 'R' o None (A u otro caracter).
    #   - L y R tienen la columna izquierda llena (trazo vertical); la A no (empieza en diagonal).
    #   - La R tiene un agujero (un contorno con "madre" en la jerarquía); la L no.
    _, _, stats, _ = cv2.connectedComponentsWithStats(letra, 8, cv2.CV_32S)
    x, y, w, h = stats[1, :4]            # caja que rodea al caracter (stats[0] es el fondo)
    # Se suma por columnas dentro de la caja y se mira la primera columna:
    # si no está completa (suma < alto) no es L ni R.
    if np.sum(letra[y:y + h, x:x + w], 0)[0] < h:
        return None
    # findContours con RETR_TREE devuelve la jerarquía de contornos. Un contorno que
    # tiene "padre" (hh[3] != -1) es un agujero dentro de la letra.
    contours, hierarchy = cv2.findContours(letra, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    agujeros = sum(hh[3] != -1 for hh in hierarchy[0])   # hierarchy: [Next, Previous, First_Child, Parent]
    return 'R' if agujeros else 'L'


def imagen_no_aprobados(ruta, img, img_th, filas, cols, registros):
    # Arma una fila por alumno con los 6 campos OK y Condición Final L o R:
    # letra indicadora (roja R, azul L; colores en BGR) + recorte del Nombre y Apellido.
    alumnos, salida = [], []
    for i, oks in enumerate(registros, start=1):
        # Solo se mira la condición si el registro entero está bien cargado (all(oks)).
        c = condicion(celda(img_th, filas, cols, i, 6).astype(np.uint8)) if all(oks) else None
        if c:
            # Recorte del nombre (columna 2) con margen blanco; 40 px a la izquierda para la letra.
            fila = cv2.copyMakeBorder(celda(img, filas, cols, i, 2), 5, 5, 40, 5, cv2.BORDER_CONSTANT, value=255)
            fila = cv2.cvtColor(fila, cv2.COLOR_GRAY2BGR)   # a color para poder dibujar en rojo/azul
            # Se escribe la letra R (rojo) o L (azul) a la izquierda del nombre.
            cv2.putText(fila, c, (10, fila.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 255) if c == 'R' else (255, 0, 0), 2)
            alumnos.append(c)
            salida.append(fila)
    # Se apilan todas las filas en una sola imagen. Si no hay ningún alumno, se genera
    # igual una imagen con el texto "Sin alumnos L/R" (así siempre hay una salida por planilla).
    salida = np.vstack(salida) if salida else cv2.putText(
        np.full((30, 200), 255, np.uint8), 'Sin alumnos L/R', (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 0, 1)

    # Se guarda junto a la planilla: no_aprobados_grade_sheet_<id>.png
    ruta_salida = Path(ruta).with_name(f'no_aprobados_{Path(ruta).stem}.png')
    cv2.imwrite(str(ruta_salida), salida)
    print(f'Imagen de alumnos no aprobados: {ruta_salida.name} ({len(alumnos)} alumnos)')
    return alumnos
```

### 4.6 Puntos C y D — CSV y ciclo sobre las cuatro planillas

**Punto c.** No hubo que procesar nada nuevo de la imagen: `validar_planilla` ya devuelve la lista de OK/MAL de cada registro en el orden de la planilla, así que el CSV es escribir esa lista en un archivo de texto:
- Una primera línea con los nombres de las columnas, copiados del enunciado (c.ii).
- Una línea por registro con su número (1 a 20) como ID y los seis resultados separados por comas.
- Las filas vacías de la planilla también van, con todo MAL: el enunciado pide una fila por registro y el ID tiene que coincidir con el orden.
- Se escribe con `open`/`write` de Python base: el material de la cátedra no tiene ningún ejemplo de escritura de CSV.
- El nombre sale del de la planilla (`validacion_` + nombre sin extensión), con `pathlib.Path` (`PDI_U2_p2_stain.py`).

**Punto d.** El bloque principal recorre las planillas con un `for`. Para cada una:
1. Llama una sola vez a `validar_planilla` (punto a).
2. Pasa esos datos a `imagen_no_aprobados` (punto b). Antes esta función llamaba a la validación por su cuenta; se cambió para que cada planilla se procese una sola vez.
3. Guarda el CSV (punto c).
4. Imprime un resumen: registros con los seis campos bien, MAL por campo y alumnos en R y en L.

Los nombres se arman con el índice (`grade_sheet_{k}.png`, k de 1 a 4), el mismo recurso que usa `PDI_U1_p1_Letras.py` (MEJORA 2). Así queda afuera `grade_sheet_empty.png`, que no tiene registros.

### 4.7 Puntos C y D — código comentado

```python
# --- Problema 2.c - CSV con los resultados de la validación -------------------
def guardar_csv(ruta, registros):
    # Una fila por registro: ID (orden en la planilla) + un OK/MAL por campo, en el orden de la planilla.
    ruta_csv = Path(ruta).with_name(f'validacion_{Path(ruta).stem}.csv')
    with open(ruta_csv, 'w', encoding='utf-8') as f:
        f.write('ID,Legajo,Nombre y Apellido,Parcial 1,Parcial 2,Parcial 3,Condición Final\n')   # columnas del enunciado
        for i, oks in enumerate(registros, start=1):
            f.write(f'{i},' + ','.join('OK' if ok else 'MAL' for ok in oks) + '\n')
    print(f'CSV de validación: {ruta_csv.name}')


# --- Problema 2.d - Aplicación cíclica sobre las cuatro planillas --------------
if __name__ == '__main__':
    for k in range(1, 5):      # grade_sheet_1.png ... grade_sheet_4.png
        ruta = Path(__file__).parent / f'grade_sheet_{k}.png'
        print(f'\n=============== {Path(ruta).name} ===============')
        img, img_th, filas, cols, registros = validar_planilla(ruta)                # Punto a
        alumnos = imagen_no_aprobados(ruta, img, img_th, filas, cols, registros)    # Punto b
        guardar_csv(ruta, registros)                                                # Punto c

        # Informe de resultados de la planilla
        n_ok = sum(all(oks) for oks in registros)                                   # registros con los 6 campos OK
        mal = [sum(not oks[j] for oks in registros) for j in range(len(CAMPOS))]    # campos MAL por columna
        print(f'Registros correctos: {n_ok} de {len(registros)}')
        print('Campos MAL: ' + ', '.join(f'{campo} {m}' for (campo, _), m in zip(CAMPOS, mal)))
        print(f'No aprobados: {alumnos.count("R")} R, {alumnos.count("L")} L')
```

### 4.8 Resultados

Alumnos que no aprobaron, con los seis campos bien cargados (de la verificación del punto b):

| Planilla | Registros con todo OK y L o R | Alumnos |
|---|---|---|
| 1 | 10 | **L:** Bianca Monte, Farias Jorge, Juana Gomez, Amanda Santos, Nahuel Fausto, Julio Foglia. **R:** Rivas Hugo, Jorge Delgado, Jose Santini, Camila Godoy |
| 2 | 3 | **L:** Bianca Monte, Farias Jorge, Amanda Santos |
| 3 | 0 | Imagen con "Sin alumnos L/R" (ningún registro tiene los seis campos bien) |
| 4 | 4 | **L:** Nicolas Vega, Miguel Sastre. **R:** Jorge Delsio, Camila Godoy |

Qué se ve en los números (tabla de la sección 1.2):
- La **planilla 1** es la "limpia": los únicos MAL son las 5 filas vacías (registros 3, 11, 14, 15 y 20), que fallan en todos los campos.
- La **planilla 3** no tiene ningún registro completo. Los errores son de los mismos tipos que en la 2: legajos con dígitos de más o de menos o con espacios, nombres de una sola palabra o muy largos, notas vacías o de tres caracteres ("100", "AUS") y condiciones como "LL", "RR" o "Rec".
- En las cuatro planillas las filas vacías cuentan como registros con todo MAL.
- En la planilla 4 hay registros con todo OK y condición A (Juana Gomez, Renzo Garcia): quedan afuera, como corresponde. Los registros con algún campo MAL no aparecen aunque su condición sea L o R (por ejemplo Nahuel Fausto en la planilla 2, que tiene "LL").

### 4.9 Verificación

Se corrió el script en las cuatro planillas y se compararon a mano los 80 registros con lo que se ve en cada imagen: coinciden todos. Casos que confirman las reglas:

| Planilla | Registro | Contenido | Resultado |
|---|---|---|---|
| 1 | 1 | Ejemplo de la figura 3a (C-1557/1, JUAN CARLINI, 6, 6, 7, A) | todo OK |
| 2 | 1 | JULIAN CARLINI (13 letras) | Nombre MAL |
| 2 | 4 | R-87455/6 (9 caracteres) | Legajo MAL |
| 2 | 19 | S-94722/ 1 (tiene un espacio) | Legajo MAL; Parcial 3 = 100, MAL |
| 3 | 8 | AMANDASANTOS (una sola palabra) | Nombre MAL |
| 3 | 15 | Parcial 2 = 1.0 (el punto cuenta como caracter) | Parcial 2 MAL |
| 2 | 17 | Condición "Rec" | Condición MAL |
| 1 | 3, 11, 14, 15, 20 | Filas vacías | todo MAL |

Además:
- La salida del punto a es idéntica a la de antes de reestructurar el código, en las cuatro planillas (comparada línea por línea).
- Cada CSV tiene 21 líneas (encabezado + 20 registros), 7 columnas, IDs del 1 al 20 en orden y los mismos OK/MAL que imprime la consola.

### 4.10 Decisiones propias y limitaciones

Cosas que el material no define y el grupo resolvió:

- **Los 12 caracteres del nombre no cuentan el espacio.** El enunciado dice "no más de 12 caracteres en total" sin aclarar si el espacio suma. Con componentes conectadas el espacio no aparece (no tiene píxeles), así que se cuentan solo letras. Con esa interpretación AMANDA SANTOS (12 letras) da OK. Si la cátedra quiere contarlo, alcanza con sumar `n_pal - 1` a los caracteres. **Conviene consultarlo antes de entregar:** cambiaría el resultado de nombres como AMANDA SANTOS o NAHUEL FAUSTO.
- **Una fila vacía da todo MAL**, porque ningún campo vacío cumple su regla.
- **La Ñ se contaría como dos caracteres** (la N y la tilde son dos componentes). No aparece en las planillas, así que no se resolvió; habría que unir componentes que se superponen en x.
- **El criterio de la columna izquierda llena** para separar A de L/R es del grupo (las herramientas sí son de la cátedra). Si apareciera otra letra con trazo vertical a la izquierda (B, D, P...), se clasificaría como L o R según tenga agujero. Como el enunciado solo habla de L y R, no se cubrió.
- **Umbrales** (150, 80 % para filas, 60 % para columnas, área 1, espacio 6 px): ajustados mirando las cuatro planillas. Con otra tipografía u otra escala podrían fallar.
- **Formato de la imagen de salida** (apilado vertical, letra roja o azul a la izquierda) y **ubicación de los archivos** (junto a cada planilla): elegidos por el grupo; el enunciado no los define.
- Dos nombres para el mismo campo: el CSV usa "Nombre y Apellido" (como pide c.ii) y la consola "Nombre y apellido" (como el ejemplo del punto a). El enunciado usa las dos formas.

---

## 5. Cómo ejecutarlo

```bash
python3 -m venv .venv
source .venv/bin/activate          # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
python problema1.py                # abre 4 figuras y lista los detalles por consola
python problema2.py                # genera no_aprobados_*.png y validacion_*.csv junto a cada planilla
```

Sin pantalla, para el Problema 1: `MPLBACKEND=Agg python problema1.py`.

---

## 6. Material de la cátedra usado

| Archivo | Qué se tomó |
|---|---|
| `TUIA_PDI_TP1_2026_C2.pdf` (consigna) | Reglas de cada campo, formato de salida, AYUDAS: `copyMakeBorder` + `BORDER_REPLICATE`, umbral, sumas por fila/columna, líneas de más de 1 px, componentes conectadas, filtrado por área |
| `U2/Código-20260826/PI_U2_Transformacion_y_Filtrado_p1.py` | `imread` en grises, `cv2.equalizeHist`, histograma → CDF, subplots con `sharex/sharey` y `vmin/vmax`, estilo de comentarios de parámetros |
| `U2/Código-20260826/PI_U2_Transformacion_y_Filtrado_p2.py` | Tipos de borde de OpenCV y elección de `BORDER_REPLICATE`; `plt.xticks([])` |
| `U2/Ejercicios-20260923/PDI_U2_p2_stain.py` | Ecualizar un recorte (`img[f1:f2, c1:c2]` + `equalizeHist`), matriz booleana por umbral, `np.sum` por filas/columnas contra el máximo, `pathlib.Path`, validación de carga |
| `U2/Código-20260826/PI_U2_ej_blurred_face.py` | `np.full`, orden BGR de OpenCV |
| `U2/Código-20260826/PI_U2_ej_video_face_detection_and_blur.py` | `cv2.putText` |
| `U3/Código-20260923/PDI_U3_Segmentacion.py` | Umbralado manual, `connectedComponentsWithStats` y `stats`, `sorted(..., key=...)`, `findContours` con `RETR_TREE` y jerarquía, `cvtColor` de gris a color |
| `U1/PDI_U1_p1_Letras.py` | Inicio/fin de pulsos (`np.diff` + `np.argwhere` + `reshape`), recortes por índices, separar letras por columnas vacías, un archivo por elemento con f-string en un `for` |
| `U1/PDI_U1_Fundamentos_p1.py` | `cv2.imwrite` |
| Sin fuente en el material | Escritura del CSV con `open`/`write`; `np.vstack` |

---

## 7. Preguntas probables de la defensa (con respuesta corta)

1. **¿Por qué la ecualización global no revela los detalles y la local sí?** Los detalles difieren del fondo en pocos niveles y los píxeles oscuros son el 29 % de la imagen: en el histograma global quedan juntos al principio de la CDF y se mapean todos a valores bajos. La local calcula la CDF solo con los vecinos, donde esa diferencia mínima se estira a todo [0, 255].
2. **¿Por qué M y N impares?** Para que la ventana tenga un único píxel central (M = 2m + 1, N = 2n + 1).
3. **¿Por qué `BORDER_REPLICATE` y no ceros?** Replicar no agrega niveles de gris que la imagen no tiene; los ceros meterían negro artificial en el histograma de las ventanas del borde.
4. **¿Cómo influye el tamaño de ventana?** Muy chica: solo bordes y ruido de fondo. Muy grande: entra el fondo claro y el resultado se parece a la global. Rango útil acá: 15x15 a 31x31; se eligió 21x21.
5. **¿Qué ruido queda y por qué?** Los píxeles de nivel 226 del fondo (2,5 %) quedan negros, con cualquier ventana, porque son el nivel más bajo del fondo.
6. **¿Cómo encuentran las celdas de la tabla en el Problema 2?** Umbralan, suman por filas y columnas, y los picos (muchos más píxeles oscuros que el resto) son las líneas; con `pulsos` se obtienen inicio y fin de cada una.
7. **¿Cómo cuentan palabras sin leer texto?** Componentes conectadas ordenadas de izquierda a derecha; si el hueco entre dos caracteres supera 6 px hay un espacio (letras: 0 a 4 px; palabras: 10 a 13 px).
8. **¿Cómo distinguen L, R y A?** La L y la R tienen la primera columna de su caja completamente llena; la A no. La R además tiene un agujero (contorno con madre en `findContours` con `RETR_TREE`).
9. **¿Qué limitaciones tiene el Problema 2?** No lee caracteres; los umbrales están calibrados con estas cuatro planillas; el espacio del nombre no cuenta como caracter (decisión del grupo, a confirmar con la cátedra); la Ñ se contaría como dos componentes.
10. **¿Por qué se calcula RMSE/restas en `float` y no en `uint8`?** (Repaso de la Unidad 1, útil si preguntan por tipos de dato.) Porque `uint8` da la vuelta al pasarse de 0 o 255 (overflow) y la resta de dos imágenes daría valores sin sentido.
