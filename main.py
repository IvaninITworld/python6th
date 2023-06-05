# 변수 선언
a = 10
b = 3.14
c = "Hello, Wolrd!"
d = [1, 2, 3]
e = (4, 5, 6)
f = {7, 8, 9}
g = {"apple": 1, "banana": 2, "orange": 3}

# 데이터 타입 출력
print("a : ", type(a))
print("b : ", type(b))
print("c : ", type(c))
print("d : ", type(d))
print("e : ", type(e))
print("f : ", type(f))
print("g : ", type(g))

# 덧셈
a = 4
b = 2
total = a + b
print("덧셈", total)
print("덧셈 타입", type(total))

# 뺄셈
a = 4
b = 2
total = a - b
print("뺄셈", total)
print("뺄셈 타입", type(total))

# 곱셈
a = 4
b = 2
total = a * b
print("곱셈", total)
print("곱셈 타입", type(total))

# 나눗셈
a = 4
b = 2
total = a / b
print("나눗셈", total)
print("나눗셈 타입", type(total))

# 나머지
total = a % b
print("나머지", total)
print("나머지 타입", type(total))

# 거듭제곱
total = a ** b
print("거듭제곱", total)
print("거듭제곱 타입", type(total))

# 몫 (양수)
total = a // b
print("몫 (양수)", total)
print("몫 (양수) 타입", type(total))

# 몫 (음수)
a = -5
total = a // b
print("몫 (음수)", total)
print("몫 (음수) 타입", type(total))

# 대소비교
a = 4
b = 2

print("a < b : ", a < b)
print("a > b : ", a > b)
print("a <= b : ", a <= b)
print("a >= b : ", a >= b)
print("a == b : ", a == b)
print("a != b : ", a != b)

# 논리 연산자
a = 5
b = 2
c = 3
d = 200

print("AND 연산자")
print("a > b and a > c : ", a > b and a > c)
print("a > b and a < c : ", a > b and a < c)
print("b < a < c : ", b < a < c)

print("OR 연산자")
print("a > b and a > c : ", a > b or a > c)
print("a > b and a < c : ", a > b or a < c)
print("b < a < c : ", b < a < c)

# 할당 연산자
a = 10
b = 20
m = 15

y = a + b
print(y)

m += 10 # m = m +10
print(m)

m **= 2
print(m)

m //= 2
print(m)

# 비트 연산자
a = 10
b = 15

print("a: ", bin(a))
print("b: ", bin(b))