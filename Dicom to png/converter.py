import numpy as np
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_modality_lut
from PIL import Image

ds = pydicom.dcmread('image.dicom')


new_image = ds.pixel_array.astype(float)

mod = apply_modality_lut(new_image, ds)

voi = apply_voi_lut(mod, ds)



scaled_image = (np.maximum(voi, 0) / voi.max()) * 255.0

scaled_image = np.uint8(scaled_image)

final_image = Image.fromarray(scaled_image)

final_image.save('image.png')


