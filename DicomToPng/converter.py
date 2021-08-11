import numpy as np
#from image_utils import imgtonumpy, numpytoimg, normalization, shape_as
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_modality_lut
from PIL import Image

ds = pydicom.dcmread('image.dicom')


new_image = ds.pixel_array.astype(float)

lut = pydicom.pixel_data_handlers.util.apply_modality_lut(new_image, ds)
lut = pydicom.pixel_data_handlers.util.apply_voi_lut(lut, ds)
#lut = normalization(lut)
if ds[0x0028,0x0004].value == "MONOCHROME1":
	lut = -1*(lut-255)
#lut = shape_as(lut)

scaled_image = (np.maximum(voi, 0) / voi.max()) * 255.0

scaled_image = np.uint8(scaled_image)

final_image = Image.fromarray(scaled_image)

final_image.save('image.png')


