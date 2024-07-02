serim = ["정세림", '25', '010-1234-5678']
name = serim[0]
age = serim[1]
phone = serim[2]
print(type(serim))
print(name, age, phone)

names = [['a', 'b', 'c'], ['20', '21', '22'], ['010', '010', '010']]
print(names[0][0:2])

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)

print(len(numbers))
print(len(names[0]))


# 리스트에 요소 추가 및 삭제하기
last = [1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)