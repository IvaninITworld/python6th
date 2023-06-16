from googletrans import Translator

translator = Translator()
# sentence = "좋은 아침이에요"

# sentence = "안녕하세요 코드라이언입니다."

# detected = translator.detect(sentence)
# print(detected.lang)

sentence = input("번역을 원하는 문장을 입력하세요 : ")
dest = input("번역을 원하는 언어를 입력하세요 : ")

result = translator.translate(sentence, dest=f"{dest}")
detect = translator.detect(sentence)

print("\n============= 번역 결과 ============\n")
print(detect.lang,":", result.origin)
print(result.dest,":", result.text)
print("\n====================================\n")