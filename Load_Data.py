import glob, os
import ants
from pathlib import Path
import numpy as np
import nibabel as nib
import ImagesFunctions as imf
def Load_Timeseries():
    #Inicializamos listas:
    coordenadas = list()
    timeseries = list()
    indicesForSeedTs = list()
    mod_path = Path(__file__).parent
    #A través de una ruta relativa buscamos la carpeta de almacenamiento de datos.
    pathOfData =  str((mod_path / str("../Datos/timeseries_N10")).resolve())
    os.chdir(pathOfData)
    #Partiendo de la estructura: ../DatosOriginales/sujeto/t01/Imagenes
    #Cargamos todos los sujetos
    subjects = glob.glob("**")
    for subject in subjects:
    #Cargamos con numpy, la matriz de dentro del fichero.
        matriz = np.loadtxt(pathOfData+"/"+str(subject))
        #Separamos de la matriz el timeseries de sus coordenadas.
        coordenadasSubject =matriz[0:3]
        timeseriesSubject = matriz[3:]
        mascaraMatriz,coordenadasLesion = Load_Coord_Example()
        indices = imf.Return_List_Index_coord(coordenadasSubject,coordenadasLesion)
        indicesForSeedTs.append(indices)
        coordenadas.append(coordenadasSubject)
        timeseries.append(timeseriesSubject)
        #print("Matriz coordenadas:\n", coordenadas)
    #print("timeseries:\n",timeseries)
    return coordenadas,timeseries, indicesForSeedTs, mascaraMatriz

def Load_Coord_Example():
    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    #A través de una ruta relativa buscamos la carpeta de almacenamiento de datos.
    pathOfData =  str((mod_path / '../Datos/DataWorking/031768').resolve())
    os.chdir(pathOfData)
    #Cargamos con numpy, la matriz de dentro del fichero.
    ImageExample = nib.load(pathOfData+"/031768_lesson[1].nii.gz")
    mascaraMatriz = ImageExample.get_fdata()
    coords = np.where(mascaraMatriz != 0)
    matrixCoord = imf.arraysCoord_To_MatrixCoord(coords)
    return ImageExample,matrixCoord
def return_template():
    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    #Utilizamos la plantilla MANI152
    pathOfData =  str((mod_path / '../Datos/MNI152.nii.gz').resolve())
    return np.array(ants.image_read(pathOfData))