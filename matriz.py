from nodos import Nodo,nodoEncabezado
from encabezado import listaEncabezado

class matriz:
    def __init__(self):
        self.eFilas =  listaEncabezado()
        self.eColumnas = listaEncabezado()

    def insertar(self,fila,columna,valor):
        nuevo = Nodo(fila,columna,valor)

        #Insercion de encabezados por filas
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = nodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha !=None:
                    if nuevo.columna < actual.derecha.columna:
                       nuevo.derecha = actual.derecha
                       actual.derecha.izquierda = nuevo
                       actual.izquierda = actual
                       actual.derecha = nuevo 
                       break
                    actual = actual.derecha 

                if actual.derecha == None: 
                    actual.derecha = nuevo 
                    nuevo.izquierda = actual 
        
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = nodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.eColumnas.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual =eColumna.accesoNodo
                while actual.abajo !=None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

                if actual.abajo == None:
                    actual.abajo = nuevo 
                    nuevo.arriba = actual

    def recorridoFilas(self):
        eFila = self.eFilas.primero
        print("\n**********************recorrdio por filas ***********************")

        while eFila != None:
            actual =eFila.accesoNodo
            print("\nFila "+str(actual.fila))
            print("Columna valor")
            while actual!= None:
                print(str(actual.columna) + "        " + str(actual.valor))
                actual = actual.derecha         
            eFila = eFila.siguiente
        print("\n**********************FIN recorrdio por filas ***********************")

    def recorrerColumnas(self): 
        eColumna = self.eColumnas.primero
        print("\n**********************recorrdio por columnas ***********************")

        while eColumna != None:

            actual = eColumna.accesoNodo
            print("\nColumna "+ str(actual.columna))
            print("Fila Valor")
            while actual !=None:
                print(str(actual.fila)+ "      "+ actual.valor)
                actual = actual.abajo
            
            eColumna = eColumna.siguiente
        print("\n**********************FIN recorrdio por columna ***********************")

    def recorrerCompleto(self): 
        eFila = self.eFilas.primero
        print("\n**********************recorrdio ***********************")
        while eFila != None:
            actual =eFila.accesoNodo
            fila = ""
            while actual!= None:
                fila += "|" + str(actual.valor) + "| "
                actual = actual.derecha   
            print( str(fila))         
            eFila = eFila.siguiente
        print("\n**********************FIN recorrdio  ***********************")

    def MejorRuta(self,x1,y1,x2,y2,m,n): 
        print("\n********************** Mejor Ruta ***********************")
        Inicio = self.eFilas.primero
        actual =Inicio.accesoNodo
        actual = Inicial(actual,x1,y1,x2,y2,Inicio)
        #print( AsignarTempInicial(actual.arriba,actual.abajo,actual.izquierda,actual.derecha,1000000000000000000000).valor , " valor final\n")
        actual = AsignarTempInicial(actual.arriba,actual.abajo,actual.izquierda,actual.derecha,1000000000000000000000)    
        
        while actual.finish == 0:
            AsignarTemporales(actual,actual.arriba,actual.abajo,actual.izquierda,actual.derecha,1000000000000000000000)
            actual = Buscarmin(self.eColumnas.primero,100000000000000000)
        
        print("\n**********************FIN recorrdio  ***********************")
    
        RutaRegreso(actual,y2,x2)

def Inicial(actual,x1,y1,x2,y2,Inicio):
    
    for x in range(1,x2):
        actual = actual.derecha
    for y in range(1,y2):
        actual = actual.abajo
    actual.finish = "1"

    print("(",x1,",",y1,")")  
    print("(",x2,",",y2,")")
    #print(actual.valor + " final: " + actual.finish)
    actual = Inicio.accesoNodo

    for x in range(1,x1):
        actual = actual.derecha
    for y in range(1,y1):
        actual = actual.abajo
    actual.star = "0"
    actual.temporal = 0
    actual.final = 0
    #print(actual.valor + " inicio: " + actual.star + "\n")   
    actual.revisado = True

    return actual

def AsignacionFinal(eColumnasPrimero,min,actual):
    eColumna = eColumnasPrimero
    while eColumna != None:
        actual = eColumna.accesoNodo
        
        while actual !=None:
            print(actual.temporal)
            if actual.temporal != None:
                if actual.revisado == False:
                    if min > int(actual.temporal):
                        min = int(actual.temporal)
            actual = actual.abajo
        
        eColumna = eColumna.siguiente
    #print("\n",min)

def Buscarmin(eColumnasPrimero,min): 
    eColumna = eColumnasPrimero
    
    while eColumna != None:
        actual = eColumna.accesoNodo
        
        while actual !=None:
            #print(actual.temporal)
            if actual.temporal != None:
                if actual.revisado == False:
                    if min > int(actual.temporal):
                        min = int(actual.temporal)
                        ruta = actual
            actual = actual.abajo
        
        eColumna = eColumna.siguiente

    ruta.final = ruta.temporal
    ruta.revisado = True
    #print(ruta.final," valor final")
    return ruta

    #if ruta.revisado == True:
        #print("\nMin: ",min," rura:",ruta," ruta", ruta.valor, " final",ruta.final)

def AsignarTemporales(actual,arriba,abajo,izquierda,derecha,min):
    
    if arriba != None:
        if arriba.revisado == False:
            if arriba.temporal is None:
                arriba.temporal = int(arriba.valor) + int(actual.final)
            else:
                temporal = int(arriba.valor) + int(actual.final)
                if  temporal < int(arriba.temporal):
                    arriba.temporal = arriba.temporal
        
        #print(arriba.temporal , "arriba temp")
                
    if abajo != None:
        if abajo.revisado == False:
            if abajo.temporal is None:
                abajo.temporal = int(abajo.valor) + int(actual.final)
            else:
                temporal = int(abajo.valor) + int(actual.final)
                if  temporal < int(abajo.temporal):
                    abajo.temporal = abajo.temporal
        
        #print(abajo.temporal , "abajo temp")

    if derecha != None:
        if derecha.revisado == False:
            if derecha.temporal is None:
                derecha.temporal = int(derecha.valor) + int(actual.final)
            else:
                temporal = int(derecha.valor) + int(actual.final)
                if  temporal < int(derecha.temporal):
                    derecha.temporal = derecha.temporal
        
        #print(derecha.temporal , "derecha temp")


    if izquierda != None:
        if izquierda.revisado == False:
            if izquierda.temporal is None:
                izquierda.temporal = int(izquierda.valor) + int(actual.final)
            else:
                temporal = int(izquierda.valor) + int(actual.final)
                if  temporal < int(izquierda.temporal):
                    izquierda.temporal = izquierda.temporal
        
        #print(izquierda.temporal , "izquierda temp")

def AsignarTempInicial(arriba,abajo,izquierda,derecha,min):

    if arriba != None:
        arriba.temporal = arriba.valor
        arriba.final = arriba.valor
        if min > int(arriba.temporal):
            min =  int(arriba.temporal)

        #print(arriba.temporal)

    if abajo != None:
        abajo.temporal = abajo.valor
        abajo.final = abajo.valor
        if min > int(abajo.temporal):
            min =  int(abajo.temporal)
        
        #print(abajo.temporal)

    if derecha != None:
        derecha.temporal = derecha.valor
        derecha.final = derecha.valor
        if min > int(derecha.temporal):
            min =  int(derecha.temporal)

        #print(derecha.temporal)

    if izquierda != None:
        izquierda.temporal = izquierda.valor
        izquierda.final = izquierda.valor
        if min > int(izquierda.temporal):
            min =  int(izquierda.temporal)

        #print(izquierda.temporal)

    if arriba != None:
          if min == int(arriba.temporal):
            arriba.revisado = True
            return arriba
        
    if abajo != None:
        if min == int(abajo.temporal):
            abajo.revisado = True
            return abajo 

    if derecha != None:
        if min == int(derecha.temporal):
            derecha.revisado = True
            return derecha 

    if izquierda != None:
       if min == int(izquierda.temporal):
            izquierda.revisado = True
            return izquierda 

def RutaRegreso(actual,m,n):
    print ( "(",n,",",m,")")

    while actual.temporal != 0:

        valor = int(actual.final) - int(actual.valor)
        #print(valor , "valor")

        if actual.izquierda != None:
            if actual.izquierda.final != None:
                if int(actual.izquierda.final) == valor:
                    actual = actual.izquierda
                    n -= 1 

        if actual.derecha != None:
            if actual.derecha.final != None:
                if int(actual.derecha.final) == valor:
                    actual = actual.derecha
                    n += 1

        if actual.abajo != None:
            if actual.abajo.final != None:
                if int(actual.abajo.final) == valor:
                    actual = actual.abajo
                    m+=1

        if actual.arriba != None:
            if actual.arriba.final != None:
                if int(actual.arriba.final) == valor:
                    actual = actual.arriba
                    m-=1
        
        print ( "(",n,",",m,")")
    

    
        
