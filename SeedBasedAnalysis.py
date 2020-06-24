import numpy as np
import Load_Data as ld
import ants
import nibabel as nib
import ImagesFunctions as imf
from scipy import stats
from nilearn import plotting
import matplotlib
from timeit import default_timer
startTime = default_timer()
coord, timeseries, indiceTimeseries,coordMatrix  = ld.Load_Timeseries()
print('Este es el dato que buscas jeje',timeseries[1].shape)
coord = np.int_(coord)
time2 = default_timer()
print("Tiempo en cargar los datos: ", time2-startTime)
print('Longitud de la lista de timeseries', len(timeseries))

stat_map_list = imf.Get_Pearson_Correlation(timeseries, indiceTimeseries)
time3 = default_timer()
print("Tiempo que tarda en hacer el analisis: ", time3-time2)