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
# stu_roll = array.array("i", [101, 102, 103, 104, 105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])
# # 101
# # 102
# # 103
# # 104
# # 105
#
# print("for in 사용")
# for element in stu_roll:
#     print(element)
# # 101
# # 102
# # 103
# # 104
# # 105
#
# print("인덱스를 이용한 순회")
# n = len(stu_roll)
# for i in range(n):
#     print(i, "=", stu_roll[i])
# # 0 = 101
# # 1 = 102
# # 2 = 103
# # 3 = 104
# # 4 = 105
#
# print("인덱스를 사용한 while 루프 배열 순회")
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
# # 101
# # 102
# # 103
# # 104
# # 105

# # 다차원 배열
# multi_dimentional_array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print("Element at (0, 0): ", multi_dimentional_array[0][0])
# print("Element at (1, 2): ", multi_dimentional_array[1][2])
# print("Element at (2, 1): ", multi_dimentional_array[2][1])
# # Element at (0, 0):  1
# # Element at (1, 2):  6
# # Element at (2, 1):  8
#
# for i in range(len(multi_dimentional_array)):
#     for j in range(len(multi_dimentional_array)):
#         print(multi_dimentional_array[i][j], end=' ')
#     print()
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # 배열관련 메서드
# import array
#
# stu_roll = array.array("i", [101, 102, 103, 104, 105])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
# # 101
# # 102
# # 103
# # 104
# # 105
#
# # 배열 insert()
# print("Array After Insert")
# stu_roll.insert(1, 106)
# stu_roll.insert(3, 107)
#
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
# # 101
# # 106
# # 102
# # 107
# # 103
# # 104
# # 105
#
# # 배열 remove()
# print("Array After remove")
# stu_roll.remove(101)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
# # 106
# # 102
# # 107
# # 103
# # 104
# # 105
#
# # 배열 pop()
# print("Array After pop()")
# stu_roll.pop()
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
# # 106
# # 102
# # 107
# # 103
# # 104
#
# # 배열 메소드
# print("Array index()")
# stu_roll = array.array("i", [101, 102, 103, 104, 105])
# print(stu_roll.index(101))
# # 0
#
# # 배열 extend()
# print("Array extend()")
# arr = array.array("i", [201, 208, 209])
# stu_roll.extend(arr)
#
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
# # 101
# # 102
# # 103
# # 104
# # 105
# # 201
# # 208
# # 209
#
# # 배열 reverse()
# print("Array reverse()")
# stu_roll.reverse()
#
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
# # 105
# # 104
# # 103
# # 102
# # 101


# # 4교시
# from array import array
#
# # import array
#
# stu_roll = array("i", [101, 102, 103, 104, 105, 106, 107])
#
# # 배열 슬라이싱
# print("Array slice()")
# print(stu_roll[1:5])
# # array("i", [102, 103, 104, 105])
# print(stu_roll[0:])
# # array("i", [101, 102, 103, 104, 105, 106, 107])
#
# n = len(stu_roll)
# for i in range(n):
#     print(i, "=", stu_roll[i])
# # 0 = 101
# # 1 = 102
# # 2 = 103
# # 3 = 104
# # 4 = 105
# # 5 = 106
# # 6 = 107
#
# print("인덱스 1 부터 5까지(인덱스 5 포함x)")
# a = stu_roll[1:5]
# for i in a:
#     print(i)
# # 102
# # 103
# # 104
# # 105
#
# print("인덱스 0 부터 끝까지")
# b = stu_roll[0:]
# for i in b:
#     print(i)
# # 101
# # 102
# # 103
# # 104
# # 105
# # 106
# # 107
#
# print("인덱스 처음부터 5까지(인덱스 5 포함x)")
# c = stu_roll[:5]
# for i in c:
#     print(i)
# # 101
# # 102
# # 103
# # 104
# # 105
#
# print("인덱스 마지막 4개")
# d = stu_roll[-4:]
# for i in d:
#     print(i)
# # 104
# # 105
# # 106
# # 107
#
# print("인덱스 0부터 6번째 까지(인덱스 6 포함 x) 2개씩 건너뛰어")
# e = stu_roll[0:6:2]
# for i in e:
#     print(i)
# # 101
# # 103
# # 105
#
# print("인덱스 마지막 인덱스로 부터 5개 요소 중 맨앞 2개의 요소[-5-(-3)=-2]를 출력")
# f = stu_roll[-5:-3]
# for i in f:
#     print(i)
# # 103
# # 104
#
# # 문자열
# str1 = "LikeLion"
# str2 = "LikeLion"
# str3 = """
# 동해물과 백두산이
# 마르고 닳도록
# 하느님이 보우하사
# 우리나라 만세
# """
#
# print(str1)
# print(str2)
# print(str3)
# # LikeLion
# # LikeLion
# #
# # 동해물과 백두산이
# # 마르고 닳도록
# # 하느님이 보우하사
# # 우리나라 만세
#
# str4 = "Hello 'LikeLion' How are you?"
# str5 = "Hello 'LikeLion' How are you?"
#
# print(str4)
# # Hello "LikeLion" How are you?
# print(str5)
# # Hello "LikeLion" How are you?
#
# str6 = "Hello \n How are you?"
# str7 = "Hello \\ How are you?"
# str8 = r"Hello \n How are you?"
#
# print(str6)  # 줄바꿈
# # Hello
# # How are you?
# print(str7)
# # Hello \ How are you?
# print(str8)  # escape 문자 생략해버리는
# # Hello \n How are you?
# print(type(str8))
# # <class 'str'>
#
# str9 = "Hello \\ How are \t you?"
#
# print(str9)  # tab 삽입
# # Hello \ How are          you?
#
# # 메모리 할당
# # 파이썬에서 문자열은 객체로 취급
# # 문자열은 불변 객체로 생성된 후에는 변경할 수 없다.
# # 파이썬에서 변수는 모두 참조값을 가지고 있다.
# # 가변 객체(Mutable Object), 불변 객체(Immutable Object)
#
#
# def greet(name, msg):
#     print(name, msg)
# # 철수 안녕하세요!
# # 철수 안녕하세요!!
#
# greet(name="철수", msg="안녕하세요!")
# greet(msg="안녕하세요!!", name="철수")
#
#
# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# # name: 철수
# # age: 25
# # city: 서울
#
# display_info(name="철수", age=25, city="서울")

######################################################################

# # 인자가 없는 함수
# print("인자가 없는 함수")


# def disp():
#     name = "멋쟁이사자"
#     print("Welcome to", name)


# print("함수 실행")
# disp()


# def add(y):
#     x = 10.2334
#     print(x + y)
#     print(f"Formattered Output{x + y:.2f}")
#     print(f"Formattered Output{x + y:10.2f}")  # 전체 출력의 폭을 지정
#     # Formattered Output     30.23
#     print(f"Formattered Output{x + y:6.2f}")  # 전체 출력의 폭을 지정
#     # Formattered Output 30.23


# add(20)


# def add():
#     x = 10
#     y = 20
#     c = x + y
#     return c


# sum1 = add()  # add 의 return 값이 sum 에 할당
# print(sum1)


# def newAdd(y):
#     x = 10
#     c = x + y
#     d = y - x
#     return c, d, 50


# a = 30
# total = newAdd(a)
# k, l, m = newAdd(a)
# print(total)
# print(k)
# print(l)
# print(m)


# def disp():
#     def show():
#         print("show function")

#     show()


# print("순서 체크 1")
# disp()
# print("순서 체크 2")


# def disp():
#     def show():
#         return "show function"

#     result = show() + " adding"
#     return result


# print("순서 체크 1")
# print(disp())
# print("순서 체크 2")

#
# def disp(sh):
#     print(type(sh))
#     print("Disp Function" + sh*())
#
#
# def show():
#     return " show function"
#
#
# # 함수 자체를 변수 처럼 사용 show() -> show
# disp(show)
#
#
# a = [1, 2, 3, 4]
#
# def adds():
#     print("this is a test code")

# def pw(x, y):
#     z = x ** y
#     print(z)
#
# pw(2, 5)
# pw(5, 2)
#
# def show (name, age):
#     print(f"Name: {name} Age: {age}")
#
# # 호출 시점에 키를 레이블로 사용
# show(name="멋쟁이사자", age="42")
# # Name: 멋쟁이사자 Age: 42
#
# # 순서를 바꿔도 정상적으로 동작
# show(age="42", name="멋쟁이사자")
# # Name: 멋쟁이사자 Age: 42


# def show(name, age=27):
#     print(f"Name: {name} Age: {age}")
#
#
# # 레이블에 직접 값을 넣어주면 변경되지만
# show(name="멋쟁이사자", age="42")
# # Name: 멋쟁이사자 Age: 42
#
# # 비어있는 레이블은 실제 미리 선언 되어 있는 내용이 들어간다.
# # 만약 age 에 대한 값이 선언되어 있지 않은 상태에서 빈값으로 출력하면 에러
# # TypeError: show() missing 1 required positional argument: "age"
# show(name="멋쟁이사자")
#
#
# # Name: 멋쟁이사자 Age: 27
#
#
# # 가변 인자 실습
# def add(x, y):
#     z = x + y
#     print("Addition: ", z)
#
#
# add(5, 2)
#
#
# def add(*num):
#     z = num[0] + num[1] + num[2]
#     print("Addition *: ", z)
#
#
# add(5, 2, 4)
#
#
# def add(x, *num):
#     z = x + num[0] + num[1]
#     print("Addition *: ", z)
#
#
# add(5, 2, 4)
#
# # 가변 키워드 인자 "**"
# def add(**num):
#     z = num["a"] + num["b"] + num["c"]
#     print("Addition: ", z)
#
# add(a=5, b=2, c=4)
#
#
# # 전역 변수
# def show():
#     x = 10
#     print(x)
#
# show()
#
# def add(y):
#     x = 10
#     print(x)
#     print(x + y)
#
# add(20)
#
# a = 50
#
# def show():
#     x = 10
#     a = x
#     print(x) # local
#     print(a) # local
#
# show()
# print("Global variable a: ", a)
#

# a = 50
# def show():
#     a = 10
#     print("show-a:", a)
#
# show()
# print("global a: ", a)
#
# def show2():
#     global a
#     print("show2-in but global a: ", a)
#     a = 20
#     print("show2-in a: ",a)
#
# show2()
# print("global a :", a)

# fruits = ["apple", "banana", "cherry", "orange"]
#
# print(fruits)
#
# fruits.append("grape")
#
# print(fruits)
#
# fruits.insert(2, "kiwi")
#
# print(fruits)
#
# print(fruits.pop())
# print(fruits.pop(1))
#
# print(fruits)
#
# fruits.append("cherry")
# print("cherry appended", fruits)
#
# print(fruits.index("cherry"))
# print(fruits.remove("cherry"))
# print(fruits.index("cherry"))
# print(fruits.remove("cherry"))
# print(fruits)


# fruits = ["apple", "banana", "cherry", "orange"]
# vegetables = ["carrot", "cucumber"]
#
# grocery = fruits + vegetables
# print(grocery)
#
# numbers = [10, 5, 8, 1, 7]
# numbers.sort()
#
# print(numbers)
# # [1, 5, 7, 8, 10]
#
# slice_numbers = numbers[1:4]
# print("slice_numbers", slice_numbers)
# # slice_numbers [5, 7, 8]
#
# numbers_copy = numbers.copy()
# print("numbers_copy", numbers_copy)
# # numbers_copy [1, 5, 7, 8, 10]
#
# numbers_clone = numbers[:]
# print("numbers_clone", numbers_clone)
# # numbers_clone [1, 5, 7, 8, 10]


# # 사용자 입력으로 리스트 만들기
# user_input_list = []
# num_elements = int(input("Enter Number of Elements: "))
#
# for i in range(num_elements):
#     user_input_list.append(input("Enter Elements: "))
#
# print("User Input List:")
# for element in user_input_list:
#     print(element)


# # 제네레이터
# def fibonacci_generator(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# fibonacci_sequence = fibonacci_generator(10)
#
# for number in fibonacci_sequence:
#     print(number)
#
#
# # 0
# # 1
# # 1
# # 2
# # 3
# # 5
# # 8
# # 13
# # 21
# # 34
#
# def odd_numbers(start, end):
#     while start <= end:
#         if start % 2 != 0:
#             yield start
#         start += 1
#
#
# result = odd_numbers(1, 10)
#
# for num in result:
#     print(num)
# # 1
# # 3
# # 5
# # 7
# # 9
#
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
# result = fibonacci(10)
#
# print(next(result))
# # 0
# # print(next(result))
# print(next(result))
# # 1
#
# for num in result:
#     print(num)
# # 1
# # 2
# # 3
# # 5
# # 8
# # 13
# # 21
# # 34


# def generate_alphabet(start_letter, end_letter):
#     start = ord(start_letter)
#     end = ord(end_letter)
#     while start <= end:
#         yield chr(start)
#         start += 1
#
#
# runner = generate_alphabet('A', 'F')
# for letter in runner:
#     print(letter)
# # A
# # B
# # C
# # D
# # E
# # F


# # 튜플 (Tuple)
# b = (10)  # 정수
# c = (10,)  # 단일 요소 튜플을 생성
# d = (10, 20, 30, 40)
# e = (10, 20, -50, 21.3, '멋쟁이사자')
# f = 10, 20, -50, 21.3, '멋쟁이사자'  # 튜플 e 와 f 는 동일
#
# print("b :", b)
# # b : 10
# print("c :", c)
# # c : (10,)
# print("d :", d)
# # d : (10, 20, 30, 40)
# print("e :", e)
# # e : (10, 20, -50, 21.3, '멋쟁이사자')
# print("f :", f)
# # f : (10, 20, -50, 21.3, '멋쟁이사자')
# print(d, e, f, sep="\n")  # 한번에 출력하면서 줄바꿈 넣기
# # (10, 20, 30, 40)
# # (10, 20, -50, 21.3, '멋쟁이사자')
# # (10, 20, -50, 21.3, '멋쟁이사자')
#
# # 튜플 : 인덱스, 슬라이싱 -> 튜플의 슬라이싱은 튜플이다
# a = (10, 20, -50, 21.3, '멋쟁이사자')
#
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
#
# print(a[:3])
# print(a[1:4])
# print(a[3:])
#
# # 튜플 : 결합과 반복
# a = (10, 20, -50, 21.3, '멋쟁이사자')
# d = (10, 20, 30, 40)
#
# k = a + d
# print("결합 k :", k)
# l = a * 3
# print("반복 l :", l)
#
# # 튜플 : 튜플 내 요소 확인하기
# a = (10, 20, -50, 21.3, '멋쟁이사자')
# print(10 in a)  # True
# print('멋쟁이사자' in a)  # True
# print(15 in a)  # False
#
# # 튜플 : 최소값 최대값
# d = (10, 20, 30, 40, -50)
# print(min(d))
# print(max(d))
#
# # 튜플 : 요소의 개수 세기
# a = (10, 20, -50, 21.3, '멋쟁이사자', 10, 10)
# print(a.count(10))  # 10 이 몇개가 들어있는지
# # 3
#
# # 튜플 : 정렬
# a = (10, 20, -50, 21.3, 10, 16)
# sorted_a = sorted(a)
# print(sorted_a)
# # [-50, 10, 10, 16, 20, 21.3]
#
# # 튜플 : 리스트간 변환
# a = (10, 20, -50, 21.3, 10, 16)
# b = list(a)
# print("Tuple to List :", b)
# print(type(b))
# #Tuple to List : [10, 20, -50, 21.3, 10, 16]
# # <class 'list'>
#
# c = [10, 20, -50, 21.3, 10, 16]
# d = tuple(c)
# print("List to Tuple :", d)
# print(type(d))
# #List to Tuple : (10, 20, -50, 21.3, 10, 16)
# # <class 'tuple'>
#
# # 튜플 : 중첩
# nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# print(nested_tuple)
# # ((1, 2, 3), (4, 5, 6), (7, 8, 9))
#
# a, b, c = nested_tuple
# print(a)
# print(b)
# print(c)
# # (1, 2, 3)
# # (4, 5, 6)
# # (7, 8, 9)
#
# nested_tuple2 = (a, b, c)
# print(nested_tuple2)
# # ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# # set
# a = {10, 20, 30}
# a = {10, 20, 30, "멋쟁이사자", "Bae", 40}
# a = {10, 20, 30, "멋쟁이사자", "Bae", 40, 10, 20}
# # dictionary 가 인덱스를 가지고 잇지 않아서 출력할 때마다 값이 뒤죽박죽으로 출력된다.
#
# print(a)
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {'멋쟁이사자', 'Bae', 20, 40, 10, 30}
# # ...
#
# # 하지만 한번 실행할때 반복했을 때는 같은 형태로만 사용한다.
# i = 0
# while i < 3:
#     print(a)
#     j = 0
#     while j < 3:
#         print(a)
#         j += 1
#     i += 1
#
# print(a)
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
# # {20, 'Bae', 40, 10, 30, '멋쟁이사자'}
#
# b = set()
# print(type(b))
# # <class 'set'>
#
# a.add(50)
# a.update([10, 20, 60, 70])
# print(a)
# # {70, 10, 20, 'Bae', 30, 40, 50, '멋쟁이사자', 60}
#
# a.remove('멋쟁이사자')
# a.discard('멋쟁이사자')
# a.discard(70)
# print(a)
# # {10, 20, 'Bae', 30, 40, 50, 60}
#
# new_set = a.copy()
# print("요소 제거 전 :", new_set)
# new_set.clear()  # 모든 요소 제거
# print("요소 제거 후 - clear() :", new_set)
# # set()
#
#
# # 교집합
# a = {10, 20, 30, "멋쟁이사자", "Bae", 40, 10, 20}
# new_set = a.copy()
# new_set.discard('Bae')
# print(a)
# print(new_set)
#
# intersection_a_new_set = a.intersection(new_set, a)
# print(intersection_a_new_set)
# # {40, 10, 50, 20, 60, 30}
#
# # 여러개의 교집합
# b = {10, 20}
# intersection_a_new_set_b = a.intersection(new_set, a, b)
# print(intersection_a_new_set_b)
# # {10, 20}
#
# # 합집합
# union_a = a.union(new_set)
# print(union_a)
# # {40, 10, 50, 20, 60, 30, 'Bae'}
#
# # 차집합
# difference_a = a.difference(new_set)
# print(difference_a)
# # {'Bae'}
#
# # 부분집합
# issubset_a = a.issubset(new_set)
# print(issubset_a)
# # False (a 는 new_set 의 부분집합이 아니다)
#
# issubset_new_set = new_set.issubset(a)
# print(issubset_new_set)
# # True (new_set 은 a 의 부분집합이 맞다)


# # 딕셔너리 (Dictionary)
# # 빈 딕셔너리 생성
# dict_name = {}
# fees = {}
#
# # 딕셔너리 생성
# stu = {101: "Kim", 102: "Bae", 103: "Hong"}
# fees = {"kim": 2000, "bae": 3000, "hong": 8000}
#
# print(stu[101])
# print(stu[102])
# print(stu[103])
# # Kim
# # Bae
# # Hong
#
# print(fees["kim"])
# print(fees["bae"])
# print(fees["hong"])
# # 2000
# # 3000
# # 8000
#
# # 딕셔너리는 수정이 가능하다.
# stu[102] = "Python"
# print(stu)
# # {101: 'Kim', 102: 'Python', 103: 'Hong'}
#
# stu[104] = "멋쟁이사자"
# print(stu)
# # {101: 'Kim', 102: 'Python', 103: 'Hong', 104: '멋쟁이사자'}
#
# print(102 in stu)
# # True
#
# del stu[102] # 키 102 삭제
# print(102 in stu)
# # False
# print(stu)
# # {101: 'Kim', 103: 'Hong', 104: '멋쟁이사자'}
#
# stu.clear()
# print(stu)
# # {}
#
# # fromkeys
# new_stu = stu.copy()
#
# key = (101, 102, 103)
# value = "멋쟁이사자"
# new_stu = dict.fromkeys(key, value) # 일괄적으로 삽입
#
# print(new_stu)
# # {101: '멋쟁이사자', 102: '멋쟁이사자', 103: '멋쟁이사자'}
#
# print(new_stu[101]) # 파이썬 특유의 코드슈가
# print(new_stu.get(101)) # 함수형으로 접근
# # 멋쟁이사자
# # 멋쟁이사자
#
# print(new_stu.items())
# # dict_items([(101, '멋쟁이사자'), (102, '멋쟁이사자'), (103, '멋쟁이사자')])
# print(new_stu.keys())
# # dict_keys([101, 102, 103])
# print(new_stu.values())
# # dict_values(['멋쟁이사자', '멋쟁이사자', '멋쟁이사자'])
#
# stu = {101: "Kim", 102: "Bae", 103: "Hong"}
# stu[104] = '멋쟁이사자'
# print(stu)
# # {101: 'Kim', 102: 'Bae', 103: 'Hong', 104: '멋쟁이사자'}
#
# stu.update({104: '멋쟁이사자2'})
# print(stu)
# # {101: 'Kim', 102: 'Bae', 103: 'Hong', 104: '멋쟁이사자2'}
#
# print(stu.pop(104))
# # 멋쟁이사자2
# print(stu)
# # {101: 'Kim', 102: 'Bae', 103: 'Hong'}


# class Mobile:
#     fp = 'yes'
#
#
# realme = Mobile()  # 생성자 함수: 클래스를 메모리공간에 띄워주고 앞 변수가 클래스의 기능을 가져다 쓸 수 있게 한다.
# redme = Mobile()
# geek = Mobile()
#
# print(Mobile.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
# # yes
# # yes
# # yes
# # yes
#
# Mobile.fp = 'no'  # 클래스 네임스페이스에 있는 변수를 변경하면 이미 클래스를 전달받은 모든 내용에도 영향을 준다.
#
# print(Mobile.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
# # no
# # no
# # no
# # no
#
# realme.fp = 'realme?'  # 인스턴스 네임스페이스에 있는 변수를 변경하면 범위가 고정되어 변경된다.
#
# print(Mobile.fp)
# print(realme.fp)
# print(redme.fp)
# print(geek.fp)
# # no
# # realme?
# # no
# # no

# # 자식 클래스 선언
# class ChildClassName (ParentClassName):
#     members of Child class


# 메소드 오버로딩 : 수평적 확장 - 추가적재, 같은 메서드에 변수를 더 태움 (매개변수의 개수를 더 태움)
# 메소드 오버라이딩 : 수직적 확장 - 상속받은 메서드를 재정의 (상속받은 부동산이 카페였는데 자식이 키즈카페로 변경)

# class Complex:
#     def __int__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#
#     def __str__(self):
#         return f'{self.real} + {self.imag}i'
#
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# c3 = c1 + c2
# print(c3)

# class Vector(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other): # 연산자 오버로딩
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self): # 연산자 오버라이딩
#         return f'Vector({self.x}, {self.y})'
#
# a = Vector(1, 2)
# b = Vector(3, 4)
#
# print(a)
# print(b)
# # 기본 출력값
# # <__main__.Vector object at 0x000001E6CBB051E0>
# # <__main__.Vector object at 0x000001E6CBB062C0>
#
# # 연산자 오버로딩 후
# # <__main__.Vector object at 0x000002E02D2F51E0>
# # <__main__.Vector object at 0x000002E02D2F6290>
#
# # 연산자 오버라이딩 후
# # Vector(1, 2)
# # Vector(3, 4)
#
# c = a + b
# print(c)
# # 기본 출력값
# # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
#
# # 연산자 오버로딩 후
# # <__main__.Vector object at 0x000002E02D2F6230>
#
# # 연산자 오버라이딩 후
# # Vector(4, 6)

# # 시간 관련
# import time
# current_time = time.time()
# print(current_time)
# # epoch
# # 1686274486.4857082
# print(type(current_time))
# # <class 'float'>
#
# current_time = time.ctime()
# print(current_time)
# # 현재 날짜와 시간
# # Fri Jun  9 10:34:46 2023
# print(type(current_time))
# # <class 'str'>
#
# from datetime import datetime
# dt = datetime(year=2023, month=5, day=5, hour=10, minute=30)
# print(dt)
# # 2023-05-05 10:30:00
# print(type(dt))
# # <class 'datetime.datetime'>
#
# # datetime - now()
# current_datetime = datetime.now()
# print(current_datetime)
# print(type(current_datetime))
# # 2023-06-09 10:40:12.478820
# # <class 'datetime.datetime'>
#
# # date 클래스
# # date 객체 생성
# from datetime import date
# d = date(year=2023, month=5, day=5)
# print(d)
# print(type(d))
# # 2023-05-05
# # <class 'datetime.date'>
#
# # date - today()
# current_date = date.today()
# print(current_date)
# print(type(current_date))
# # 2023-06-09
# # <class 'datetime.date'>
#
# # time 클래스
# # time 객체 생성
# from datetime import time
# t = time(hour=10, minute=30, second=15)
# print(t)
# print(type(t))
# # 10:30:15
# # <class 'datetime.time'>
#
# # timedelta 클래스
# # 두 날짜 사이의 차이 기간
# from datetime import timedelta
# td = timedelta(days=10)
# print(td)
# print(type(td))
# # 10 days, 0:00:00
# # <class 'datetime.timedelta'>
#
# # 두 날짜 비교하기
# from datetime import date
# d1 = date(year=2023, month=5, day=5)
# d2 = date(year=2022, month=6, day=5)
#
# # 날짜의 연산자 오버로딩으로 비교 가능
# print(d1 == d2)
# print(d1 < d2)
# print(d1 > d2)
# # False
# # False
# # True

# class ParentClass:
#     def __init__(self):
#         self.name = 'parent'
#         self.number = 10
#
#     def __str__(self):
#         return f'ParentClass name : {self.name}, number : {self.number}'
#
#     def add_num(self, new_number):
#         print(f'부모: {new_number} 만큼 더해야지')
#         self.number = self.number + new_number
#
# parent = ParentClass()
# # print(parent)
#
#
# # 기본값 출력
# # <__main__.ParentClass object at 0x000001F5A7AA51E0>
#
# # 연산자 오버라이딩 후
# # ParentClass name : parent, number : 10
#
# class ChildClass(ParentClass):  # 부모 클래스를 받아서 자식 클래스 생성
#     def __init__(self):
#         super().__init__()  # init 이후 super 메소드 -> 부모 클래스의 생성자 또는 메소드를 호출하는데 사용
#         # 없으면 ? : IndentationError: expected an indented block after function definition
#         self.name = 'child'
#
#     def __str__(self):
#         return f'ChildClass name : {self.name}, number : {self.number}'
#
#     def add_num(self, new_number): # 메소드 오버라이딩
#         print('말 안듣는 자식: 고정적으로 5 더할거임')
#         self.number = self.number + 5
#
# parent = ParentClass()
# child = ChildClass()
#
# # __init__ 이후 : ChildClass 의 name 을 변경
# print(parent)
# # ParentClass name : parent, number : 10
# print(child)
# # ParentClass name : child, number : 10
#
# # __str__ 이후 : 출력값의 내용 변경
# print(parent)
# # ParentClass name : parent, number : 10
# print(child)
# # ChildClass name : child, number : 10
#
# # ParentClass 에 add_num 추가 후
# print('7일 더 하세요')
# parent.add_num(7)
# child.add_num(7)
# # 부모: 7 만큼 더 해야지
# # 부모: 7 만큼 더 해야지
#
# print(parent)
# print(child)
# # ParentClass name : parent, number : 17
# # ChildClass name : child, number : 17
#
# # ChildClass 에 add_num 추가 후
# print('7일 더 하세요')
# parent.add_num(7)
# child.add_num(7)
# # 부모: 7 만큼 더 해야지
# # 말 안듣는 자식: 고정적으로 5 더할 거임
# # -> Child 에서 정의한 내용대로 출력
#
# print(parent)
# print(child)
# # ParentClass name : parent, number : 17
# # ChildClass name : child, number : 15

# # file 오브젝트
# # 읽기 전용으로 가져오기
# file_object = open('example.txt', 'r')
#
# content = file_object.read()
#
# print(content)
# # Hello, World!
# file_object.close()
#
# # 쓰기
# file_object = open('example.txt', 'w')
#
# content = "This is a new file \nPython is fun!"
# # Hello, World! -> This is a new file \nPython is fun!
#
# file_object.write(content)
#
# file_object.close()

# # with 문을 사용해서 파일 관리
# # 읽기
# with open('example.txt', 'r') as file_object:
#      content = file_object.read()
#      print(content)

# # 덮어 쓰기
# with open('example.txt', 'w') as file_object:
#     content = """This is a mutiline string.
# Python is a versatile language.
# It is easy to learn and use."""
#     print(content)
#     file_object.write(content)
# # This is a mutiline string.
# # Python is a versatile language.
# # It is easy to learn and use.
#
#
# # 파일의 모든 줄을 읽고 출력
# with open('example.txt', 'r') as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print('>', line.strip())
# # > This is a mutiline string.
# # > Python is a versatile language.
# # > It is easy to learn and use.

# # 파일 존재 확인하기 : os.path 사용
# import os
# filename = 'example.txt'
#
# print("파일이 존재하는지 확인하기")
# if os.path.isfile(filename):
#     print(f'P{filename}이 존재합니다.')
# else:
#     print(f'{filename}이 없습니다.')
# # 파일이 존재하는지 확인하기
# # Pexample.txt이 존재합니다.

# # 텍스트 파일에 리스트 쓰기
# file_object = open('list_example.txt', 'w')
# content_list = ["Python", "Java", "C++", "Javascript"]
#
# for item in content_list:
#     file_object.write(item + '\n')
#
# file_object.close()
# # list_example.txt 파일을 생성하고 리스트 생성
# # Python
# # Java
# # C++
# # Javascript
#
# import os
# current_directory = os.getcwd()
# print(current_directory)
# # C:\Users\xormr\workspace\python6th
#
# # os.mkdir('new_directory')
# # os.makedirs('parent_directory/child_directory/grandchild_directory1/2/3/4')
#
# for dirpath, dirnames, filenames in os.walk('.'):
#     print(f"디렉터리 경로: {dirpath}")
#     print(f"디렉터리 이름: {dirnames}")
#     print(f"파일 이름: {filenames}")
#
# # 디렉터리 경로: .
# # 디렉터리 이름: ['.git', '.idea', '.vscode', 'Bootstrap', 'HTML-CSS', 'Javascript', 'ToDoList', 'venv']
# # 파일 이름: ['.gitignore', 'classPractice.py', 'example.txt', 'inde
# # x.js', 'list_example.txt', 'main.py', 'README.md', 'requirements.txt']
# # 디렉터리 경로: .\.git
# # 디렉터리 이름: ['hooks', 'info', 'logs', 'objects', 'refs']
# # 파일 이름: ['COMMIT_EDITMSG', 'config', 'description', 'FETCH_HEAD', 'HEAD', 'index', 'ORIG_HEAD', 'packed-refs']
# # ...

# # 2023.06.12
# class Car:
#     # 클래스 속성
#     wheels = 4
#
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#
#     # method
#     @staticmethod
#     def drive():
#         return "The car is moving"
#
#     def drive(self):
#         return "The car is moving!!"
#
#     def stop(self):
#         return f"The {self.make} has stopped"
#
#
# my_car = Car("KIA", "Morning", "Blue")
#
# # 속성 사용
# print(my_car.make)
# # KIA
#
# # 메서드 호출
# print(my_car.drive())
# print(my_car.stop())
# # The car is moving!!
# # The KIA has stopped


# # 부모 클래스
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         return "the engine is running."
#
#
# # 자식 클래스
# class Car(Vehicle):
#     def start_engine(self):
#         return super().start_engine() + f" It's a {self.make} engine."
#
#
# # 인스턴스 생성 with 부모 클래스
# my_car = Vehicle("Toyota", "Corolla", 2020)
#
# # 인스턴스 생성 with 자식 클래스
# my_car2 = Car("Toyota", "Corolla", 2020)
#
# # 메서드 호출
# print(my_car.start_engine())
# # the engine is running.
#
# print(my_car2.start_engine())
# # the engine is running. It's a car engine.


# # 다중상속
# class Engine:
#     def start(self):
#         return "Engine started"
#
#     def stop(self):
#         return "Engine stopped"
#
#
# class Wheels:
#     def rotate(self):
#         return "Wheels are rotating"
#
#
# class Car(Engine, Wheels):
#     pass
#
#
# my_car = Car()
#
# print(my_car.stop())
# # Engine stopped
# print(my_car.rotate())
# # Wheels are rotation
