from funciones_listadepaises import *

doc=etree.parse("listadepaises.xml")

while True:
    menu=('''OPCIONES:
    1- LISTAR INFORMACIÓN: Mostrar el nombre de los continentes de los que tenemos información, y sus respectivos países.
    2- CONTAR INFORMACIÓN: Mostrar la cantidad de países de los que tenemos información.
    3- BUSCAR INFORMACIÓN: Pedir por teclado un país y mostrar el tipo de sistema político que tiene y su idioma.
    4- BUSCAR INFORMACIÓN RELACIONADA: Pedir por teclado un idioma y mostrar los países en los que se habla.
    5- ACERCA DE LA MONEDA: Pedir por teclado una moneda, y mostrar los países en los que se utiliza. Además, que muestre su superficie(km²) y su idioma.
    6- SALIR
    ''')

    print(menu)
    opcion=int(input("¿Qué acción desea realizar?: "))
    while opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6:
        opcion=int(input("Error. Introduzca una opción del 1 al 6: "))

    #EJERCICIO 1
    if opcion==1:
        for pais in listar_informacion(doc):
            print(pais)

    #EJERCICIO 2
    if opcion==2:
        print(contar_informacion(doc))

    #EJERCICIO 3
    if opcion==3:
        cadena=str(input("Introduce un país: "))
        for pais in buscar_informacion(doc,cadena):
            print(pais)

    #EJERCICIO 4
    if opcion==4:
        cadena=str(input("Introduce un idioma: "))
        for idioma in buscar_informacion_relacionada(doc,cadena):
            print(idioma)

    #EJERCICIO 5
    if opcion==5:
        cadena=str(input("Introduce una moneda: "))
        for moneda in buscar_moneda(doc,cadena):
            print(moneda)

    #Salir
    if opcion==6:
        print("FIN DEL PROGRAMA") 
        break  