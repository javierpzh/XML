from lxml import etree

def listar_informacion(doc):
    lista1=doc.xpath("//continentes/continente/@nombre")
    lista2=doc.xpath("//continente/pais/text()")
    for continente in lista1:
        cont=doc.xpath("//continentes/continente/@nombre")
        return cont

def contar_informacion(doc):
    lista2=doc.xpath("//continente/pais/text()")
    return len(lista2)

def buscar_informacion(doc,cadena):
    lista2=doc.xpath("//continente/pais/text()")
    for pais in lista2:
        if cadena in lista2:
            sispol=doc.xpath('/geografia/paises/pais[@nombre="%s"]/sistema/text()' %(cadena))
            idioma=doc.xpath('/geografia/paises/pais[@nombre="%s"]/idioma/text()' %(cadena))
        return sispol,idioma

def buscar_informacion_relacionada(doc,cadena):
    lista3=doc.xpath("//paises/pais/idioma/text()")
    for idioma in lista3:
        if cadena in lista3:
            pais=doc.xpath('/geografia/paises/pais[idioma="%s"]/idioma/../@nombre' %(cadena))
        return pais

def buscar_moneda(doc,cadena):
    lista4=doc.xpath("//paises/pais/moneda/text()")
    lista=[]
    for moneda in lista4:
        if cadena in lista4:
            pais=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../@nombre' %(cadena))
            lista.append(pais)
            superficie=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../superficie/text()' %(cadena))
            lista.append(superficie)
            idioma=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../idioma/text()' %(cadena))
            lista.append(idioma)
        return lista
