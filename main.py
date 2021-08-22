from ListaEnlazada import *
from carga import *
from carga import *



if __name__ == "__main__":
    xmlRuta = None
    #Menu desplegado
    def menu():
        print('1.Cargar archivo\n2.Procesar Terreno\n3.Escribir Archivo de salida\n4.Mostrar datos del estudiante\n5.Generar Grafica\n6.Salir')
    print("\n----------Bienvenido----------\n")
    menu()

    option = int(input("Ingrese una opcion: "))

    while option !=0:
        if option == 1:
            #./prueba.xml
            print("\nCargar Archivo")
            xmlRuta = input("Ingrese ruta del xml: ")
            xmlRuta = "./prueba.xml"
            cargarListas(xmlRuta)
            
        elif option == 2:
            if xmlRuta is None:
                print("\nIngrese un archivo XML primero")
            else:
                terreno = input("\nIngrese nombre del terreno: ")
                lista_e.buscar("terreno1")

        elif option == 3:
            print("Escribir archivbo de salida")    

        elif option == 4:
            print("\nDatos del estudiante:")
            print(">Sergie Daniel Arizandieta Yol")
            print(">20200119")
            print(">Introducción a la Programación y computación 2 'E'")
            print(">Ingeniería en Ciencias y Sistemas")
            print(">4to Semestre")

        elif option == 5:    
            print("Genrar grafica")

        elif option == 6: 
            print("\nGracias por usar!")
            exit()      

        else:
            print("Opcion invalida.")

        print()
        menu()
        option = int(input("Ingrese una opcion: "))
