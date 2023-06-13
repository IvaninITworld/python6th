# def make_dolcelatte():
#     print("1. 얼음을 넣는다.")
#     print("2. 연유를 30ml 넣는다.")
#     print("3. 찬 우유를 넣는다.")
#     print("4. 에스프레소샷을 넣는다.")
#
# def make_blueberry_smothie():
#     print("1. 블루베리 20g을 넣는다.")
#     print("2. 연유를 300ml 넣는다.")
#     print("3. 얼음을 넣는다.")
#     print("4. 믹서기에 간다.")
#
# def make_simple_latte():
#     print("1. 커피를 넣는다.")
#     print("1. 우유를 넣는다.")
#     print("1. 신나게 섞는다.")
#
# print("돌체라떼 만드는 법")
# make_dolcelatte()
#
# print("블루베리 스무디 만드는 법")
# make_blueberry_smothie()
#
# print("심플 라떼 만드는 법")
# make_simple_latte()



# # 질문은 key 에 저장
# total_list = []
# while True:
#     question = input("질문을 입력해 주세요: ")
#     if question == "q":
#         break
#     else:
#         total_list.append({"질문":question, "답변": ""})
#
# # 답변은 value 에 저장
# for i in total_list:
#     print(i["질문"])
#     answer = input("답변을 입력하세요: ")
#     i["답변"] = answer
# print(total_list)

season = input("현재 계절을 입력하세요.")

if season == "봄":
    print("가디건")
elif season == "여름":
    print("반팔")
elif season =="가을":
    print("코트")
elif season =="겨울":
    print("패딩")