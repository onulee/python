# 숫자 2개를 입력받아, 사칙연산 결과값을 출력하시오.
# format()함수 사용
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2
num1 = int(input("1. 숫자를 입력하세요.>> "))
num2 = int(input("2. 숫자를 입력하세요.>> "))
# 변수 : str_print
str_print = "{} / {} = {}".format(num1,num2,num1+num2)
print(str_print)
str_print2 = "{} / {} = {}".format(num1,num2,num1-num2)
print(str_print2)
str_print3 = "{} / {} = {}".format(num1,num2,num1*num2)
print(str_print3)
str_print4 = "{} / {} = {:.2f}".format(num1,num2,num1/num2)
print(str_print4)

#-----------------------------------------------
# 국어, 영어, 수학 점수를 입력받아 평균을 출력하시오
# 합계 : 240
# 평균 : 80.00 

name = input("이름을 입력하세요.>> ")
kor = int(input("국어점수를 입력하세요.>> "))
eng = int(input("영어점수를 입력하세요.>> "))
math = int(input("수학점수를 입력하세요.>> "))
total = kor+eng+math
avg = (kor+eng+math)/3
# format()함수

total_score = "합계 : {}".format(total)
print(total_score)
total_avg = "평균 : {:.2f}".format(avg)
print(total_avg)