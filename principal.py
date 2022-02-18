from funciones import LeerLibreria

informacion = LeerLibreria()

# menu
mostrar_menu = """1. Listar los monstruos que hay
2. Listar el nombre de cada monstruo y el nº de juegos en el que aparece
3. Mostrar los monstruos que empiecen por una subcadena indicada
4. Listar los monstruos que aparecen en un juego indicado
5. Mostrar la cantidad de monstruos de cada tipo en un juego indicado
6. Salir\n"""

menu = int(input(mostrar_menu))

while menu != 6:
    menu = int(input(mostrar_menu))