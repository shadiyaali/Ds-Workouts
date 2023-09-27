dic = [('amam',38,),('iman',21,),('lkdbu',87,)]



stock = {item[0]:item[1] for item in dic}
print(stock)
#...............................................................

key = ['aaa','bbb','ccc','ddd']
value = [1,2,3,4]

result = {key:value for key,value in zip(key,value)}
print(result)
#.................................................................


dic1 = {'aaa':1,'bbb':3,'ccc':4,'ddd':0}

results = {key:value for key,value in dic1.items() if value>2}
print(results)
# .................................................................