# 3,5,7,9단 홀수단만 출력하시오.

# 시작단과 끝나는 단을 입력받아, 출력하시오.
# 2, 6 -> 2~6단 까지 출력


num1 = int(input("숫자를 입력하세요.>> "))
num2 = int(input("숫자를 입력하세요.>> "))

if num1>num2:
    num1,num2 = num2,num1 #파이썬만 가능

for i in range(num1,num2+1):
    print("[ {} 단 ]".format(i))
    for j in range(1,9+1):
        print("{} X {} = {}".format(i,j,i*j))
    print()
    

# 구구단 출력
# for i in range(num1,num2+1):
#     # if 
#     if i%2 == 0:
#         print("[ {} 단 ]".format(i))
#         for j in range(1,9+1):
#             print("{} X {} = {}".format(i,j,i*j))
#         print()



# # 두수를 입력받아, 두수 사이의 합계를 구하시오.
# # 예 : 1,7 -> 1,2,3,4,5,6,7까지 합을 출력하면 됨.

# # 1,10 -> 10,1

# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# print(num1,num2)

# # if문 비교 num1, num2 num2가 더 큰지 확인
# if num1>num2:
#     # 모든 프로그램 가능
#     # t = num1
#     # num1 = num2
#     # num2 = t
#     num1,num2 = num2,num1 #파이썬만 가능

# sum = 0
# for i in range(num1,num2+1):
#     sum = sum + i
#     print("i : {}, sum : {}".format(i,sum))
    
# print("{}에서 {}까지의 합계 : {} ".format(num1,num2,sum))    