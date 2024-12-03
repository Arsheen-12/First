a = 10
b =20
'''print(a > b)   # a is greater than b
print(a < b)   # a is less than b
print(a >= b)  # a is greter than or equal to b 
print(a <= b)  # a is less than or equal to b 
print(a == b)  # a is equal to b
print(a != b)  # a is not equal to b

c1 = a > 10
c2 = b > 10
r1 = c1 and c2
r2 = c1 or c2
r3 = not(c1)
print(r1)
print(r2)
print(r3)

a = True or False
if a:
    print("If Block")
    print("Woohoo!")
else:
    print("Else Block")

n = int(input())
if( n%2 == 0):
    print("Even Number")
else:
    print("Odd Number")
#If the last bit is 1, the number is odd.
#If the last bit is 0, the number is even.

n = int(input())
if(n & 1):
    print("Odd")
else:
    print("Even")

n = int(input())
#Check If the number is between 1 to 10
if n>=1 and n<=10:
    print("too low")
#2=0010,4=0100,3=0011,5=0101
#Check If the number is between 11 to 20
elif n>=10 and n<=20:
    print("medium")

#Check If the number is between 21 to 30
elif n>=20 and n<=30:
    print("large")
#Check if the number is greater than 30 
else:
    print("too large")

x = 15
if x <= 15:
    print("Inside if")
else:
    print("Inside else")'''

x = 5
if x < 6:
    print("Hello")
if x == 5:
    print("Hi")
else:
    print("Hey")
    
