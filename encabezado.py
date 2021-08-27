
class listaEncabezado:
    def __init__(self,primero=None):
        self.primero = primero
    
    def setEncabezado(self,nuevoData):
        if self.primero == None:
            self.primero = nuevoData
        elif nuevoData.Indicador < self.primero.Indicador:
            nuevoData.siguiente = self.primero
            self.primero.anterior = nuevoData
            self.primero = nuevoData
        else:
            actual = self.primero
            while actual.siguiente != None:
                if nuevoData.Indicador < actual.siguiente.Indicador:
                    nuevoData.siguiente = actual.siguiente
                    actual.siguiente.anterior = nuevoData
                    nuevoData.anterior = actual
                    actual.siguiente = nuevoData
                    break

                actual = actual.siguiente
            
            if actual.siguiente == None:
                actual.siguiente = nuevoData
                nuevoData.anterior = actual

    def getEncabezado(self,Indicador):
        actual = self.primero
        while actual != None:
            if actual.Indicador == Indicador:
                return actual
            actual = actual.siguiente
        return None 