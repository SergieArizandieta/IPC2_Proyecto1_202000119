from xml.dom import minidom
from matriz import *
from ListaEnlazada import *

lista_e = lista_enlazada()

def cargarListas(xmlRuta):
    try:
        ruta = xmlRuta 
        xml = minidom.parse(ruta)
        rootNode = xml.documentElement

        terrenos = rootNode.getElementsByTagName("terreno")
        matrizGenerada = list
        for terreno in terrenos:
            if terreno.hasAttribute("nombre"):
                    matrizGenerada = matriz()
                    nombre = terreno.getAttribute("nombre")
                                 
                    dimension = terreno.getElementsByTagName("dimension")
                    for tamano in dimension:
                        m = tamano.getElementsByTagName("m")[0]
                        n = tamano.getElementsByTagName("n")[0]


                    posicioninicio = terreno.getElementsByTagName("posicioninicio")
                    for inicio in posicioninicio:
                        x1 = inicio.getElementsByTagName("x")[0]
                        y1 = inicio.getElementsByTagName("y")[0]

                    posicionfin = terreno.getElementsByTagName("posicionfin")
                    for final in posicionfin:
                        x2 = final.getElementsByTagName("x")[0]
                        y2 = final.getElementsByTagName("y")[0]

 

                    posicion = terreno.getElementsByTagName("posicion")
                    for position in posicion:
                        matrizGenerada.insertar(position.getAttribute("y")[0] ,position.getAttribute("x")[0],position.childNodes[0].data)
                    
                    e1 = Listaterrenos(nombre,matrizGenerada,x1.childNodes[0].data,y1.childNodes[0].data,x2.childNodes[0].data,y2.childNodes[0].data,m.childNodes[0].data,n.childNodes[0].data )
                    lista_e.insertar(e1)

        # print("Recorrer listas")
        #lista_e.recorrer() 
        print("\nArchivo Cargado con Exito")
    
    except Exception:
        print ("\nError en la ruta ingresada")


