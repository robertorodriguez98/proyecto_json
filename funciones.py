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

def monstruosJuegos(datos):
    listaJuegos = []
    for monstruo in datos.get("monsters"):
        for juegos in monstruo.get("games"):
            if juegos.get("game") not in listaJuegos:
                listaJuegos.append(juegos.get("game"))
    print(listaJuegos)