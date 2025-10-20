#Map : 키, 값(kim:30)

d = {'one':'hana', 'two':'dul', 'three':'set'}
print(type(d))
print(d)
print(d['two'])

d['one'] = 1
print(d)

d['four'] = 4
print(d)
print(len(d)) # 딕셔너리 항목(키-값 쌍)의 개수

print(d.keys())
print(d.values())
print('one' in d.keys()) # true
print('dul' in d) # true
print('dul' in d.values()) # True
print(d.items()) # 딕셔너리의 (키, 값) 쌍 전체 보기


for i in d.keys():
    print(i)
print("----------")
for j in d.values():
    print(j)
print("----------")
for i,j in d.items():
    print(i,j)
print("----------")

print()
word = ["Hello", "World~~"]
dict = {}
for i in word:
    dict[i] = len(i)

print(dict)

d={}
word1 = "Hello"
word2 = "World~~"
d[word1] = len(word1)
d[word2] = len(word2)
print(d)