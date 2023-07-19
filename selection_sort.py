my_list = [3,5,56,32,0,1]
print(my_list)
for i in range(len(my_list)-1):
    min_value = my_list[i]
    for j in range(i+1,len(my_list)):
        if my_list[j] > min_value:
            min_value = my_list[j]  # fixed typo here
    min_ind = my_list.index(min_value)
    if my_list[i] != my_list[min_ind]:
        my_list[i], my_list[min_ind] = my_list[min_ind], my_list[i]
print(my_list)                



list1 = [98,90,67,34,59,12,48]
print(list1)

for i in range(len(list1)-1):
    min_value = list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] > min_value :
             min_value = list1[j]
        min_ind = list1.index(min_value)
        if list1[i] != list1[min_ind:]:
            list1[i],list1[min_ind] = list1[min_ind],list1[i]
print(list1)            

 