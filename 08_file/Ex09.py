import xml.etree.ElementTree as ET

tree = ET.parse("Car_Info.xml")
root = tree.getroot()
print("myroot:", root)


for car in root.iter('car'):
    oneCar=[]
    name = car.find("brand").attrib['name']
    oneCar.append({"브랜드영문":name})
    oneCar.append({"브랜드:": car.find("brand").text})
    oneCar.append({"모델": car.find("model").text})
    oneCar.append({"연식": car.find("year").text})
    oneCar.append({"색상":car.find("color").text})

print("oneCar:", oneCar)