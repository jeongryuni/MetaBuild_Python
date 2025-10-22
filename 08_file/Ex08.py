import xml.etree.ElementTree as ET

# 방법 1) 파일을 직접 읽어서 문자열로 처리
# with open('student.xml', 'r', encoding='utf-8') as f:
#     xmlData = f.read()
    # print(xmlData)
    # print(type(xmlData)) # <class 'str'> 태그인식x

# myroot = ET.fromstring(xmlData)
# print("myroot:", myroot) # <Element 'students' at 0x000001FE8D384860>


# 방법 2) parse() 함수 사용 → 파일에서 직접 XML을 파싱 (fromstring 기능 포함)
tree = ET.parse('student.xml')
myroot = tree.getroot()
print("myroot:", myroot)

totalList=[]
for stu in myroot.iter('student'):
    onePerson=[]
    # 하위요소 찾을때 find
    onePerson.append(stu.find("name").text)
    onePerson.append(stu.find("국어").text)
    onePerson.append(stu.find("영어").text)
    onePerson.append(stu.find("수학").text)

    score_total = (int(stu.find("국어").text) + int(stu.find("영어").text) + int(stu.find("수학").text))
    onePerson.append(score_total)
    totalList.append(onePerson)
    # print(onePerson)
print(totalList)

