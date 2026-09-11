import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Segundo/Procesamiento de Imagenes I/U2 - Transformacion y Filtrado/Ejercicios/john_canny_bio.png',cv2.IMREAD_GRAYSCALE)
-+
plt.figure()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()


