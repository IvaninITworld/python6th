# # SMTP 메일 서버에 연결한다.
# # SMTP 메일 서버에 로그인한다.
# # SMTP 메일 서버로 메일을 보낸다.
#
#
# import smtplib # 파이썬 내장 - SMTP 프로토콜
# from email.message import EmailMessage # 파이썬 내장 - 이메일
# import imghdr # 파이썬 내장 - 이미지 유형 판단
# import re # 파이썬 내장 - 정규 표현식 for 유효성 검사
#
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 465
#
# # 이메일을 만든다.
# # 이메일의 내용을 담는다.
# # 발신자, 수신자를 설정한다.
# message = EmailMessage()
# message.set_content("코드라이언 수업중입니다.")
#
# message["Subject"] = "이것은 제목입니다."
# message["From"] = "###@gmail.com"
# message["To"] = "###@gmail.com"
#
#
#
# # 이미지 파일을 가져와서 읽기
# myfile = open("codelion.png", "rb")
# myfile.read()
# print(myfile.read())
#
# with open("codelion.png", "rb") as image:
#     image_file = myfile.read()
#
# image_type = imghdr.what('codelion', image_file)
# message.add_attachment(image_file, maintype='image', subtype=image_type)
#
# # 서버주소와 포트번호가 필요
# smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
# smtp.login("###@gmail.com", "######")
#
# # 소문자 a-z 대문자 A-Z : 2~3개
# reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
# # print(re.match(reg,"codelion.example@gmail.com"))
#
# smtp.send_message()
# smtp.quit()


# 최종
import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

message["Subject"] = "이것은 제목입니다."
message["From"] = "###@gmail.com"
message["To"] = "###@gmail.com"

with open("codelion.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("###@gmail.com","######")
# 메일을 보내는 sendEmail 함수를 호출해서 실행해보기
sendEmail("###gmailcom")
smtp.quit()