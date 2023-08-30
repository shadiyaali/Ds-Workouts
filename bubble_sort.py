# list1 = [10,15,4,23,0]
# print("unsorted list:" ,list1)
# for j in range(len(list1)-1):
#     for i in range(len(list1)-1-j):
#         if list1[i] > list1[i+1]:
#             list1[i],list1[i+1] = list1[i+1],list1[i]
#     #         print(list1)
#     #     else:
#     #         print(list1)
#     # print()            
# print("sorted list:", list1)            



list1= [1,9,6,4,8,0,3,2]
print(list1)
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j] < list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
print(list1)     

 
