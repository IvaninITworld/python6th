# # 별이 빛나는 밤
# # *****
# # *****
# # *****
# # *****
# # *****
# input_data = int(input("How tall do you want ??"))
#
# for x in range(input_data):
#     print(" " * (input_data - x) + "*" * (x + 1) + "*" * x)
#
# #      *
# #     ***
# #    *****
# #   *******
# #  *********


# # 줄 바꿔서 출력하기
# input_data = int(input("How many times?"))
#
# for x in range(input_data):
#     print(input_data - x)
# # 5
# # 4
# # 3
# # 2
# # 1

# input_data = int(input("target number?"))
#
# for x in range(input_data):
#     if x % 10 == 0:
#         print()
#     print(x + 1, end="\t")
#
# print()
# # 1       2       3       4       5       6       7       8       9       10
# # 11      12      13      14      15      16      17      18      19      20
# # 21      22      23      24      25      26      27      28      29      30

# 로또 번호 추천하기
# 사용자에게 로또를 몇개 살건지 숫자를 입력해달라고 요청
# 1 부터 45 까지의 숫자중에 6개를 랜덤으로 뽑아
# 사용자에게 입력받은 개수 만큼 반복해서 사용자가 원하는 갯수만큼 번호 추천
# 오름차순으로 정렬해서 출력

import random

times = int(input("How many do you want?"))

for x in range(times):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)



