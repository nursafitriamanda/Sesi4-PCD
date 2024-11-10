import imageio as img
import numpy as np
from scipy.ndimage import rotate, zoom
import matplotlib.pyplot as plt

def rotate_image(image, degree, scale_factor=1.0):
    # Rotasi gambar menggunakan scipy.ndimage.rotate
    rotated_image = rotate(image, degree, reshape=False)
    
    # Memperbesar/memperkecil gambar menggunakan scipy.ndimage.zoom
    zoomed_image = zoom(rotated_image, (scale_factor, scale_factor, 1))
    
    return zoomed_image

image = img.v2.imread("c://Users//allya saffira//Documents//download.jpg")

# Menampilkan gambar asli dan gambar yang dirotasi 90 derajat
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")

plt.subplot(1, 2, 2)
rotated_image = rotate_image(image, 90, scale_factor=1.2)
plt.imshow(rotated_image)
plt.title("Rotasi 90 Derajat")

plt.show()