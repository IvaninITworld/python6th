class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.number = 10

    def __str__(self):
        return f'ParentClass name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('부모 : ', new_number, '만큼 더해야지')
        self.number = self.number + new_number

    def minus_num(self, new_number):
        print('부모 : ', new_number, '만큼 빼야지')
        self.number = self.number - new_number

    def multiple_num(self, new_number):
        print('아낌없이 주는 부모 : 자식아 넌 곱하기 함수 없지? 괜찮아 내가 줄게')
        self.number = self.number * new_number


class ChildClass(ParentClass):  # 부모 클래스 상속
    def __init__(self):
        super().__init__()
        self.name = 'child'
        self.number = 10

    def __str__(self):
        return f'ChildClass name : {self.name}, number : {self.number}'

    def add_num(self, new_number):  # 부모 클래스에 있던 add_num 메소드를 오버라이딩(Overriding)
        print('말 안듣는 자식 : 고정적으로 5 더할껀데?')
        self.number = self.number + 5

    def minus_num(self, new_number):  # 부모 클래스에 있던 minus_num 메소드를 오버라이딩(Overriding)
        print('말 안듣는 자식 : 난 고정적으로 5 뺄껀데?')
        self.number = self.number - 5

    def discipline(self, order, *num):  # 파이썬은 오피셜로는 오버로딩을 지원하지 않는다. 대신 이렇게 유사하게 가능
        if order == '상냥한 말투':
            print('말 안듣는 자식 : ', num[0], ' 이 숫자 마음에 안들어')
        elif order == '말좀 들어라':
            print('말 듣는 자식 : ', num[0], ', ', num[1], ' 이 숫자 마음에 들어요')


parent = ParentClass()
child = ChildClass()
print('클래스 정보')
print(parent)
print(child)
print()
# 클래스 정보
# ParentClass name : parent, number : 10
# ChildClass name : child, number : 10

print('7을 더하세요')
parent.add_num(7)
child.add_num(7)
print(parent)
print(child)
print()
# 7을 더하세요
# 부모 :  7 만큼 더해야지
# 말 안듣는 자식 : 고정적으로 5 더할껀데?
# ParentClass name : parent, number : 17
# ChildClass name : child, number : 15

print('7을 빼세요')
parent.minus_num(7)
child.minus_num(7)

print(parent)
print(child)
print()
# 7을 빼세요
# 부모 :  7 만큼 빼야지
# 말 안듣는 자식 : 난 고정적으로 5 뺄껀데?
# ParentClass name : parent, number : 10
# ChildClass name : child, number : 10

print('자식만 10 곱하기')
child.multiple_num(10)
print(child)

print('훈육시키기')
child.discipline('상냥한 말투', 1)
child.discipline('말좀 들어라', 10, 20)
# 자식만 10 곱하기
# 아낌없이 주는 부모 : 자식아 넌 곱하기 함수 없지? 괜찮아 내가 줄게
# ChildClass name : child, number : 100
# 훈육시키기
# 말 안듣는 자식 :  1  이 숫자 마음에 안들어
# 말 듣는 자식 :  10 ,  20  이 숫자 마음에 들어요