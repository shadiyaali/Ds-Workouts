def prime(n):
  if n<2:
    return False
  for i in range(2,n):
    if n % i ==0:
      return False
    return True

prime_stack = []

for num in range(2,20):
  if  prime(num):
    prime_stack.append(num)
                 
print(prime_stack)     


 
