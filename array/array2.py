arry = [1,2,3,4,5,1,4,3,1,4,5,4]

first = 0
second = 0
most_repeated = []

for i in range(len(arry)):
    count = 0
    for j in range(len(arry)):
        if i != j :
            if arry[i] == arry[j]:
                count =+ 1
        if count > first :
            second = first
            first = count
            most_repeated = arry[i]
        elif count < first and count > second:
            second = count

if most_repeated is not None:
    print("second largest" , most_repeated)
            
