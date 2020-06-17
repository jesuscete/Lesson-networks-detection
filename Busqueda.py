import glob, os
my_path = os.path.abspath(os.path.dirname(__file__))
movedPath = os.path.join(my_path, "../Datos/DatosOriginales/")
os.chdir(movedPath)
subjects = glob.glob("**")
for i in subjects:
    #print(i)
    cadena = str(i+"/t01")
    os.chdir(movedPath+cadena)
    brainImage = glob.glob("*.gz")
    for j in brainImage:
        print(j)
    #if("LesionSmooth" in i):
    #    print(i)