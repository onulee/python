

# 리스트 내포 100개 리스트의 값에 +100 전부 해서 출력하시오.
# [100,101,102,103......199]
arr = [i for i in range(100)]
print(arr)

# arr2 = [리스트내포 사용해서 생성]
arr2 = [i+100 for i in arr]
print(arr2)

a_list = []
for i in range(100):
    a_list.append(i)
print(a_list)   

aa_list = [i for i in range(100)] 
print(aa_list)



# arr = [1,2,3,4,5,6,7,8,9,10]
# # arr2 = [1,2,3,4,5,.....10]

# # 리스트 내포
# arr2 = [i+1 for i in range(100)]
# print(arr2)

# a_list = [1,2,3]
# aa_list = ["1m","2m","3m"]

# aaa_list = [str(i)+"m" for i in a_list]
# print(aaa_list)

# # arr2 리스트에 cm 붙여서 리스트 생성하시오.
# arr2_list = [str(i)+"cm" for i in arr2]
# print(arr2_list)

# arr3_list = []
# for i in arr2: arr3_list.append(str(i)+"cm")    
# print(arr3_list)    