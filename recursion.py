def count(n):
    if n==0:
        return"success"
    else:
        print(n)
        return count(n-1)    

s = count(5)
print(s)        


def count(n):
    if n==0:
        return "success"
    else:
        print(n)
        return count(n-1)

s = count(10)
print(s)    

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr = [1,2,3,4,5,6]
x =5
s = linear_search(arr,x)
print(s)  

def binary_search(arr,x):
    low =0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return -1            
arr = [1,2,3,4,5,6]
x =5
s = binary_search(arr,x)
print(s) 