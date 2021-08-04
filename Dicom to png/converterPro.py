import os
import numpy as np
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_modality_lut
from PIL import Image

def get_names(path):
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dicom']:
                names.append(filename)
    
    return names



def convert_dcm_png(name):
    
    ds = pydicom.dcmread('/home/tunit/Desktop/Dataset_Dicom/'+name)
    
    img = ds.pixel_array.astype(float)
    mod = apply_modality_lut(img, ds)
    voi = apply_voi_lut(mod, ds)
    rescaled_image = (np.maximum(voi,0)/voi.max()) * 255.0 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels

    final_image = Image.fromarray(final_image)

    return final_image


names = get_names('/home/tunit/Desktop/Dataset_Dicom')
for name in names:
    image = convert_dcm_png(name)
    image.save(name+'.png')    