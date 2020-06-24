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
for ind in range(len(timeseries)):
    seed_timeseries = imf.SeedTimeseries_return(timeseries[ind],indiceTimeseries[ind])
    timeseriesT = timeseries[ind].transpose()
    stat_map = np.zeros(timeseriesT.shape[0])
    for i in range(timeseriesT.shape[0]):
        stat_map[i] = stats.pearsonr(seed_timeseries, timeseriesT[i])[0]
    stat_map[np.where(np.mean(timeseriesT,axis=1) == 0)] = 0
time3 = default_timer()
print("Tiempo que tarda en hacer el analisis: ", time3-time2)