class estudiante:
  def __init__(self,carnet,nombre,edad,direccion,telefono,email,carrera,puesto):
    self.carnet=carnet
    self.nombre=nombre
    self.edad=edad
    self.direccion=direccion
    self.telefono=telefono
    self.email=email
    self.carrera=carrera
    self.puesto=puesto

class nodo:
    def __init__(self,estudiante =None,siguiente=None):
      self.estudiante=estudiante
      self.siguiente=siguiente

class lista_enlazada:
  def __init__(self):
    self.primero = None

  def insertar(self, estudiante):
    if self.primero is None:
      self.primero = nodo(estudiante=estudiante)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(estudiante=estudiante)
    
  def recorrer(self):
    actual= self.primero
    while actual != None:
      print("carnet: ", actual.estudiante.carnet,"nombre: ", actual.estudiante.nombre, "email: ", actual.estudiante.email, "->")
      actual = actual.siguiente


  def buscar(self,carnet):
    actual = self.primero
    anterior = None
    while actual and actual.estudiante.carnet != carnet:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("No se encontro la persona con el carnet:", carnet)
        break
    if actual is not None:
      if actual.estudiante.carnet == carnet:
        print("carnet: ", actual.estudiante.carnet,"nombre: ", actual.estudiante.nombre, "email: ", actual.estudiante.email, "->")

if __name__ == "__main__":
    e1 = estudiante(202000119,"Gerson Ortiz",19,"Residenciales p...",41350000,"Gerson.ortiz@gmial.com","Ingenieria en Sistemas","Programador JR")
    e2 = estudiante(201912323,"Karen Hurtarte",20,"Residenciales p...",41350000,"Karen.hurtarte@gmial.com","Ingenieria en Sistemas","Programador JR")
    e3 = estudiante(201913232,"Luis Mnedez",21,"Residenciales p...",41350000,"Luis.mendez@gmial.com","Ingenieria en Sistemas","Programador JR")
    lista_e = lista_enlazada()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.insertar(e3)
    lista_e.recorrer()   
    print("")
    lista_e.buscar(202000119)
    lista_e.buscar(2019122123323)

      
    