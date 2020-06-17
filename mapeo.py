#%%

import ants
from nilearn import plotting
import os.path
import matplotlib
my_path = os.path.abspath(os.path.dirname(__file__))
#Para evitar problemas utilizamos la funcionalidad de os, para leer rutas. (Ruta relativa)
fixedPath = os.path.join(my_path, "../Datos/MNI152.nii.gz")
movedPath = os.path.join(my_path, "../Datos/Atlas/Site3/031865/t01/031865_t1w_deface_stx.nii.gz")
maskPath = os.path.join(my_path, "../Datos/Atlas/Site3/031865/t01/031865_LesionSmooth_stx.nii.gz")

'''
#Sirve para mostrar por pantalla o en una nueva ventana un "gráfico"
plotting.plot_glass_brain(movedPath)
matplotlib.pyplot.show()
'''
#Convertimos las imagenes a imagenes ants
fixed = ants.image_read(fixedPath)
moving = ants.image_read(movedPath)
mask = ants.image_read(maskPath)
# --fixed.plot(overlay=moving,title='Before Registration')

fixed = ants.resample_image(fixed, (64,64,64), 1, 0)
moving = ants.resample_image(moving, (64,64,64), 1, 0)
#Aplicamos la transformación para encajar ambas imagenes en las mismas dimensiones y espacio
mytx = ants.registration(fixed=fixed , moving=moving ,type_of_transform = 'SyN' )
mywarpedimage = ants.apply_transforms( fixed=fixed, moving=moving,transformlist=mytx['fwdtransforms'] )
#Guarda en el directorio especificado, la imagen ya transformada
#guardado = os.path.join(my_path, "../Datos/prueba.nii.gz")
#ants.image_write(mywarpedimage,guardado)
mascaraTransformada = ants.apply_transforms(mywarpedimage,mask,transformlist=mytx['fwdtransforms'],interpolator='nearestNeighbor')
#mask.plot(overlay=mascaraTransformada,title='After Registration')
#mask.plot(title='After Registration')
#prueba.plot(title='After Registration')
# %%
guardado = os.path.join(my_path, "../Datos/031865.nii.gz")
ants.image_write(mywarpedimage,guardado)
guardado2 = os.path.join(my_path, "../Datos/031865LesionMask.nii.gz")
ants.image_write(mascaraTransformada,guardado2)