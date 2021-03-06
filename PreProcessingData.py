import glob, os
import transformeAndSave as ts
import ants
#Necesario para que el sistema de rutas aleatorio funcione de manera correcta
my_path = os.path.abspath(os.path.dirname(__file__))
#Almacenamiento de datos adaptable a su disposición
movedPath = os.path.join(my_path, "../Datos/DatosOriginales/")
os.chdir(movedPath)
#Partiendo de la estructura: ../DatosOriginales/sujeto/t01/Imagenes
#Cargamos todos los sujetos
subjects = glob.glob("**")
#Recorremos los sujetos
for subject in subjects:
    #Creamos la cadena path
    cadena = str(subject+"/t01")
    #Evita problemas con los paths relativos y absolutos
    os.chdir(movedPath+cadena)
    #Dentro de la carpeta t01 del sujeto concreto, buscamos todas las imagenes
    brainImage = glob.glob("*.gz")
    lesionList = list()
    for j in brainImage:
        #Si no es una lesión le hacemos la transformada al template (Siempre se trata primero la imagen del cerebro concreto pues necesitamos "trans" para la mascara)
        if not ("Lesion" in j):
            pathToFunction = os.path.join(my_path, "..")
            os.chdir(pathToFunction)
            stringImage= glob.glob("Datos/DatosOriginales/"+cadena+"/"+j)[0]
            #Llamamos a la función que realiza la transformación con el template.
            print("Procesando la t1 de "+subject+"...")
            imagenTransf,mytx = ts.Transform_Image("../"+str(stringImage))
        #Si es una lesión lo guardamos en una lista para cuando terminemos con el sujeto
            print("Guardando la t1 de "+subject+"...")
            ts.Save_Images_Transformed(subject,imagenTransf,True)
            print("FINALIZADO")
        else:
            pathToFunction = os.path.join(my_path, "..")
            os.chdir(pathToFunction)
            stringLesion= glob.glob("Datos/DatosOriginales/"+cadena+"/"+j)[0]
            lesionList.append(stringLesion)
    cont=1
    for lesion in lesionList:
        print("Procesando las mascaras de las lesiones de "+subject+"... ["+str(cont)+"]")
        mascaraTransf = ts.Transform_Lesion_Mask("../"+lesion,imagenTransf,mytx)
        print("Guardando las mascaras de las lesiones de "+subject+"... ["+str(cont)+"]")
        ts.Save_Images_Transformed(subject,mascaraTransf,False,cont)
        cont+=1
    print("Finalizado")
        
