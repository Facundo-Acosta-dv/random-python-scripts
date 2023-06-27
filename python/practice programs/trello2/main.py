def val_int(mensaje="Ingrese un numero"):
	val = True
	while val:
		try:
			x = int(input(mensaje+": "))
			val = False
		except ValueError:
			print("Solo números")
			val = True
	return x
val_int()
