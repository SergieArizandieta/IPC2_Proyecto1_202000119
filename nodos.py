class Nodo:
    def __init__(self,fila,columna,valor,x,y):
        self.valor=valor

        self.fila=fila
        self.columna=columna
        self.derecha = None
        self.izquierda = None
        self.arriba = None  
        self.abajo = None
        
        self.final = None
        self.temporal = None
        self.revisado = False
      
        self.marcador = False

        self.x = x
        self.y = y

        self.star = 1
        self.finish = 0

class nodoEncabezado:
    def __init__(self, Indicador):
        self.Indicador = Indicador
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None
    