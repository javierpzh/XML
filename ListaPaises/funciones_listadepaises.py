#EJERCICIO 1
def listar_informacion(doc):
    lista_continentes=doc.xpath("//continentes/continente/@nombre")
    for elem in lista_continentes:
        cont=doc.xpath("//continentes/continente/@nombre")
    return cont

#EJERCICIO 2
def contar_informacion(doc):
    lista_paises=doc.xpath("//continente/pais/text()")
    return len(lista_paises)

#EJERCICIO 3
def buscar_informacion(doc,pais):
    lista_paises=doc.xpath("//continente/pais/text()")
    for elem in lista_paises:
        if pais in lista_paises:
            sispol=doc.xpath('/geografia/paises/pais[@nombre="%s"]/sistema/text()' %(pais))
            idioma=doc.xpath('/geografia/paises/pais[@nombre="%s"]/idioma/text()' %(pais))
        return sispol,idioma

#EJERCICIO 4
def buscar_informacion_relacionada(doc,idioma):
    lista_idiomas=doc.xpath("//paises/pais/idioma/text()")
    for elem in lista_idiomas:
        if idioma in lista_idiomas:
            pais=doc.xpath('/geografia/paises/pais[idioma="%s"]/idioma/../@nombre' %(idioma))
        return pais

#EJERCICIO 5
def buscar_moneda(doc,moneda):
    lista_monedas=doc.xpath("//paises/pais/moneda/text()")
    lista_paises=[]
    lista_superficies=[]
    lista_idiomas=[]
    for elem in lista_monedas:
        if moneda in lista_monedas:
            pais=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../@nombre' %(moneda))
            lista_paises.append(pais)
            superficie=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../superficie/text()' %(moneda))
            lista_superficies.append(superficie)
            idioma=doc.xpath('/geografia/paises/pais[moneda="%s"]/moneda/../idioma/text()' %(moneda))
            lista_idiomas.append(idioma)
        return lista_paises,lista_superficies,lista_idiomas


#VALIDACIONES

def validar_pais(doc,pais):
    if pais in doc.xpath("//continente/pais/text()"):
        return True

def validar_idioma(doc,idioma):
    if idioma in doc.xpath("//paises/pais/idioma/text()"):
        return True

def validar_moneda(doc,moneda):
    if moneda in doc.xpath("//paises/pais/moneda/text()"):
        return True