import numpy as np
import Load_Data as ld
coord, timeseries = ld.Load_Timeseries()
coord = np.int_(coord)
seed_timeseries = np.mean(timeseries[coord],axis=0)