import glob, os
my_path = os.path.abspath(os.path.dirname(__file__))
movedPath = os.path.join(my_path, "../Datos/Atlas/Site3/")
os.chdir(movedPath)
imagenes = glob.glob("**/**/*.nii.gz")
for i in imagenes:
    if("LesionSmooth" in i):
        print(i)