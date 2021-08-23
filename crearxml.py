import xml.etree.cElementTree as ET

def crearxml():
    ruta = "./"
    
    root = ET.Element("terreno",name="terreno122")
    pocicioninicio = ET.SubElement(root, "posicioninicio")
    ET.SubElement(pocicioninicio, "x").text = "1"
    ET.SubElement(pocicioninicio, "y").text = "1"

    pocicionfinal = ET.SubElement(root, "posicionfinal")
    ET.SubElement(pocicionfinal, "x").text = "5"
    ET.SubElement(pocicionfinal, "y").text = "5"


    ET.SubElement(root, "combustible",).text = "84"
    ET.SubElement(root, "posicion", x="1",y="2").text = "1"

    def prettify(element, indent='  '):
        queue = [(0, element)]  

        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level+1)  
            if queue:
                element.tail = '\n' + indent * queue[0][0]  
            else:
                element.tail = '\n' + indent * (level-1)  
            queue[0:0] = children 

    prettify(root)
    archio = ET.ElementTree(root)
    archio.write(ruta + 'prueba.xml', encoding='UTF-8', xml_declaration=True)


