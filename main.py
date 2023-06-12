# 파이썬 패키지
from MyApp.Handlers.text_handler import handle_text

input_text = "python_basic package practice"
handle_text(input_text)
# 변환된 텍스트: PYTHON_BASIC PACKAGE PRACTICE

# # 기본 예외처리
# try:
#     # result = 10 / 0 # for ZeroDivisionError
#     # number = int("Not a number") # for ValueError
#     number = 5 + "Not a number"
# except ZeroDivisionError:
#     print("Error: Division by zero.")
# # Error: Division by zero.
# except ValueError:
#     print("Error: Invalid value.")
# # Error: Division by zero.
# except TypeError:
#     print("Error: Invalid type.")
# # Error: Invalid type.
#
# print("Program continues.")
# # Program continues.

# # custom exception
# class CustomException(Exception):
#     def __init__(self, message):
#         self.message = message
#
# try:
#     raise CustomException("This is a custom exception.")
# except CustomException as e:
#     print(f"Error: {e.message}")

# # 파이썬 알고리즘
# a = ['a1', 'b2', 'c3']
#
# # 방법 1: range 사용
# for i in range(len(a)):
#     print(i, a[i])
# # 0 a1
# # 1 b2
# # 2 c3
#
# # 방법 2: 직관적인 방법
# i = 0
# for v in a:
#     print(i, v)
#     i += 1
# # 0 a1
# # 1 b2
# # 2 c3
#
# # 방법 3: enumerate
# for i, v in enumerate(a):
#     print(i, v)
# # 0 a1
# # 1 b2
# # 2 c3

# # 리스트 메서드의 시간 복잡도
# len(a) # 시간 복잡도 : O(1) - 전체 요소의 개수를 리턴한다.
# a[i] # 시간 복잡도 : O(1) - 인덱스 i의 요소를 가져온다.
# a[i:j] # 시간 복잡도 : O(k) - 인덱스 i 부터 j 까지 슬라이스의 길이만큼인 k 개의 요소를 가져온다. 이 경우 객체 1개에 대한 조회가 필요하므로 O(k) 이다.
# elem in a # 시간 복잡도 : O(n) - elem 요소가 존재하는지 확인한다. 처음부터 순차 탐색하므로 n 만큼 시간이 소요된다.
# a.count(elem) # 시간 복잡도 : O(n) - elem 요소의 개수를 리턴한다.
# a.index(elem) # 시간 복잡도 : O(n) - elem 요소의 인덱스를 리턴한다.
# a.append(elem) # 시간 복잡도 : O(1) - 리스트 마지막에 elem 요소를 추가한다.
# a.pop() # 시간 복잡도 : O(1) - 리스트 마지막 요소를 추출한다. 스택의 연산이다.
# a.pop(0) # 시간 복잡도 : O(n) - 리스트 첫 번째 요소를 추출한다. 큐의 연산이다. 이 경우 전체복사가 필요하므로 O(n)이다.
# del a[i] # 시간 복잡도 : O(n) - 인덱스 i 의 요소를 삭제한다.
# a.sort() # 시간 복잡도 : O(n log n) - 정렬한다. 팀소트(Timsort)를 사용하며, 최선의 경우 O(n)에도 실행될 수 있다.
# min(a), max(a) # 시간 복잡도 : O(n) - 최솟값/최댓값을 계산한다.
# a.reverse() # 시간 복잡도 : O(n) - 뒤집는다. 리스트는 입력 순서가 유지되므로 뒤집게 되면 입력 순서가 반대로 된다.

# # dictionary
# words = ['apple', 'bat', 'bar', 'atom', 'book']
# by_letters = {}
#
# for word in words:
#     letter = word[0]
#     if letter not in by_letters:
#         by_letters[letter] = [word]
#     else:
#         by_letters[letter].append(word)
#
# print(by_letters)
# # {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
# print(by_letters['c'])
# # KeyError: 'c'


# from collections import defaultdict
# words = ['apple', 'bat', 'bar', 'atom', 'book']
# by_letters = defaultdict(list)
# for word in words:
#     by_letters[word[0]].append(word)
# print(by_letters)
# # defaultdict(<class 'list'>, {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']})
# print(by_letters['c'])
# # []




