import os
import numpy as np
from laspy.file import File
import laspy
import rasterio
from PIL import Image

imgs_path = '/Users/bound_to_love/Downloads/train/RemoteSensing/LAS/'

def process_img(filename, show=False):
    with File(imgs_path+filename, mode='r') as inFile:
        print(filename)
        print(inFile.header.data_format_id)
        print(inFile)
        I = inFile.Classification == 2
        print(type(I))
        for spec in inFile.reader.point_format:
            print("Copying dimension: " + spec.name)
            in_spec = inFile.reader.get_dimension(spec.name)
            print(np.shape(in_spec))
            print(in_spec)
        '''
        outFile = File(imgs_path+"out_"+filename, mode='w', header=inFile.header)
        outFile.points = inFile.points[I]
        outFile.close()
        '''

imgs = [f for f in os.listdir(imgs_path) if '.las' in f]

# Read just one image
process_img(imgs[0], show=True)

# Read ALL images
#[process_img(f) for f in imgs]
