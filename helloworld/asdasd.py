# num1 = int(input("1번 숫자를 적어주세요"))
# num2 = int(input("2번 숫자를 적어주세요"))

# if (num1 > num2):
#     print(num2)
# elif (num1 < num2):
#     print(num1)
# else:
#     print("num1 과 num2가 같습니다.

# korean = input("문자열을 입력하시오 : ")
# korean_length = len(korean)
# i = 0

# while (korean_length > 0):
#     print(korean[i:i + 1])
#     i = i + 1
#     korean_length -= 1


# korean = input("문자열을 입력하시오 : ")

# korean_length = len(korean)

# i = 0

# for i in korean_length:
#     print(korean[i])


# char = input("input a string : ")
# cnt = len(char)
# print("Length of input string :", cnt)

# i = 0
# lowerCnt = 0

# while i < cnt:
#     if (char[i] > "a" and char[i] <= "z"):
#         lowerCnt += 1
#     i += 1
# print("the number of lower letters are: ", lowerCnt)


sen = input("Input a string: ")
sen_len = len(sen)
foundStart = False
i = 0


while i < sen_len:
    if (not(foundStart) and sen[i] == 'a'):
        start = i + 1
        foundStart = True
    if sen[i] == "z":
        end = i
        break
i += 1
print("the result is: ", sen[start:end])

#이걸 한 번 추가해보겠습니다. 제발 됐으면 좋겠네요

#영문자가 아닌게 한글이겠죠



