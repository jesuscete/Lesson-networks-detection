import numpy as np
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

