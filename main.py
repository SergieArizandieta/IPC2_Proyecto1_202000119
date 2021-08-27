from ListaEnlazada import *
from carga import *


validacion = False
 

if __name__ == "__main__":
    
        aceptacion = True
        xmlRuta = None
        terreno = None
        #Menu desplegado
        def menu():
            
            print('1.Cargar archivo\n2.Procesar Terreno\n3.Escribir Archivo de salida\n4.Mostrar datos del estudiante\n5.Generar Grafica\n6.Salir')
        print("\n----------Bienvenido----------\n")
        menu()

        

        while aceptacion == True:

            try:
        
                option = int(input("\nIngrese una opcion: "))
            
                if option == 1:
                    if validacion == False:
                        print("\nCargar Archivo")
                        xmlRuta = input("Ingrese ruta del xml: ")
                        cargarListas(xmlRuta)
                        validacion = True
                        #xmlRuta = "./prueba.xml"

                    else:
                        lista_e.limpiar() 
                        lista_e.recorrer() 
                        print("Cargar Archivo")
                        xmlRuta = input("Ingrese ruta del xml: ")
                        cargarListas(xmlRuta)
                         
                        
                elif option == 2:

                    if xmlRuta is None or xmlRuta=="":
                        print("\nIngrese un archivo XML primero")
                    else:
                        print("\nTerrenos cargados en XML")   
                        lista_e.recorrer() 
                        terreno = input("\nIngrese nombre del terreno: ")
                        lista_e.buscar(terreno,True,"",None)
                        ruta = "./XML_Terrenos/"
                        lista_e.buscar(terreno,False,ruta,None)
                        lista_e.Grafo(terreno,None)

                        #terreno = "terreno1"

                elif option == 3:

                        print("\nTerrenos procesados:")
                        lista_e.recorrerNombres()
                        print("")
                        terrenos = input("\nIngrese nombre del terreno para generar XML: ")
                        ruta = "./XML_Terrenos/"
                        lista_e.buscar(terrenos,True,"","XML")

                        #lista_e.buscar(terrenos,False,ruta) 
                        #terrenos = "terreno1"
                        

                elif option == 4:
                    print("\nDatos del estudiante:\n")
                    print(">Sergie Daniel Arizandieta Yol")
                    print(">20200119")
                    print(">Introducción a la Programación y computación 2 'E'")
                    print(">Ingeniería en Ciencias y Sistemas")
                    print(">4to Semestre\n")

                elif option == 5:    

                        
                    if terreno is None:
                        print("\nProcese un terreno primero")
                    else: 
                        print("\nTerrenos procesados:")
                        lista_e.recorrerNombres()
                        terrenoGrafo = input("\nIngrese nombre del terreno: ")
                        lista_e.Grafo(terrenoGrafo,"importar")
                        #terrenoGrafo = "terreno1"
                        #lista_e.Grafo(terrenoGrafo)
                       
                elif option == 6: 
                    print("\nGracias por usar!")
                    exit()      

                else:
                    print("Opcion invalida.")
                menu()

            except Exception:
                print ("\nError vuelva a intentarlo")
                print()
                menu()
            
           

