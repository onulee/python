# 1. 딕셔너리 추가
dic = {}
dic['no'] = 1
dic['name'] = '홍길동'
dic['kor'] = 100

print(dic)

#---------------------
# 2. 딕셔너리 삭제
del dic['no']  # del 키를 입력하면 삭제
print(dic)

#----------------------
# 3. 딕셔너리 수정
dic['name'] = '이순신'
print(dic)

# --------------------
# 4. 딕셔너리 출력
print(dic)
# print(dic['total'])  # 없는 키값을 입력하면 에러
print(dic.get('total')) # 없으면 None

print(dic.keys()) # key값을 리스트 형태로 출력
print(dic.values()) #values 값을 리스트 형태로 출력
print(dic.items()) # ('name', '이순신') 튜플형태로 출력


#-------------------------
# 전체 출력 - 키,값 모두 출력
for i,value in enumerate(dic):
    print(f"{i} : {value}")

# 키를 돌려줌.
for key in dic:   
    print(key)  # 키 출력
    print(dic[key]) # 값 출력
    

# 존재하는지 확인
if 'name' in dic:
    print("키값이 존재합니다.")  

if 'no' in dic:
    print(f"no : {dic['no']}")     
else:
    print("no 키는 존재하지 않습니다.")    
     
    
    
    

# # 딕셔너리 생성
# dic1 = {1:"a",2:"b",3:"c"}
# print(dic1)

# students_list = [1,"홍길동",100]
# students = {"no":1,"name":"홍길동","kor":100}
# print(students)

# stu = {'학번':1000,'이름':'홍길동','학과':'컴퓨터공학'}
# print(stu)




# 리스트 자리수 출력
# number = [273,103,5,32,65,9,72,800,99]

# # 자리수 : 3, 값 : 273
# # 자리수 : 3, 값 : 103
# # 자리수 : 1, 값 : 5

# for n in number:
#     value = n
#     length = len(str(n))
#     print(f"자리수 : {length} ,값 : {value}")




# # 100이상의 숫자만 출력하시오.
# # 그리고 그 합을 구하시오.
# sum = 0
# for n in number:
#     if n>=100:
#         sum += n
#         print(n)
# print(f"합계 : {sum}")        