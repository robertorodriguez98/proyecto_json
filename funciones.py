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