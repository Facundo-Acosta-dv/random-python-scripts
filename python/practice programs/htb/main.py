import os


def file_value(dir):
    path = dir
    fp = open(path, "rb")
    data = fp.read()
    fp.close()
    return data


def scan(ruta):
    search = {}

    for dirs_names, _, files in os.walk(ruta):
        search[dirs_names] = files

    return search


def detect_empty_keys(list):
    keys = []

    for key, _ in list.items():
        if len(list[key]) == 0:
            keys.append(key)

    return keys


def del_empty_keys(list, empty_keys):
    for i in range(len(empty_keys)):
        # acá se borra en "list" el directorio en la posición i de "empty_keys"
        del list[empty_keys[i]]

    return list


def find_file(lista, keyword):
    for key, _ in lista.items():
        lista[key] = [x for x in lista[key] if x.startswith(keyword)]  # ????

    return lista


def save_content(content, filename="output.txt"):  # saves content
    with open(filename, "wb") as file:
        file.write(content)
        file.close()


if __name__ == "__main__":

    dir = input("directory: ")
    json_dir = input("file name: ")

    result = scan(dir)

    result = find_file(result, "HackMe")

    empty_keys = detect_empty_keys(result)
    result = del_empty_keys(result, empty_keys)

    # ______________ todo buen hasta aqui

    os.system("clear")

    rutas = []
    for ruta, value in result.items():
        for file_name in value:
            file_dir = (os.path.join(ruta, file_name))
            rutas.append(file_dir)

    for ruta in rutas:
        save_content(file_value(ruta), json_dir)
