import glob, os
import ants
from pathlib import Path
import numpy as np
import nibabel as nib
def Load_Timeseries():
    mod_path = Path(__file__).parent
    #A través de una ruta relativa buscamos la carpeta de almacenamiento de datos.
    pathOfData =  str((mod_path / str("../Datos/timeseries_N10")).resolve())
    os.chdir(pathOfData)
    #Partiendo de la estructura: ../DatosOriginales/sujeto/t01/Imagenes
    #Cargamos todos los sujetos
    subjects = glob.glob("**")
    #Cargamos con numpy, la matriz de dentro del fichero.
    matriz = np.loadtxt(pathOfData+"/"+subjects[0])
    #Separamos de la matriz el timeseries de sus coordenadas.
    coordenadas = matriz[0:3]
    timeseries = matriz[3:]
    #print("Matriz coordenadas:\n", coordenadas)
    #print("timeseries:\n",timeseries)
    return coordenadas,timeseries

def Load_Coord_Example():
    cwd = Path.cwd()
    mod_path = Path(__file__).parent
    #A través de una ruta relativa buscamos la carpeta de almacenamiento de datos.
    pathOfData =  str((mod_path / '../Datos/DataWorking/031768').resolve())
    os.chdir(pathOfData)
    #Cargamos con numpy, la matriz de dentro del fichero.
    ImageExample = nib.load(pathOfData+"/031768_lesson[1].nii.gz")
    mascaraMatriz = ImageExample.get_fdata()
    x,y,z = np.where(mascaraMatriz != 0)
    return ImageExample,x,y,z
