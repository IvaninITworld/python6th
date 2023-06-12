# # 파이썬 패키지
# from MyApp.Handlers.text_handler import handle_text
#
# input_text = "python_basic package practice"
# handle_text(input_text)

# 기본 예외처리
try:
    # result = 10 / 0 # for ZeroDivisionError
    # number = int("Not a number") # for ValueError
    number = 5 + "Not a number"
except ZeroDivisionError:
    print("Error: Division by zero.")
# Error: Division by zero.
except ValueError:
    print("Error: Invalid value.")
# Error: Division by zero.
except TypeError:
    print("Error: Invalid type.")
# Error: Invalid type.

print("Program continues.")
# Program continues.
