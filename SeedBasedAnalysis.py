import numpy as np
import Load_Data as ld
import ants
import nibabel as nib
import ImagesFunctions as imf
from scipy import stats
from nilearn import plotting,datasets
import matplotlib
from timeit import default_timer
startTime = default_timer()
stat_map_list = list()
coord, timeseries, indiceTimeseries,coordMatrix  = ld.Load_Timeseries()
coord = np.int_(coord)
time2 = default_timer()

print("Tiempo en cargar los datos: ", time2-startTime)
stat_map_list, zfisher_list = imf.Get_Pearson_Correlation(timeseries, indiceTimeseries)
print(stat_map_list[0].shape)
print("Matriz zfisher", np.asmatrix(zfisher_list[0]).shape)
fsaverage = datasets.fetch_surf_fsaverage()
print(fsaverage['pial_left'])
time3 = default_timer()
print("Tiempo que tarda en hacer el analisis: ", time3-time2)
x = imf.oneSample_ttest(zfisher_list,timeseries,coord)