import os
import numpy as np
from image_utils import imgtonumpy, numpytoimg, normalization, shape_as
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
from pydicom.pixel_data_handlers.util import apply_modality_lut
from registration import registration
from PIL import Image

target = np.asarray('image1.png')
ref = np.asarray('reference.png')
target = registration(target, ref)
ref = Image.fromarray(ref)
ref = ref.convert("L")
target = Image.fromarray(target)
target = target.convert("L")
target.save('registered.png')

