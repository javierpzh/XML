from lxml import etree
doc=etree.parse("listadepaises.xml")
lista1=doc.xpath("//continentes/continente/@nombre")
lista2=doc.xpath("//continente/pais/text()")
lista3=doc.xpath("//paises/pais/idioma/text()")
lista4=doc.xpath("//paises/pais/moneda/text()")

def listar_informacion(lista1,lista2):
    for continente in lista1:
        cont=doc.xpath("//continentes/continente/@nombre")
        return cont

def contar_informacion(lista2):
    return len(lista2)

def buscar_informacion(lista2,cadena):
    for pais in lista2:
        if cadena in lista2:
            sispol=doc.xpath('/geografia/paises/pais[@nombre="%s"]/sistema/text()' %(cadena))
            idioma=doc.xpath('/geografia/paises/pais[@nombre="%s"]/idioma/text()' %(cadena))
        return sispol,idioma

def buscar_informacion_relacionada(lista3,cadena):
    for idioma in lista3:
        if cadena in lista3:
            pais=doc.xpath('/geografia/paises/pais[idioma="%s"]/idioma/../@nombre' %(cadena))
        return pais

def buscar_moneda(lista4,cadena):
    lista_paises=[]
    lista_superficies=[]
    lista_idiomas=[]
    for moneda in lista4:
        if cadena in lista4:
            pais=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../@nombre' %(cadena))
            lista_paises.append(pais)
            superficie=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../superficie/text()' %(cadena))
            lista_superficies.append(superficie)
            idioma=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../idioma/text()' %(cadena))
            lista_idiomas.append(idioma)
        return lista_paises,lista_superficies,lista_idiomas
