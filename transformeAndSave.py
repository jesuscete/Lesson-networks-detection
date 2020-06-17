import ants
from nilearn import plotting
import os.path
import matplotlib

'''
Funcion: Transfor,_image
Params: imagePath - Path de la imagen a transformar.
return: mywarpedimage - Imagen transformada al template
        mytx - Deformación, para ser más tarde aplicada a la mascara.
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