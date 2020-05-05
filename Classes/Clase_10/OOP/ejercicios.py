first_list = (1,3,5,7)
second_list = (2,4,6,8)

new_list = list()

new_list.extend(first_list)
new_list.extend(second_list)
new_list.sort()

print(new_list)