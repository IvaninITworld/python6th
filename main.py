# # 변수 선언
# a = 10
# b = 3.14
# c = "Hello, Wolrd!"
# d = [1, 2, 3]
# e = (4, 5, 6)
# f = {7, 8, 9}
# g = {"apple": 1, "banana": 2, "orange": 3}

# # 데이터 타입 출력
# print("a : ", type(a))
# print("b : ", type(b))
# print("c : ", type(c))
# print("d : ", type(d))
# print("e : ", type(e))
# print("f : ", type(f))
# print("g : ", type(g))

# # 덧셈
# a = 4
# b = 2
# total = a + b
# print("덧셈", total)
# print("덧셈 타입", type(total))

# # 뺄셈
# a = 4
# b = 2
# total = a - b
# print("뺄셈", total)
# print("뺄셈 타입", type(total))

# # 곱셈
# a = 4
# b = 2
# total = a * b
# print("곱셈", total)
# print("곱셈 타입", type(total))

# # 나눗셈
# a = 4
# b = 2
# total = a / b
# print("나눗셈", total)
# print("나눗셈 타입", type(total))

# # 나머지
# total = a % b
# print("나머지", total)
# print("나머지 타입", type(total))

# # 거듭제곱
# total = a**b
# print("거듭제곱", total)
# print("거듭제곱 타입", type(total))

# # 몫 (양수)
# total = a // b
# print("몫 (양수)", total)
# print("몫 (양수) 타입", type(total))

# # 몫 (음수)
# a = -5
# total = a // b
# print("몫 (음수)", total)
# print("몫 (음수) 타입", type(total))

# # 대소비교
# a = 4
# b = 2

# print("a < b : ", a < b)
# print("a > b : ", a > b)
# print("a <= b : ", a <= b)
# print("a >= b : ", a >= b)
# print("a == b : ", a == b)
# print("a != b : ", a != b)

# # 논리 연산자
# a = 5
# b = 2
# c = 3
# d = 200

# print("AND 연산자")
# print("a > b and a > c : ", a > b and a > c)
# print("a > b and a < c : ", a > b and a < c)
# print("b < a < c : ", b < a < c)

# print("OR 연산자")
# print("a > b and a > c : ", a > b or a > c)
# print("a > b and a < c : ", a > b or a < c)
# print("b < a < c : ", b < a < c)

# # 할당 연산자
# a = 10
# b = 20
# m = 15

# y = a + b
# print(y)

# m += 10  # m = m +10
# print(m)

# m **= 2
# print(m)

# m //= 2
# print(m)

# # 비트 연산자
# a = 10
# b = 15

# print("a: ", bin(a))
# print("b: ", bin(b))


# # 명시적 타입 변환
# n1 = 10.99
# vn1 = int(n1)

# print(vn1, type((vn1)))


# # 자료형
# data = [10, 20, -50, 21.3, "likeLion"]
# print(data)

# for i in data:
#     print(type(i))

##################################################

# # 예제 1: 간단한 if 문
# x = 5
# if x > 3:
#     print("x는 3보다 크다.")

# # 예제 2: if else
# age = 18
# if age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년입니다.")


# # 예제 3: 중첩된 if else
# score = 85
# if score <= 90:
#     print("Class A")
# else:
#     if score >= 80:
#         print("Class B")
#     else:
#         if score >= 70:
#             print("Class C")
#         else:
#             print("Class D")

# # 예제 4: if elif
# marks = 75
# if marks >= 90:
#     print("A")
# elif marks >= 80:
#     print("B")
# elif marks >= 70:
#     print("C")
# elif marks >= 60:
#     print("D")
# else:
#     print("F")


# # 예제 5: 입력받아 if else 로 처리하기
# a = int(input("Enter Number Greater then or equal to 2: "))
# if a >= 2:
#     print("Correct!! You have Entered: ", a)
# else:
#     print("Wrong!! you have entered: ", a)


# # 예제 6: 입력받아 if elif 문으로 처리하기
# day = input("요일을 입력하세요 : ")
# if day == "Mon":
#     print("월요일")
# elif day == "Tue":
#     print("화요일")
# elif day == "Wed":
#     print("수요일")
# else:
#     print("휴일")

# # while 문
# i = 0
# while i < 10:
#     i += 1
#     print("i: ", i)
# else:
#     print("i is greater than 9")

# # while ture
# while True:
#     a = input("Enter Menu Number: ")
#     if a == 0:
#         break
#     print("a: ", a)
# else:
#     print("else")

# # while 루프
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
# print("End")

# b = 2
# while b <= 20:
#     print(b)
#     b += 2
# print("End")

# # else
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
# else:
#     print("while 문 거짓, else 부분 실행")
# print("End")

# # 무한 루프
# while True:
#     print("Like Lion")
# print("End")

# # 무한 루프 + 종료 코드
# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 5:
#         break
# print("End")

# # 중첩
# i = 1
# while i <= 3:
#     print("Outer Loop", i)
#     i += 1
#     j = 1
#     while j <= 5:
#         print("Inner loop", j)
#         j += 1
# print("End")

# # 문법: range(j) 0, 1, 2, 3, 4, ..., j-1
# for i in range(5):
#     print(i)
# # 0 ~ 4

# for i in range(2, 7):
#     print(i)
# # 2 ~ 6

# for i in range(1, 10, 2):
#     print(i)
# # 1 3 5 7 9

# for i in range(-1, -10, -2):
#     print(i)
# # -1 -3 -5 -7 -9

# a = range(5)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))
# print(type(a[3]))
# print(type(a[4]))

# print("Reverse Rage with Start, Stop, Step")
# r = range(5, 0, -1)
# print(r[0])
# print(r[1])
# print(r[2])
# print(r[3])
# print(r[4])
# # 5 4 3 2 1

# # for in
# st = "멋쟁이 사자"
# for ch in st:
#     print(ch)
# else:
#     print("Else")

# print("End")

# a = 5
# if a < 6:
#     pass
# else:
#     print("6 보다 큼")

# # 배열 생성 및 원소 접근
# import array

# # from array import *

# stu_roll = array.array("i", [101, 102, 103, 104, 105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])

# print("for in 사용")
# for element in stu_roll:
#     print(element)

# print("인덱스를 이용한 순회")
# n = len(stu_roll)
# for i in range(n):
#     print(i, "=", stu_roll[i])

# print("인덱스를 사용한 while 루프 배열 순회")
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1


# # 배열 삽입
# stu_roll = array.array("i", [101, 102, 103, 104, 105])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# # 배열 insert()
# print("Array After Insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)

# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# # 배열 remove()
# print("Array After remove")
# stu_roll.remove(101)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# # 배열 pop()
# print("Array After pop()")
# stu_roll.pop()
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# # 배열 메소드
# print("Array index()")
# stu_roll = array.array("i", [101, 102, 103, 104, 105])
# print(stu_roll.index(101))

# # 배열 extend()
# print("Array extend()")
# arr = array.array("i", [201, 208, 209])
# stu_roll.extend(arr)

# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# # 배열 reverse()
# print("Array reverse()")
# stu_roll.reverse()

# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1

# 4교시
from array import array

# import array

stu_roll = array("i", [101, 102, 103, 104, 105, 106, 107])

# 배열 슬라이싱
print("Array slice()")
print(stu_roll[1:5])
# array('i', [102, 103, 104, 105])
print(stu_roll[0:])
# array('i', [101, 102, 103, 104, 105, 106, 107])

n = len(stu_roll)
for i in range(n):
    print(i, "=", stu_roll[i])

print("인덱스 1 부터 5까지(인덱스 5 포함x)")
a = stu_roll[1:5]
for i in a:
    print(i)

print("인덱스 0 부터 끝까지")
b = stu_roll[0:]
for i in b:
    print(i)

print("인덱스 처음부터 5까지(인덱스 5 포함x)")
c = stu_roll[:5]
for i in c:
    print(i)

print("인덱스 마지막 4개")
d = stu_roll[-4:]
for i in d:
    print(i)

print("인덱스 0부터 6번째 까지(인덱스 6 포함 x) 2개씩 건너뛰어")
e = stu_roll[0:6:2]
for i in e:
    print(i)

print("인덱스 마지막 인덱스로 부터 5개 요소 중 맨앞 2개의 요소[-5-(-3)=-2]를 출력")
f = stu_roll[-5:-3]
for i in f:
    print(i)

# 문자열
str1 = "LikeLion"
str2 = "LikeLion"
str3 = """
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
"""

print(str1)
print(str2)
print(str3)

str4 = 'Hello "LikeLion" How are you?'
str5 = "Hello 'LikeLion' How are you?"

print(str4)
# Hello "LikeLion" How are you?
print(str5)
# Hello 'LikeLion' How are you?

str6 = "Hello \n How are you?"
str7 = "Hello \\ How are you?"
str8 = r"Hello \n How are you?"

print(str6)  # 줄바꿈
# Hello
# How are you?
print(str7)
# Hello \ How are you?
print(str8)  # escape 문자 생략해버리는
# Hello \n How are you?
print(type(str8))

str9 = "Hello \\ How are \t you?"

print(str9)  # tab 삽입
# Hello \ How are          you?

# 메모리 할당
# 파이썬에서 문자열은 객체로 취급
# 문자열은 불변 객체로 생성된 후에는 변경할 수 없다.
# 파이썬에서 변수는 모두 참조값을 가지고 있다.
# 가변 객체(Mutable Object), 불변 객체(Immutable Object)


def greet(name, msg):
    print(name, msg)


greet(name="철수", msg="안녕하세요!")
greet(msg="안녕하세요!", name="철수")


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="철수", age=25, city="서울")


# 인자가 없는 함수
print("인자가 없는 함수")


def disp():
    name = "멋쟁이사자"
    print("Welcome to", name)


print("함수 실행")
disp()


def add(y):
    x = 10.2334
    print(x + y)
    print(f"Formattered Output{x + y:.2f}")
    print(f"Formattered Output{x + y:10.2f}")  # 전체 출력의 폭을 지정
    # Formattered Output     30.23
    print(f"Formattered Output{x + y:6.2f}")  # 전체 출력의 폭을 지정
    # Formattered Output 30.23


add(20)
