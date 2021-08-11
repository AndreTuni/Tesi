import matplotlib.pyplot as plt

import pydicom



ds= pydicom.dcmread('img2.dicom')

plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
