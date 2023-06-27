
# 3 primeras cuevas - no dragon
# 4ta cueva en adelante - 1% de encontrar dragon
# no dragon = 10 monedas
# si dragon, puede salir del juego o luchar lo cual
# consume 50% de su vida total o pagar 100 monedas para ver otra cueva.
# registrar cuantos dragones mato
# el juego se termina si la vida del jugador llega a 0, si el dinero llega a 0 o si el jugador se va

# final imprimir
# nombre
# vida
# dinero
# dragones muertos
# cuevas visitadas
# contenido de la siguiente cueva

def validador(mensaje):
	val = True
	while val:
		try:
			validando = int(input(mensaje))
			val = False
		except ValueError:
			print("solo numeros")
			val = True
	return validando

def rangeado(desde, hasta, mensaje):

	val = True
	while val:
		try:
			validando = int(input(mensaje))
			val = False
			if validando < desde or validando > hasta:
				os.system("cls")
				val = True

		except ValueError:
			os.system("cls")
			val = True
	return validando

import os
import random
import time

dinero = 1000
vida = 100
fs = 0 #failstack
probability = 0.5
dragones_muertos = 0
cuevas_visitadas = 0
menu = True
chance = 0

def dragon():

    global menu
    global vida
    global dinero
    global dragones_muertos

    val = True

    while val:
        val2 = True
        os.system("cls")
        eleccion = rangeado(1, 3, "Un dragón acecha...\n"
        "---------------------\n"
        "1•Enfrentar  2•Ver otra cueva  3•Terminar juego\n")
        os.system("cls")
        while val2:
            match eleccion:
                case 1:
                    vida /= 2
                    if vida < 1:
                        val2 = False
                        val = False
                        menu = False
                    dinero += 100
                    dragones_muertos += 1
                    print("----------------------------------------------------")
                    print("luchas con el dragon y tu salud se reduce en un 50%!")
                    print(f"+100$ \n Dinero actual: {dinero} \n Hp: {int(vida)}\n")
                    input("presiona una tecla para continuar...")
                    os.system("cls")
                    val = False
                    val2 = False
                case 2:
                    pagar = True
                    while pagar:
                        elegir = rangeado(1, 2,
                            "Desea pagar $100 para ver otra cueva?\n"
                            "1• Si  2• No\n"
                            f"Dinero actual: {dinero}\n"
                            )
                        if elegir == 1:
                            print("$-100")
                            print("")
                            dinero -= 100
                            if dinero < 1:
                                menu = False
                            pagar = False
                            val = False
                            val2 = False
                        if elegir == 2:
                            os.system("cls")
                            pagar = False
                            val2 = False
                case 3:
                    val2 = False
                    val = False
                    menu = False


def buscar_cueva():

    global chance
    global rng
    global probability
    global fs
    global dinero
    global cuevas_visitadas

    buscar = True
    while buscar:

        chance = probability + fs if chance < 80 else 80

        rng = round(random.random() * (100 - 1 + 1) + 1, 1)
        #print(f"failstack = {math.ceil(fs) }")
        #print(f"dragon chance: {chance}%")
        print(
        "Exploras las profundidades de la cueva...\n"
        )
        time.sleep(1)
        os.system("cls")

        if rng < chance and cuevas_visitadas > 3:
            fs = 0
            dragon()

        fs += 8
        dinero += 10
        print("Has explorado la cueva!\n"
        "$+10\n"
        )
        print("")
        input("Presione una tecla para continuar... ")
        os.system("cls")

        buscar = False

        cuevas_visitadas += 1


while menu:
    os.system("cls")
    print("------------------------")
    print(
    f"Hp: {int(vida)}\n"
    f"Dinero actual: {dinero}\n")
    if cuevas_visitadas > 3:
        print(f"Probabilidad de dragon en siguiente cueva: {int(chance)}%")

    menu_elegir = rangeado(1, 2,
    "-------------------------\n"
    "1•Explorar cueva  2•Terminar juego\n"
    "\n"
    "Que desea hacer? "
    )
    match menu_elegir:
        case 1:
            os.system("cls")
            buscar_cueva()
        case 2:
            menu = False

os.system("cls")
print(
"Fin del juego\n"
"----------------------------\n"
f"Dragones matados: {dragones_muertos}\n"
f"Cuevas visitadas: {cuevas_visitadas}\n"
f"Hp final: {vida}\n"
f"Dinero final: {dinero}\n"
)
