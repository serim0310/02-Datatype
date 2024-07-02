# 1
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
email = input("이메일 주소를 입력하세요.")
phone = input("연락처를 입력하세요.")

dic = {name : [age, email, phone]}
print(dic)

# 2
exchange = {'달러' : 1320, '엔화' : 950, '위안' : 182}
철수 = [13, 200, 13]

print(exchange['달러'] * 철수[0] + exchange['엔화'] * 철수[1] + exchange['엔화'] * 철수[2])