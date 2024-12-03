'''a = "Arsheen"
for i in a:
    print(i)

#print numbers from 1 to n
n = int(input())
for i in range(1,n+1,1):
    print(i)

n = int(input())
for i in range(n+1):
    print(i)

# print numbers from n to 1
n = int(input())
for i in range(n, 0, -1):
    print(i)

for i in range(1,10,2):
    print(i,end=' ')

for i in range(0,10,2):
    print(i,end=' ')

#multiples of 3
a = int(input())
b = int(input())
for i in range(a, b+1, 1):
    if i % 3 == 0:
        print(i)

# check if a number is prime or not using for loop
n = int(input())
flag = False
for d in range(2, n,1):
    if n % d == 0:
        flag = True
if flag:
    print("Not Prime")
else:
    print("Prime")    '''

n = int(input())
for i in range(1, n + 1, 1):
    for s in range(n-i):
        print(" ", end = '')
    for j in range(i, 2*i, 1):
        print(j, end =  '')
    for k in range(2*i-2, i-1, -1):
        print(k, end = '')
    print()


    

