from bs4 import BeautifulSoup

# example.html 파일을 읽기 모드로 열기
fp = open('file/example.html')

# HTML 파서를 이용해 BeautifulSoup 객체 생성
soup = BeautifulSoup(fp, 'html.parser')

# 1. <title> 태그 전체 출력
print("1: ", soup.title)

# 2. <title> 태그의 이름(name 속성) 출력 -> "title"
print("2: ", soup.title.name)

# 3. <title> 태그 안의 텍스트 내용 출력
print("3: ", soup.title.string)

# 4. <title> 태그의 부모 태그 전체 출력 (보통 <head>)
print("4: ", soup.title.parent)

# 5. <title> 태그의 부모 태그 이름 출력 -> "head"
print("5: ", soup.title.parent.name)

# 6. 첫 번째 <p> 태그 전체 출력
print("6: ", soup.p)

# 7. 첫 번째 <div> 태그 전체 출력
print("7: ", soup.div)

# 8. <table> 태그가 없으면 None 출력
print("8: ", soup.table)

# 9. 모든 <div> 태그를 리스트 형태로 출력
print("9: ", soup.find_all('div'))

# 10. 모든 <p> 태그를 리스트 형태로 출력
print("10: ", soup.find_all('p'))

# 11. class = "ex_class" 를 가져오기
print("11: ", soup.find_all('div', 'ex_class'))

# 12. 모든 id='ex_id가져오기
print("12: ", soup.find_all(id='ex_id'))

# 13. 모든 <div>중 id = 'ex_id' 가져오기
print("13: ", soup.find_all('div', id='ex_id'))

# 파일 닫기
fp.close()
