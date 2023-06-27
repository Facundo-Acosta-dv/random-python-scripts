import os

ruta = "/"
for dir, _, files in os.walk(ruta):
    for file in files:
        print(os.path.join(dir, file))
