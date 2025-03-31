a = 10
a_list = [1,2,3,4,5]

print("a : ",a)

a_list[0] = 100
print("a_list : ",a_list)  # [100,2,3,4,5]

# a변수와 b변수는 다른 변수임.
b = a
b = 1000
print("a : ",a)  # 10
print("b : ",b)  # 1000

# 새롭게 복사 : 깊은 복사
# a_list = [1,2,3,4,5]
# b_list = [*a_list]
# b_list[1] = 200

# print(a_list)  # [100,2,3,4,5]
# print(b_list)


### 주소값 복사 : 얕은복사
# # a_list, b_list 다른 리스트 인가??
# a_list = [1,2,3,4,5]
# b_list = a_list
# b_list[1] = 200

# print(a_list)  # [100,2,3,4,5]






# a_list = [1,2,3,4,5]
# sum = 0
# for i in a_list:
#     sum = sum + i
# print(sum)    




# 구구단
# 2 X 1 = 2
# for i in range(2,10):
#     print("[ {} 단 ]".format(i))
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j))
#     print()