from xml.dom import minidom
from matriz import *
from ListaEnlazada import *

lista_e = lista_enlazada()

def cargarListas(xmlRuta):
    
    try:
        ruta = xmlRuta 

        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
        for terrenos in root:
            validacionlextura = True
            
            
            for dimension in terrenos.iter('m'):
                m=dimension.text
            
            for dimension in terrenos.iter('n'):
                n=dimension.text
     
            for posicioni in terrenos.iter('posicioninicio'):
                for x in posicioni.iter('x'):
                    x1=x.text
                for y in posicioni.iter('y'):
                    y1=y.text   
      
            for posicionf in terrenos.iter('posicionfin'):
                for x in posicionf.iter('x'):
                    x2=x.text
                for y in posicionf.iter('y'):
                    y2=y.text  

            if int(m)>100 or int(n)>100 or int(m)<1 or int(n)<1 :
                validacionlextura = False

            matrizGenerada = matriz()

            if validacionlextura == True:
                nombre=terrenos.attrib['nombre']
                print("Se ha guardado la información del mapa: " + nombre )
                for posicion in terrenos.iter('posicion'):
                    #fila,columna,valor,x,y
                    matrizGenerada.insertar(int(posicion.attrib['y']) ,int(posicion.attrib['x']),int(posicion.text),int(posicion.attrib['x']),int(posicion.attrib['y']))
        
                e1 = Listaterrenos(nombre,matrizGenerada,x1,y1,x2,y2,m,n )
                #terreno,lista,x1,y1,x2,y2,m,n  
                lista_e.insertar(e1)
                
        
        #lista_e.recorrer() 
        print("\nArchivo Cargado con Exito\n")
        return True
    
    except Exception:
        print ("\nError en la ruta ingresada\n")
        return False


