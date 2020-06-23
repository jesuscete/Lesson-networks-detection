import numpy as np
import Load_Data as ld
import ants
import nibabel as nib
import ImagesFunctions as imf
from scipy import stats
from nilearn import plotting
import matplotlib
coord, timeseries = ld.Load_Timeseries()

coord = np.int_(coord)
mascaraMatrix, coordMatrix= ld.Load_Coord_Example()
coordTimeserie = imf.Intersect_Column_Matrix(coord,coordMatrix)
indiceTimeseries = imf.Return_Index_Coord_Column(coord,coordTimeserie)
seed_timeseries = imf.SeedTimeseries_return(timeseries,indiceTimeseries)
timeseries = timeseries.transpose()
stat_map = np.zeros(timeseries.shape[0])
for i in range(timeseries.shape[0]):
    stat_map[i] = stats.pearsonr(seed_timeseries, timeseries[i])[0]
stat_map[np.where(np.mean(timeseries,axis=1) == 0)] = 0
