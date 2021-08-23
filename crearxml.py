import xml.etree.cElementTree as ET

#def crearxml():
ruta = "./"

root = ET.Element("terreno",name="terreno1")
pocicioninicio = ET.SubElement(root, "posicioninicio")
ET.SubElement(pocicioninicio, "x").text = "1"
ET.SubElement(pocicioninicio, "y").text = "1"

pocicionfinal = ET.SubElement(root, "posicionfinal")
ET.SubElement(pocicionfinal, "x").text = "5"
ET.SubElement(pocicionfinal, "y").text = "5"


ET.SubElement(root, "combustible",).text = "84"
ET.SubElement(root, "posicion", x="1",y="2").text = "1"

def prettify(elemento, identificador='  '):
    validar = [(0, elemento)]  

    while validar:
        level, elemento = validar.pop(0)
        children = [(level + 1, child) for child in list(elemento)]
        if children:
            elemento.text = '\n' + identificador * (level+1)  
        if validar:
            elemento.tail = '\n' + identificador * validar[0][0]  
        else:
            elemento.tail = '\n' + identificador * (level-1)  
        validar[0:0] = children 

prettify(root)
archio = ET.ElementTree(root)
archio.write(ruta + 'prueba.xml', encoding='UTF-8')


