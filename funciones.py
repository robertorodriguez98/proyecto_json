import json

def LeerLibreria():
    try:
        f=open("monsters.json")
        datos = json.load(f)
        f.close()
        return datos
    except:
        print("error al leer el fichero json")

def listarNombre(datos):
    for monstruo in datos.get("monsters"):
        print("%s, tipo %s"%(monstruo.get("name"),monstruo.get("type")))
    print()

def contarJuegos(datos):
    for monstruo in datos.get("monsters"):
        print("%s aparece en %d juegos"%(monstruo.get("name"),len(monstruo.get("games"))))

def monstruoSlice(datos,nombre):
    for monstruo in datos.get("monsters"):
        if monstruo.get("name").lower().startswith(nombre.lower()):
            print(monstruo.get("name"))
    print()

def listarJuegos(datos):
    listaJuegos = []
    for monstruo in datos.get("monsters"):
        for juegos in monstruo.get("games"):
            if juegos.get("game") not in listaJuegos:
                listaJuegos.append(juegos.get("game"))
    return listaJuegos

def buscaJuegos(datos):
    listaJuegos = listarJuegos(datos)
    print("Juegos disponibles:")
    for juego in listaJuegos:
        print(juego)
    buscJuego = input("Dime el juego a buscar: ")

    for monstruo in datos.get("monsters"):
        for juegos in monstruo.get("games"):
            if juegos.get("game").lower() == buscJuego.lower():
                print(monstruo.get("name"))

def listarTipos(datos):
    listaTipos = []
    for monstruo in datos.get("monsters"):
        if monstruo.get("type") not in listaTipos:
            listaTipos.append(monstruo.get("type"))
    return listaTipos

def buscarTipos(datos):
    listaTipos = listarTipos(datos)
    listaJuegos = listarJuegos(datos)
    
    dicTipos = d = dict.fromkeys(listaTipos, 0)

    for juego in listaJuegos:
        print(juego)
    buscJuego = input("Dime el juego a buscar: ")

    for monstruo in datos.get("monsters"):
        for juegos in monstruo.get("games"):
            if juegos.get("game").lower() == buscJuego.lower():
                dicTipos[monstruo.get("type")] += 1

    for elemento in listaTipos:
        if dicTipos[elemento] > 0:
            print("%s: %d monstruos"%(elemento,dicTipos[elemento]))