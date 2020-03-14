
num1 = 0
num2 = 1
 
n = int(input())
for _ in range(n):    
    num3 = num1+num2
    num1 = num2
    num2 = num3
    print(num1)

# for i in range(0, n):
#     if i < n:
#         num1, num2 = num2, num1 + num2
#         print(num1)
