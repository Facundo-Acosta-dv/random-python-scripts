#----------------------------------------------------------------------|#
from Models.bmxs import Bmx
from pynput.keyboard import Key, Listener
import os
import marcas as m
from time import *
from tools import *
 ###                        
  #####    ######  #### ### 
  ##  ##  ## ## ##  ##   #  
  ##  ##  ## ## ##   ####   
  ##  ##  ## ## ##   ###    
  ##  ##  ## ## ##  #  ##   
 ######   ## ## ## ###  ### 
                            
 ###               ###      
  #####   ### ###   #####   
  ##  ##   ##  ##   ##  ##  
  ##  ##   ##  ##   ##  ##  
  ##  ##   ##  ##   ##  ##  
  ##  ##   ##  ##   ##  ##  
 #### ###   ### ## ######   

 #### ###    ##    
  ##   #    ###    
  ##   #     ##    
  ##   #     ##    
   ## #      ##    
   ## #      ##    
    ##     ######  
## TOOLSET ##
def clear():
	return os.system("clear")

def val_minmax(min, max,mensaje="Ingrese un número"):
	x = val_int(mensaje)
	if x > max or x < min:
		clear()
		cooldown=2
		lateral_fade(f"Fuera de rango • {3} ")
		sleep(1)
		clear()
		for _ in range(cooldown):
			clear()
			print(f"Fuera de rango • {cooldown} ")
			cooldown-=1
			sleep(1)
	if x >= min and x <= max:
		return x

def inputless_val_minmax(min, max, numero):
	if numero > max or numero < min:
		clear()
		cooldown=2
		lateral_fade(f"Fuera de rango • {3} ")
		sleep(1)
		clear()
		for _ in range(cooldown):
			clear()
			print(f"Fuera de rango • {cooldown} ")
			cooldown-=1
			sleep(1)
		return None
	if numero >= min and numero <= max:
		return numero

def val_marca(mensaje="{mensaje}"):
	val = True
	while val:
		minput = input(mensaje+": ")

		for i in m.marcas:
			if minput.lower() == i.lower():
				val = False
				break

		if val == True:
			clear()
			lateral_fade("Marca no encontrada")
	return minput.capitalize()

def val_len(mensaje="{mensaje}", min= 4, max= 16):
	error_min=f"No puede contener menos de {min} caracteres"
	error_max=f"No puede contener mas de {max} caracteres"
	x = input(mensaje+": ").capitalize()
	if len(x) > max:
		clear()
		cooldown = 2
		lateral_fade(error_max, 0.02)
		print(f"{'':>16} •{3}•")
		sleep(1)
		for _ in range(cooldown):
			clear()
			print(f"{error_max}\n{'':>16} •{cooldown}•")
			cooldown -=1
			sleep(1)
			clear()
	if len(x) < min:
		clear()
		cooldown = 2
		lateral_fade(error_min, 0.02)
		print(f' {"":>16} •{3}•')
		sleep(1)
		for _ in range(cooldown):
			clear()
			print(f"{error_min}\n {'':>16} •{cooldown}•")
			cooldown -= 1
			sleep(1)
			clear()
	if len(x) <= max and len(x) >= min:
		return str(x)

def val_int(mensaje="Ingrese un numero"):
	val = True
	while val:
		try:
			x = int(input(mensaje+": "))
			val = False
		except ValueError:
			lateral_fade(f"Solo números • {3}",0.03)
			cooldown = 2
			sleep(1)
			for _ in range(cooldown):
				clear()
				print(f"Solo números • {cooldown}")
				cooldown -= 1
				sleep(1)
			return 'value_error'
	return x

### Funciones ##
catalogo = []
def shit():
	def agregar_bmx(marca, cuadro, manillar, horquilla, avance, dire):
		global catalogo
		bmx = Bmx(id, marca, cuadro, manillar, horquilla, avance, dire)
		catalogo.append(bmx)

		for i in range(len(catalogo)):
			print(catalogo[i].get_cuadro())

	marca = val_marca("Ingrese marca")
	cuadro = añadir_cuadro()
	manillar = val_marca("Ingrese marca")
	dire = val_marca("Ingrese marca")
	clear()
	horquilla = val_marca("Ingrese marca y modelo")
	avance = val_marca("Ingrese Marca del avance")

	agregar_bmx(marca,cuadro,manillar,horquilla,avance,dire)
	print(catalogo)

### añadir ##

bmx = Bmx(id, nombre="", cuadro="debug", manillar="debug", horquilla="debug", avance="debug", dire="debug")

def añadir_cuadro():
	#-cuadro
	def frame_size():
		sizes = ["20","20.25", "20.50", "20.75", "21"]
		val = True
		while val:
			clear()
			lateral_fade("	  Tamaño del cuadro", 0.02)
			clear()
			print(
				"	  Tamaño del cuadro\n",
				"20    20.25    20.50    20.75    21\n",
				"|       |        |        |      |\n",
				"1       2        3        4      5\n"
			)
			x = val_int()
			if x != 'value_error':
				x = inputless_val_minmax(1,5,x)
				if x != None: val = False
			match x:
				case 1:
					return sizes[0]
				case 2:
					return sizes[1]
				case 3:
					return sizes[2]
				case 4:
					return sizes[3]
				case 5:
					return sizes[4]
	#frame_size()
	def frame_model():
		clear()
		val = True
		while val:
			x = val_len("Modelo del cuadro")
			if x != None:
				val = False
				return x
	cuadro_marca = val_marca("Marca del cuadro")
	cuadro_modelo = frame_model()
	cuadro_tamaño = frame_size()
	x = cuadro_marca+" "+cuadro_modelo.lower()+" "+cuadro_tamaño
	bmx.set_cuadro(x)
añadir_cuadro()
catalogo.append(bmx)
bmx.set_nombre(f"bmx .{bmx.get_id()}")

print(catalogo)
for i, bmx in enumerate(catalogo):
	print(f"nombre: {catalogo[i].get_nombre()}")
	print(f"cuadro: {catalogo[i].get_cuadro()}")
	print(f"manillar: {catalogo[i].get_manillar()}")
	print(f"horquilla: {catalogo[i].get_horquilla()}")
	print(f"avance: {catalogo[i].get_avance()}")
	print(f"dire: {catalogo[i].get_dire()}")

	#ver val_marca y agregar un input que te dé la lista de las marcas
	#marca no encontrada, querrás decir .find(marca_ingresada)
	