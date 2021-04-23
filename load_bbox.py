
import shapefile # pip3 install pyshp
import pandas as pd
import re
from collections import defaultdict

mlbs_shp_path = "../data/IDTREES_competition_train_v2/ITC/train_MLBS"
osbs_shp_path = "../data/IDTREES_competition_train_v2/ITC/train_OSBS"
csv_path = "../data/IDTREES_competition_train_v2/Field/itc_rsFile.csv"

def read_bbox(mlbs_shp_path, osbs_shp_path, csv_path):

    mlbs_shape = shapefile.Reader(mlbs_shp_path)
    osbs_shape = shapefile.Reader(osbs_shp_path)

    record_shapes = defaultdict(list)
    for feature in mlbs_shape.shapeRecords():
        record_shapes[feature.record.indvdID].append(feature.shape.bbox)
    for feature in osbs_shape.shapeRecords():
        record_shapes[feature.record.indvdID].append(feature.shape.bbox)

    refs = pd.read_csv(csv_path)
    refs['rsFile'] =  [re.sub("\.tif.*$", "", x) for x in refs['rsFile']]
    id_filename = dict(zip(refs['id'], refs['rsFile']))
    indvdid_filename =dict(zip(refs['indvdID'], refs['rsFile']))

    img_bounding_box = defaultdict(list)
    for key, value in record_shapes.items():
        fname = indvdid_filename[key]
        img_bounding_box[fname].extend(value)
    
    return img_bounding_box

'''
Returns a dictionary with filenames corresponding to a list of bounding boxes.
The filenames are the prefixes without the endings (e.g. MLBS_1 not MLBS_1.tif or MLBS_1.las).
The bounding boxes are xmin, ymin, xmax, ymax.
'''
img_bounding_boxes = read_bbox(mlbs_shp_path, osbs_shp_path, csv_path)
# print(len(img_bounding_boxes)) # length only 83 when there are 85 images?
