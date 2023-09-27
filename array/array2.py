# arry = [1, 2, 3, 4, 5, 1, 4, 3, 1, 4, 5, 4]

# first = 0
# second = 0
# dict = {}

# for i in range(len(arry)):
#     count = 0
#     for j in range(len(arry)):
#         if i != j:
#             if arry[i] == arry[j]:
#                 count += 1
#                 dict[arry[i]] = count

# print(dict) 
# for key, value in dict.items():
#     if value > first:
#         second = first
#         first = value
#     elif value > second and value != first:
#         second = value
 
# second_most = [key for key,value in dict.items() if value == second] 
# print("second largest" , second_most)
            


ar = [1, 8, 5, 8, 5, 6, 7,  1, 5]
count = 0
value = []
for i in range(len(ar)):
    for k in range(1, len(ar)):
        if ar[i] == ar[k]:
            count += 1
    value.append(count)
    count = 0

largest = second_largest = float('-inf')

for num in value:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num


print(second_largest)

print(ar[value.index(second_largest)])