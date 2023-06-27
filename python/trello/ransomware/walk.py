import os
#note that this script creates a txt and the following encrypter doesnt encrypt any files-
#other than the target.txt itself
r="/"
trg_extension=".py"
target=[]
all_dirs=[]
count=0

def write_target(list):
	with open("target.txt", "a") as trg:
		for i in list:
			x=i.replace("'","")+"\n"
			trg.write(x)

def search(ruta):
	global count, target
	for dir, _, files in os.walk(ruta):
		for f in files:
			fullp=str(dir+f)
			all_dirs.append(fullp)
			if f.endswith(trg_extension):
				l=dir+f
				print(f)
				target.append(l)
				count += 1
			if count >= 10000:
				count = 0
				write_target(target)
				target=[]
	write_target(target)

def write_dirs(list):
	with open("all_dirs.txt", "a") as txt:
		for i in list:
			x=i.replace("'","")+"/n"
			txt.write(x)

search(r)
write_target(target)
write_dirs(all_dirs)