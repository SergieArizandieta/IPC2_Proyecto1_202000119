from matriz import *

class Listaterrenos:
  def __init__(self,terreno,lista,x1,y1,x2,y2,m,n):
    self.terreno=terreno
    self.lista=lista
    self.x1=x1
    self.y1=y1
    self.x2=x2
    self.y2=y2
    self.m=m
    self.n=n
    self.validado = False
    self.xml = None
    self.grafo = None

class nodo:
    def __init__(self,terreno =None,siguiente=None):
      self.terreno=terreno
      self.siguiente=siguiente
class lista_enlazada:
  def __init__(self):
    self.primero = None

  def insertar(self, terreno):
    if self.primero is None:
      self.primero = nodo(terreno=terreno)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(terreno=terreno)
    
  def recorrer(self):
    print("\n")
    actual= self.primero
    while actual != None:
      #print("terreno:", actual.terreno.terreno,"lista:", actual.terreno.lista, "x1:", actual.terreno.x1,"y1:", actual.terreno.y1,"x2:", actual.terreno.x2,"y2:", actual.terreno.y2)
      print("*", actual.terreno.terreno)
      actual = actual.siguiente

  def recorrerNombres(self):
    actual= self.primero
    while actual != None :
      if actual.terreno.validado == True:   
        print("*", actual.terreno.terreno)
      actual = actual.siguiente

  def buscar(self,terreno,opcion,rutaIngresada,XML):
    actual = self.primero
    anterior = None
    while actual and actual.terreno.terreno != terreno:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        if XML is not None:
          print("\nNo se encontro el Terreno:", terreno, "\n")
        break
    if actual is not None:
      if actual.terreno.terreno == terreno:

        if XML is not None and actual.terreno.validado == True:
            print("\nCreando archivo XML para terreno:" ,  actual.terreno.terreno) 
            actual.terreno.lista.crearXML(actual.terreno.terreno,actual.terreno.xml)

        elif opcion == True and actual.terreno.validado == False and XML is None:
          print("\nTerreno a procesar: ", actual.terreno.terreno)
          actual.terreno.lista.recorrerCompleto()
          actual.terreno.lista.MejorRuta(int(actual.terreno.x1),int(actual.terreno.y1),int(actual.terreno.x2),int(actual.terreno.y2),int(actual.terreno.m),int(actual.terreno.n))
          actual.terreno.lista.ReporteMatriz()
          actual.terreno.validado = True

        elif opcion == False  :
          xml = actual.terreno.lista.exportarxmls(int(actual.terreno.y1),int(actual.terreno.x1),actual.terreno.terreno,int(actual.terreno.y2),int(actual.terreno.x2),rutaIngresada)
          actual.terreno.xml = xml
          #print("XMLSSSADS")
          #print(xml)
         
        else:
           print(" El terreno fue anteriormente procesado\n ")

  def Grafo(self,terreno,importar):
    actual = self.primero
    anterior = None
    while actual and actual.terreno.terreno != terreno:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("\nNo se encontro el Terreno:", terreno, "\n")
        break
    if actual is not None:
      if actual.terreno.terreno == terreno:
        if  actual.terreno.validado == True and actual.terreno.grafo == None and importar == None:
            
            documento = actual.terreno.lista.insertarGrafo(actual.terreno.terreno,int(actual.terreno.m),int(actual.terreno.n))
            actual.grafo = documento
            #print(actual.grafo)
        elif  actual.terreno.validado == True  and importar is not None:
            #print("Importar")
            #print(actual.grafo)
            actual.terreno.lista.importarGrafo(actual.grafo,actual.terreno.terreno )
  
  def limpiar(self):

      cadena = ""

  
      actual= self.primero
      while actual != None:
        if actual.siguiente is not None:
          cadena += actual.terreno.terreno + ","
          #print("*", actual.terreno.terreno)
          actual = actual.siguiente
        else:
          cadena += actual.terreno.terreno
          actual = actual.siguiente 
      
      totalNames = cadena.split(",")
      #print(totalNames)

      for teerrenoV in totalNames:
        actual = self.primero
        anterior = None

        while actual and actual.terreno.terreno != teerrenoV:
          anterior = actual
          actual = actual.siguiente
        
        if anterior is None:
          self.primero = actual.siguiente
        elif actual:
          anterior.siguiente = actual.siguiente
          actual.siguiente = None


      
    
      




      
    