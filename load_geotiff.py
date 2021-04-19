import numpy as np
import rasterio
import os
from PIL import Image

imgs_path = './data/IDTREES_competition_test_v2/task1/RemoteSensing/RGB/'
output_path = './out'

def process_img(filename, show=False):
    with rasterio.open(os.path.join(imgs_path, filename)) as dataset:

        h, w = dataset.read(1).shape
        img_array = np.zeros((h, w, 3))

        # 3 color channels in RGB
        for i in range(3):
            band = dataset.read(i+1)
            img_array[:, :, i] = band

        img_array = img_array.astype(np.uint8)

        img = Image.fromarray(img_array)
        if show:
            img.show()

        img.save(os.path.join(output_path, filename))

imgs = [f for f in os.listdir(imgs_path) if '.tif' in f]

# Read just one image
process_img(imgs[0], show=True)

# Read ALL images
[process_img(f) for f in imgs]