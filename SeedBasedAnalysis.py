import numpy as np
import Load_Data as ld
import ants
import nibabel as nib
#coord, timeseries = ld.Load_Timeseries()
#coord = np.int_(coord)
mascaraMatrix, x,y,z = ld.Load_Data_Example()


#seed_timeseries = np.mean(timeseries[coord],axis=0)