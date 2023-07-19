# list1 = [3,5,56,32,0,1]
# print(list1)
# for i in range(len(list1)-1):
#     min_value = list1[i]
#     for j in range(i+1,len(list1)):
#         if list1[j] < min_value:
#             min_value = list1[j]
#     min_ind = list1.index(min_value)
#     if list1[i]!=list1[min_ind]:
#         list1[i],list1[min_ind] = list1[min_ind],list1[i]
# print(list1)                




list2 = [12,34,10,5,8,6,0,1]
print(list2)
for i in range(len(list2)-1):
    min_value = list2[i]
    for j in range(i+1,len(list2)):
        if list2[j] < min_value:
           min_value = list2[j]
    min_ind = list2.index(min_value)
    if list2[i] != list2[min_ind]:
        list2[i],list2[min_ind] = list2[min_ind],list2[i]
print(list2)                

 