from funciones import LeerLibreria,listarNombre

informacion = LeerLibreria()

# menu
mostrar_menu = """----- MENU -----
1. Listar los monstruos que hay
2. Listar el nombre de cada monstruo y el nº de juegos en el que aparece
3. Mostrar los monstruos que empiecen por una subcadena indicada
4. Listar los monstruos que aparecen en un juego indicado
5. Mostrar la cantidad de monstruos de cada tipo en un juego indicado
6. Salir\n"""

menu = int(input(mostrar_menu))

while menu != 6:
    if menu == 1:
        listarNombre(informacion)
    menu = int(input(mostrar_menu))