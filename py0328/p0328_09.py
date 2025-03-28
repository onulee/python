import random

a_list = random.sample(range(1,45+1),6)

ran_list = []
i = 0
while i<6:
    ran_input = random.randint(1,45)
    if ran_input not in ran_list:
        ran_list.append(ran_input)
        i = i + 1



print(a_list)