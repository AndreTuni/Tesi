import os
import numpy as np
from image_utils import imgtonumpy, numpytoimg, normalization, shape_as
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_modality_lut
from registration import registration
from PIL import Image


'''script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "1.dicom"
abs_file_path = os.path.join(script_dir, rel_path)'''

#ds = pydicom.dcmread('1.dicom')
'''cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("\n Files in %r: %s" % (cwd, files))'''

ds = pydicom.dcmread('4.dicom')
new_image = ds.pixel_array.astype(float)

lut = pydicom.pixel_data_handlers.util.apply_modality_lut(new_image, ds)
lut = pydicom.pixel_data_handlers.util.apply_voi_lut(lut, ds)
lut = normalization(lut)
if ds[0x0028,0x0004].value == "MONOCHROME1":
	lut = -1*(lut-255)
lut = shape_as(lut)

scaled_image = (np.maximum(lut, 0) / lut.max()) * 255.0

scaled_image = np.uint8(scaled_image)

final_image = Image.fromarray(scaled_image)

final_image.save('image4.png')



