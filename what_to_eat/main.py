# import random
# import time
#
# lunch = random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이"])
# dinner = random.choice(["김밥", "쫄면", "돈까스", "치킨"])
#
# print(lunch)
# print(dinner)
import random
import time

# for x in range(30):
#     print(random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이"]))
#     break
#     print("이 문장도 반복되나?")
#     time.sleep(1)


# information = {
#     "고향": "서울",
#     "취미": "영화관람",
#     "좋아하는 음식": "국수"
# }
# print(information)
# print(information.get("취미"))
#
# information2 = {"특기": "피아노", "사는곳": "서울"}
# print(information2.get("특기"))
# print(information2.get("사는곳"))

# information = {
#     "고향": "서울",
#     "취미": "영화관람",
#     "좋아하는 음식": "국수"
# }
# foods = ["김밥", "쫄면", "돈까스", "치킨"]
#
# print(information.get("취미"))
# information["특기"] = "피아노"
# information["사는곳"] = "서울"
#
# del information["좋아하는 음식"]
# print(information)
# print(len(information))
#
# information.clear()
# print(information)
# print(foods[-1])
# print(foods[-2])
# print(foods[-3])
# print(foods[-4])
# # print(foods[-5])
# print(foods[0])
# print(foods[1])
# print(foods[2])
# print(foods[3])
# # print(foods[4])
#
# foods.append("김밥")
# print(foods)

# for x in range(30):
#     print(x)

# foods = ["된장찌개", "피자", "제육볶음"]
# for x in range(len(foods)):
#     print(foods[x])
#
# for x in foods:
#     print(x)

# information = {
#     "고향": "서울",
#     "취미": "영화관람",
#     "좋아하는 음식": "국수"
# }
#
# for x, y in information.items():
#     print(x)
#     print(y)


# python mini project : 오늘 뭐 드실? (feat.codeLion)
import random
import time
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    item = input("음식을 추가해 주세요: ")
    if (item == "q"):
        break
    else:
        lunch.append(item)
    print(lunch)

set_lunch = set(lunch)
while True:
    print(set_lunch)

    item = input("음식을 삭제해주세요: ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))