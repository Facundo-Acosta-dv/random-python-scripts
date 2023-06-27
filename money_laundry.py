import time
import os
# .88b  d88.  .d88b.  d8b   db d88888b db    db              
# 88'YbdP`88 .8P  Y8. 888o  88 88'     `8b  d8'              
# 88  88  88 88    88 88V8o 88 88ooooo  `8bd8'               
# 88  88  88 88    88 88 V8o88 88~~~~~    88                 
# 88  88  88 `8b  d8' 88  V888 88.        88                 
# YP  YP  YP  `Y88P'  VP   V8P Y88888P    YP                 
#    db       .d8b.  db    db d8b   db d8888b. d8888b. db    db 
#    88      d8' `8b 88    88 888o  88 88  `8D 88  `8D `8b  d8' 
#    88      88ooo88 88    88 88V8o 88 88   88 88oobY'  `8bd8'  
#    88      88~~~88 88    88 88 V8o88 88   88 88`8b      88    
#    88booo. 88   88 88b  d88 88  V888 88  .8D 88 `88.    88    
#    Y88888P YP   YP ~Y8888P' VP   V8P Y8888D' 88   YD    YP    
#
#500 cada 7 días, 500 cada 30 días
#actual = 0
#meta y tiempo para meta
#---objetivos---#
#conversor a años, gui, días por meses exactos
#meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
power = True
while power:

	def val(msg="input"):
		val = True
		while val:
			try:
				x = int(input(msg))
				val = False
			except ValueError:
				print("ingresá una cifra, down")
				val = True
		return x

	plata_por_semana = val("plata x semana: ")

	def val_plata(msg="input: "):
		global plata_por_mes
		val = True
		while val:
			try:
				x = int(input(msg))
				val = False
			except ValueError:
				print("dame una cifra, down")
				val = True
			if x < plata_por_semana:
				print(f"no puede ser menor a ${plata_por_mes} pesos")
				val = True
		return x

	meta = val("meta de plata: ")
	dias_meta = int(meta / (plata_por_semana/7))

	#
	if dias_meta < 7: #in case of bug
		x = "" 

	#semanas
	if dias_meta >= 7:
		count = dias_meta / 7
		aprox = " aprox" if count % 2 else ""
		intermedio = int(count*7 - int(count)*7)
		if intermedio > 3 and intermedio < 5:
			aprox = " y medio aprox"
		if intermedio >= 5:
			aprox = " aprox"
			count += 1
		count = int(count)
		singular = f"(una semana{aprox})"
		plural = f"({count} semanas{aprox})"
		x = singular if count == 1 else plural
	#meses
	if dias_meta >= 30:
		count = dias_meta / 30
		aprox = " aprox" if count % 2 else ""
		intermedio = int(dias_meta - int(count)*30)
		if intermedio > 11 and intermedio < 20:
			aprox = " y medio aprox"
		if intermedio >= 20:
			aprox =  " aprox"
			count += 1
		count=int(count)
		singular = f"(un mes{aprox})"
		plural = f"({count} meses{aprox})"
		x = singular if count == 1 else plural

	#años
	if dias_meta >= 365:
		count = dias_meta / 365
		aprox = " aprox" if count % 2 else ""
		intermedio = (count*365 - 365*int(count))
		if intermedio > 0 and intermedio < 160:
			aprox = (" aprox")
		if intermedio > 160 and intermedio < 240:
			aprox = (" y medio aprox")
		if intermedio > 240:
			aprox = (" aprox")
			count += 1
		count = int(count)
		singular = f"(un año{aprox})"
		plural = f"({count} años {aprox})"
		x = singular if count == 1 else plural

	print(f"Faltan {dias_meta} días para conseguir ${meta} pesos{x}")
	time.sleep(2)
	input("introduzca una tecla para continuar...")
	os.system("clear")
