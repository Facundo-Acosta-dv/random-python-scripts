from Models.mascotas import Mascota

if __name__ == "__main__":

    mascotitas = []

    nombre = input("ingrese nombre de la mascota: ")
    raza = input("ingrese raza: ")

    mascota = Mascota(nombre, raza)
    mascotitas.append(mascota)

    for i in range(len(mascotitas)):
        nombre = mascotitas[i].get_nombre()
        id = mascotitas[i].get_id()
        print(f"{'{'f'{nombre}''}':-^20}")
        print(
            f"Nombre:{nombre}",
            f"\nid:{id}"
        )


