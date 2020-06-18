import ants
from nilearn import plotting
import os.path
import matplotlib
from pathlib import Path
'''
Funcion: Transfor_image.
Params: imagePath - Path de la imagen a transformar.
return: mywarpedimage - Imagen transformada al template.
        mytx - Deformación, para ser más tarde aplicada a la mascara.
Función que se encarga de transformar la imagen original (t1) al espacio y dimensión de la template MNI152.nii.gz
'''
def Transform_Image(imagePath):
    #Necesario para que el relative path funcione de manera correcta,
    my_path = os.path.abspath(os.path.dirname(__file__))
    #Utilizamos la plantilla MANI152
    templatePath = os.path.join(my_path, "../Datos/MNI152.nii.gz")
    #Cargamos el path que recibe por parametro, si el path da erroneo, ha de cambiarse en el código de Busqueda.
    path = os.path.join(my_path, imagePath)
    #Leemos los paths y los transformamos en imagenes
    template = ants.image_read(templatePath)
    image = ants.image_read(path)
    #Reesamblamos
    template = ants.resample_image(template, (64,64,64), 1, 0)
    image = ants.resample_image(image, (64,64,64), 1, 0)
    #Realizamos la transformación
    mytx = ants.registration(fixed=template , moving=image ,type_of_transform = 'SyN' )
    mywarpedimage = ants.apply_transforms( fixed=template, moving=image,transformlist=mytx['fwdtransforms'] )
    return mywarpedimage,mytx
'''
Funcion: Transfor_Lesion_Mask
Params: LesionPath - Path de la lesión
        transform - Imagen del cerebro ya transformada.
        mytx - "Transformación relativa", tomada de referencia de la transformación inicial.
return: mywarpedimage - Imagen transformada al template.
Función que en base a la transformación sometida a la t1, hace una transformación nearestNeigthbor sobre la mascara de esa lesión
'''
def Transform_Lesion_Mask(LesionPath, transform, mytx):
    #Necesario para que el relative path funcione de manera correcta,
    my_path = os.path.abspath(os.path.dirname(__file__))
    #Cargamos el path que recibe por parametro, si el path da erroneo, ha de cambiarse en el código de Busqueda.
    path = os.path.join(my_path, LesionPath)
    #Leemos los paths y los transformamos en imagenes
    mask = ants.image_read(path)
    #Realizamos la transformación
    mascaraTransformada = ants.apply_transforms(transform,mask,transformlist=mytx['fwdtransforms'],interpolator='nearestNeighbor')
    return mascaraTransformada
'''
Función: Save_Images_Transformed
Paramas: 
Función que guarda las iamgenes tanto la mascara como la t1 ya transformadas, siguiendo el modelo de almacenamiento y carga que posteriormente va a tener el programa.
'''
def Save_Images_Transformed(nameSubject, ImageToSave, isT1,*cont):
        #cwd = Path.cwd()
        #Sacamos nuestra ruta actual
        mod_path = Path(__file__).parent

        #A través de una ruta relativa buscamos la carpeta de almacenamiento de datos.
        pathOfData =  str((mod_path / str("../Datos")))
        #Si data working no existe lo creamos
        if not (os.path.exists(str(pathOfData+"/DataWorking"))):
                os.mkdir(str(pathOfData+"/DataWorking"))

        pathOfData2 =  str((mod_path / str("../Datos/DataWorking")))
        #Si el sujeto no ha sido todavía creado, lo creamos (La carpeta)
        if not (os.path.exists(str(pathOfData2+"/"+nameSubject))):
                os.mkdir(str(pathOfData2+"/"+nameSubject))
        #Si es la imagen transformada...
        if(isT1):
                #Creamos la ruta de donde guardarlo 
                savePath = (mod_path / str("../Datos/DataWorking/"+nameSubject+"/"+nameSubject+"_t1.nii.gz")).resolve()
                #Lo guardamos, se hace el casteo para evitar errores con pathlib
                ants.image_write(ImageToSave,str(savePath))
        #Si no es la imagen, es la mascara de la lesión.
        else:
                savePath = (mod_path /  str("../Datos/DataWorking/"+nameSubject+"/"+nameSubject+"_lesson["+str(cont[0])+"].nii.gz")).resolve()
                ants.image_write(ImageToSave,str(savePath))
