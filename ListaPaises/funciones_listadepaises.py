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