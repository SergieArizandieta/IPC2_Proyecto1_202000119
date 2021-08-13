from xml.dom import minidom
from matriz import *

ruta = "./prueba.xml"
xml = minidom.parse(ruta)
rootNode = xml.documentElement
lita = []

terrenos = rootNode.getElementsByTagName("terreno")
matrizGenerada = list


for terreno in terrenos:
    if terreno.hasAttribute("nombre"):
            matrizGenerada = matriz()
            print("nombre:",terreno.getAttribute("nombre"))
            posicioninicio = terreno.getElementsByTagName("posicioninicio")
            posicionfin = terreno.getElementsByTagName("posicionfin")

            print("Inicio")
            for inicio in posicioninicio:
                x = inicio.getElementsByTagName("x")[0]
                y = inicio.getElementsByTagName("y")[0]
                print(x.nodeName,":",x.childNodes[0].data)
                print(y.nodeName,":",y.childNodes[0].data)

            print("Final")
            for final in posicionfin:
                x = final.getElementsByTagName("x")[0]
                y = final.getElementsByTagName("y")[0]
                print(x.nodeName,":",x.childNodes[0].data)
                print(y.nodeName,":",y.childNodes[0].data)
            posicion = terreno.getElementsByTagName("posicion")

            print("Valores")
            for position in posicion:
                print("-----")
                print("x:",position.getAttribute("x")[0])
                print("y:",position.getAttribute("y")[0])
                print("data:",position.childNodes[0].data)
                matrizGenerada.insertar(position.getAttribute("y")[0] ,position.getAttribute("x")[0],position.childNodes[0].data)
            matrizGenerada.recorridoFilas()
            lita.append(matrizGenerada)
          

print("Nuevo")
#Imprimir lista
"""for list in lita:
    print(list)
    #list.recorridoFilas()
    list.recorrerColumnas()"""


"""
for terreno in terrenos:
    if terreno.hasAttribute("nombre"):
            matrizGenerada = matriz()
            print("nombre:",terreno.getAttribute("nombre"))
            posicioninicio = terreno.getElementsByTagName("posicioninicio")
            posicionfin = terreno.getElementsByTagName("posicionfin")

            print("Inicio")
            for inicio in posicioninicio:
                x = inicio.getElementsByTagName("x")[0]
                y = inicio.getElementsByTagName("y")[0]
                print(x.nodeName,":",x.childNodes[0].data)
                print(y.nodeName,":",y.childNodes[0].data)

            print("Final")
            for final in posicionfin:
                x = final.getElementsByTagName("x")[0]
                y = final.getElementsByTagName("y")[0]
                print(x.nodeName,":",x.childNodes[0].data)
                print(y.nodeName,":",y.childNodes[0].data)
            posicion = terreno.getElementsByTagName("posicion")

            print("Valores")
            for position in posicion:
                print("-----")
                print("x:",position.getAttribute("x")[0])
                print("y:",position.getAttribute("y")[0])
                print("data:",position.childNodes[0].data)
                matrizGenerada.insertar(position.getAttribute("y")[0] ,position.getAttribute("x")[0],position.childNodes[0].data)
            matrizGenerada.recorridoFilas()
            lita.append(matrizGenerada)
            

"""


"""

for terreno in terrenos:
    if terreno.hasAttribute("nombre"):
            matrizGenerada = matriz()
            posicioninicio = terreno.getElementsByTagName("posicioninicio")
            posicionfin = terreno.getElementsByTagName("posicionfin")

            for inicio in posicioninicio:
                x = inicio.getElementsByTagName("x")[0]
                y = inicio.getElementsByTagName("y")[0]

            for final in posicionfin:
                x = final.getElementsByTagName("x")[0]
                y = final.getElementsByTagName("y")[0]
            posicion = terreno.getElementsByTagName("posicion")

            for position in posicion:
                matrizGenerada.insertar(position.getAttribute("y")[0] ,position.getAttribute("x")[0],position.childNodes[0].data)
            lita.append(matrizGenerada)

"""