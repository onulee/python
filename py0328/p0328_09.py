# 구구단 출력하시오.
# 2 X 1 = 2
# 9 X 1 = 9

for i in range(1,10):
    for j in range(2,10):
        print("{} X {} = {}".format(j,i,i*j),end="   ")
    print()



# ## 은행가면 001 002 003... 010 011 012... 999
# for i in range(0,1000):
#     print("{:03d}".format(i))