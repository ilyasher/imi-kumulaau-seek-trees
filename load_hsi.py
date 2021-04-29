import numpy as np
import rasterio
import os
import matplotlib.pyplot as plt

imgs_path = '../data/IDTREES_competition_test_v2/task1/RemoteSensing/HSI/'
output_path = '..'


def process_img(filename, show=False):
    with rasterio.open(os.path.join(imgs_path, filename)) as dataset:

        h, w = dataset.shape
        band_number = dataset.count
        img_array = np.zeros((h, w, band_number))

        # Flexible to number of bands in image cube
        for i in range(band_number):
            band = dataset.read(i + 1)
            img_array[:, :, i] = band

        img_array = img_array.astype(np.uint8)

    if show:  # Will show spectrum for top left corner of the image cube as a test
        plt.plot(np.asarray(range(band_number)), img_array[0,0,:])
        plt.show()


imgs = [f for f in os.listdir(imgs_path) if '.tif' in f]

# Read just one image
process_img(imgs[0], show=True)