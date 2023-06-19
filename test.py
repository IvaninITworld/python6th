# # 기본 출력 방법
# li = []
# for i in range(5):
#     li.append(i)
# # print(li)
# # [0, 1, 2, 3, 4]

# # 리스트 컴프리헨션
# li2 = [i for i in range(5)]
# print(li2)
# # [0, 1, 2, 3, 4]

# li3 = list(range(5))
# print(li3)
# # [0, 1, 2, 3, 4]

# # 딕셔너리에서 리스트 컴프리헨션
# original = {'key1':'value1'}
# a = {}
# for key, value in original.items():
#     a[key] = value

# # 다음과 같이 리스트 컴프리헨션으로 표현 가능
# original = {'key1':'value1'}
# a = {key: value for key, value in original.items()}

# import sys

# a = [n for n in range(1000000)]
# b = range(1000000)

# print(len(a))
# # 1000000
# print(len(b))
# # 1000000
# print(len(a) == len(b))
# # Ture
# print(sys.getsizeof(a))
# # 8448728
# print(sys.getsizeof(b))
# # 48

# a = [1, 2, 3, 453, 121, 23]
# enumerate(a)
# print(list(enumerate(a)))
# # [(0, 1), (1, 2), (2, 3), (3, 453), (4, 121), (5, 23)]
#
#
# for i in range(len(a)):
#     print(i, a[i])
# # 0 1
# # 1 2
# # 2 3
# # 3 453
# # 4 121
# # 5 23

print(5 / 3)
print(5 // 3)
print(type(5 // 3))
print(type(5 / 3))
# 1.6666666666666667
# 1
# <class 'int'>
# <class 'float'>

# 나머지만 구하는 연산자
print(5 % 3)
# 2

# 몫과 나머지를 한 번에 구하는 연산자
print(divmod(5, 3))
# (1, 2)