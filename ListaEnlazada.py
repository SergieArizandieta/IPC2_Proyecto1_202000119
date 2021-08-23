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
      print("terreno:", actual.terreno.terreno,"lista:", actual.terreno.lista, "x1:", actual.terreno.x1,"y1:", actual.terreno.y1,"x2:", actual.terreno.x2,"y2:", actual.terreno.y2)
      actual = actual.siguiente


  def buscar(self,terreno,opcion,rutaIngresada):
    actual = self.primero
    anterior = None
    while actual and actual.terreno.terreno != terreno:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("\nNo se encontro el Terreno:", terreno)
        break
    if actual is not None:
      if actual.terreno.terreno == terreno:
       
        if opcion == True:
          print("\nTerreno a procesar: ", actual.terreno.terreno)
          actual.terreno.lista.recorrerCompleto()
          actual.terreno.lista.MejorRuta(int(actual.terreno.x1),int(actual.terreno.y1),int(actual.terreno.x2),int(actual.terreno.y2),int(actual.terreno.m),int(actual.terreno.n))
          actual.terreno.lista.ReporteMatriz()
        elif opcion == False:
          actual.terreno.lista.exportarxmls(int(actual.terreno.y1),int(actual.terreno.x1),actual.terreno.terreno,int(actual.terreno.y2),int(actual.terreno.x2),rutaIngresada)
        



      
    