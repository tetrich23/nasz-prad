import numpy as np
import matplotlib.pyplot as plt

# Parametry fraktala
width, height = 800, 800
max_iter = 256
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5

# Funkcja generująca fraktal Mandelbrota
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Tworzenie obrazu fraktala
def generate_fractal(width, height, xmin, xmax, ymin, ymax, max_iter):
    # Tworzymy obraz o wymiarach width x height
    image = np.zeros((height, width))
    
    # Skalowanie na współrzędne
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    
    for i in range(height):
        for j in range(width):
            c = x[j] + 1j * y[i]
            image[i, j] = mandelbrot(c, max_iter)
    
    return image

# Generowanie fraktala
image = generate_fractal(width, height, xmin, xmax, ymin, ymax, max_iter)

# Wizualizacja
plt.imshow(image, cmap='twilight_shifted', extent=(xmin, xmax, ymin, ymax))
plt.colorbar()
plt.title("Fraktal Mandelbrota")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
