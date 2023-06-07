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
