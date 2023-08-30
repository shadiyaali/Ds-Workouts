lst = [1,2,3,4,5,6,7,3,9]
lst.sort(reverse=True)
print(lst) 
input = int(input("enter a number")) 
if input <= len(lst):
    largest_sum = sum(lst[:input])
    print("largest sum" , largest_sum)

 
