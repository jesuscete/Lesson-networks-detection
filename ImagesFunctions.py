import numpy as np
from scipy import stats
import ImagesFunctions as imf
import pandas as pd
from nistats.second_level_model import SecondLevelModel

'''
 Params: coord, Coordenadas a transformar.
 return: Matriz de las coordendas.
 Función simple que transforma las coordenadas de un array a una matriz
'''
def arraysCoord_To_MatrixCoord(coord):
    return (np.asmatrix(coord))
'''
Params: MatrixA, Primera matriz a la hora de hacer la intersección.
        MatrixB, Segunda matriz de la hacer la intersección.
Función que crea la intersección entre dos matrices.
'''
def Intersect_Column_Matrix(matrixA,matrixB):
    aTranspose = matrixA.transpose()
    bTranspose = matrixB.transpose()
    container = list()
    for row in bTranspose:
        if row in aTranspose:
            container.append(np.array(row))
    matrizResultado = np.asmatrix(np.array(container)).transpose()
    return matrizResultado
'''
params: Mcoord, Coordendas originales del timeserie
        Mintersetc, Coordenadas de la intersección con la lesión.
return: resultado, Lista de todos los indices
Función que recibe como parametros las coordenadas y devuelve una lista con los indices de las columnas
para el timeserie
'''
def Return_Index_Coord_Column(Mcoord, Mintersect):
    resultado = list()
    McoordT = np.array(Mcoord.transpose())
    MintersectT = np.array(Mintersect.transpose())
    cont=0
    for r in McoordT:
        for c in MintersectT:
            if(np.array_equal(c,r)):
                resultado.append(cont)
        cont+=1
        
    return resultado

def SeedTimeseries_return(timeseries, indices):
    SeedTimeseries = np.mean(timeseries[:,indices],axis=1)
    return SeedTimeseries
'''
Params: MatrixA, Primera matriz a la hora de hacer la intersección.
        MatrixB, Segunda matriz de la hacer la intersección.
Función que crea la intersección entre dos matrices.
'''
def Return_List_Index_coord(CoordTs,CoordLesion):
    coordTsT = CoordTs.transpose()
    CoordLesionT = CoordLesion.transpose()
    indexCoordIntersect = list()
    for row in CoordLesionT:
        if(row in coordTsT):
            indexCoordIntersect = np.where(coordTsT == row)[0]
    '''    
    for rowa in coordTsT:
        cont=0
        if rowa in CoordLesionT:
            for rowb in CoordLesionT:
                if(np.array_equal(rowb,rowa)):
                    indexCoordIntersect.append(cont)
                    break                  
                cont+=1
    '''
    return list(indexCoordIntersect)
'''
Params: timeseres, Timeserie completo, sin las coordendas.
        indicesTimesereis, Los indices donde la lesión coincide con el timeserie.
return: stat_Map_List, lista de los stat maps individuales de cada timeserie.
Funcion que lleva a cabo la correlación de pearson para sacar la conectividad de la lesión en base al timeserie, recorre todos los timeseries
y devuelve una lista con todos los mapas disponibles para una sola lesión.
'''
def Get_Pearson_Correlation(timeseries, indiceTimeseries):
    stat_Map_List = list()
    zfisher_Map = list()
    for ind in range(len(timeseries)):
        
        seed_timeseries = imf.SeedTimeseries_return(timeseries[ind],indiceTimeseries[ind])
        timeseriesT = timeseries[ind].transpose()
        stat_map = np.zeros(timeseriesT.shape[0])
        for i in range(timeseriesT.shape[0]):
            stat_map[i] = stats.pearsonr(seed_timeseries, timeseriesT[i])[0]
        stat_map[np.where(np.mean(timeseriesT,axis=1) == 0)] = 0
        stat_Map_List.append(stat_map)
        zfisher_Map.append(transform_Data_To_fisher_z(stat_map))
    return stat_Map_List,zfisher_Map
def transform_Data_To_fisher_z(stat_map):
    fisherZ_Matrix = np.arctanh(stat_map)
    return fisherZ_Matrix

def oneSample_ttest(map_list):
    design_matrix = pd.DataFrame([1]* len(map_list), columns=['intercept'])
    second_level_model = SecondLevelModel().fit(
    map_list, design_matrix=design_matrix)
    z_map = second_level_model.compute_contrast(output_type='z_score')
    return z_map