lst1 = [1,2,3,4,5,6,3,2,1]
lst2 = [7,5,4,3,2,9]

lst3 = lst1+lst2
# print(lst3)
# s = lst1.append(37)
# for s in lst1:
    # print(s)

# r = set(lst1)
# # print(r)  

s = lst1[::-1]
# print(s)
new = []

for i in lst1:
    if i not in new:
        new.append(lst1[i])
print(new)  


{}
















