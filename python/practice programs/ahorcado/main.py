import random
import os

if __name__ == "__main__":

    palabras = [
                {'palabra':"Mariano", 'pista': "Puta"}
                ]
    rng = random.randint(0, len(palabras))
    preword = palabras[rng - 1]
    palabra_rolleada = preword['palabra']

    letterspace = []
    builder = []
    for letra in palabra_rolleada:
        letterspace.append("[]")
        builder.append("")


    power = True
    vidas = 5
    part_4 = "\\"
    part_3 = "/"
    part_2 = "\\"
    part_1 = "/"
    torso = "|"


    no_match = ""
    #hp_phases = ["😄","🙂","😨","😩"]
    hp_phases = ["😩","😨","🤔","🙂","😄","💀"]
    palabra_array = [letra.lower() for letra in palabra_rolleada]

    os.system("clear")

    while power:
        val = True
        while val:

            if vidas == 4:
                part_4 = ""
            if vidas == 3:
                part_3 = ""
            if vidas == 2:
                part_2 = ""
            if vidas == 1:
                part_1 = ""
            if vidas == 0:
                torso = ""


            print(f" {'_':_^56}... .. .")
            print(f"| {'{Juego Del Ahorcado}':_^48}.. .. .\n||")
            print(f"||       Pista: {preword['pista']}")
            print(
            f"|| {no_match}\n"
            f"||   {hp_phases[vidas - 1]}          Vidas: {vidas}\n"
            f"||   {part_1}{torso}{part_2}        Palabra: {' '.join(letterspace)}\n"
            f"|:   {part_3} {part_4}\n:\n."
            )

            if vidas <= 0:
                power = False
                input("Game over bro💩💩")
                exit()
            if builder == palabra_array:
                power = False
                input(", U WIN BRO👏👏🙌🙌🙌")
                exit()

            letra_ingresada = input("      Ingrese una letra: ").lower()
            if len(letra_ingresada) == 1:
                val = False
            os.system("clear")

        no_match = ""

        for i, letra in enumerate(palabra_rolleada.lower()):
            if letra == letra_ingresada:
                letterspace[i] = f"[{letra_ingresada}]"
                builder[i] = letra_ingresada
                no_match = "            going good bro👍"
        if letra_ingresada not in palabra_rolleada:
            no_match = ("       WTFBRO THERE IS NO LETTER MATCH😭")
            vidas -= 1



    if builder == palabra_array:
        power = False
        os.system("clear")
        print("🥳🥳🥳👏👏CONGRATULATION, U WIN BRO👏👏🙌🙌🙌")
