import time
from lxml import etree
from funciones_listadepaises import *

doc=etree.parse("listadepaises.xml")

while True:
    menu=('''OPCIONES:
    1- LISTAR INFORMACIÓN: Mostrar el nombre de los continentes de los que tenemos información.
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
        print("Has seleccionado la opción 1:")
        print("LISTAR INFORMACIÓN: Mostrar el nombre de los continentes de los que tenemos información.")
        time.sleep(1)
        print()
        print("CONTINENTES")
        for elem in listar_informacion(doc):
            print(elem)
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 2
    elif opcion==2:
        print("Has seleccionado la opción 2:")
        print("CONTAR INFORMACIÓN: Mostrar la cantidad de países de los que tenemos información.")
        time.sleep(1)
        print()
        print("Nº DE PAÍSES")
        print(contar_informacion(doc))
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 3
    elif opcion==3:
        print("Has seleccionado la opción 3:")
        print("BUSCAR INFORMACIÓN: Pedir por teclado un país y mostrar el tipo de sistema político que tiene y su idioma.")
        time.sleep(1)
        print()
        pais=str(input("Introduce un país: "))
        while validar_pais(doc,pais)!=True:
            pais=input("No existe este país. Vuelva a intentarlo: ")
        sispol,idioma=buscar_informacion(doc,pais)
        print()
        print("Sistema político: ",sispol[0],"")
        print("Idioma: ",idioma[0],"")
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 4
    elif opcion==4:
        print("Has seleccionado la opción 4:")
        print("BUSCAR INFORMACIÓN RELACIONADA: Pedir por teclado un idioma y mostrar los países en los que se habla.")
        time.sleep(1)
        print()
        idioma=str(input("Introduce un idioma: "))
        while validar_idioma(doc,idioma)!=True:
            idioma=input("No existe este idioma. Vuelva a intentarlo: ")
        print()
        print("PAÍSES")
        for elem in buscar_informacion_relacionada(doc,idioma):
            print(elem)
        time.sleep(1)
        print()
        print()
        print()
        print()

    #EJERCICIO 5
    elif opcion==5:
        print("Has seleccionado la opción 5:")
        print("ACERCA DE LA MONEDA: Pedir por teclado una moneda, y mostrar los países en los que se utiliza. Además, que muestre su superficie(km²) y su idioma.")
        time.sleep(1)
        print()
        moneda=str(input("Introduce una moneda: "))
        while validar_moneda(doc,moneda)!=True:
            moneda=input("No existe esta moneda. Vuelva a intentarlo: ")
        lista_paises,lista_superficies,lista_idiomas=buscar_moneda(doc,moneda)
        for p,s,i in zip(lista_paises,lista_superficies,lista_idiomas):
            for p,s,i in zip(p,s,i):
                print(" ",p,"-",s,"km²","-",i)
        time.sleep(1)
        print()
        print()
        print()
        print()

    #Salir
    elif opcion==6:
        print("Has seleccionado la opción 6:")
        print("SALIR")
        time.sleep(1)
        print("FIN DEL PROGRAMA") 
        break  