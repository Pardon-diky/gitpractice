# pi = 3.14
# radius = int(input("반지름 넣어봐"))
# area = radius * radius * pi

# if radius <= 0:
#     print("잘못된 반지름")
# elif radius >= 50:
#     print("ㅈㄴ큰 원")
#     print("area is", area)
# else:
#     print("일반적인 원입니다.")
#     print("area is", area)

num1 = int(input("1번 숫자를 적어주세요"))
num2 = int(input("2번 숫자를 적어주세요"))

if (num1 > num2):
    print(num2)
elif (num1 < num2):
    print(num1)
else:
    print("num1 과 num2가 같습니다.")