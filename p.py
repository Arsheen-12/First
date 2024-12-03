a=4
i=1
while i<a:
    bag=''
    j=0
    while j<a:
        bag+='*'
        j+=1
    print(bag)
    i+=1

a=4
i=0
while i<a:
    bag=''
    j=1
    while j<=a:
        bag+=str(j)
        j+=1
    print( bag)
    i+=1

a=4
i=1
while i<=a:
    bag=''
    j=1
    while j<=a:
        bag+=str(a-j+1)
        
        j+=1
    print(bag)
    i+=1

a=4
i=1
while i<=a:
    bag=''
    j=1
    while j<=a:
        bag+=str(a-i+1)
        
        j+=1
    print(bag)
    i+=1

a=4
i=1
while i<=a:
    bag=''
    j=1
    while j<=i:
        bag+=str(j)
        j+=1
    print(bag)
    i+=1

a=4
i=1
while i<=a:
    bag=''
    j=1
    while j<=i:
        bag+=str(i)
        j+=1
    print(bag)
    i+=1

a=4
i=1
while i<=a:
    bag=''
    j=1
    p=i
    while j<=i:
        bag+=str(p)
        p+=1
        j+=1
    print(bag)
    i+=1

a=4
i=1
while i<=a:
    bag=''
    j=1
    while j<=i:
        bag+=str(j)
        j+=1
    print(bag)
    i+=1

a=4
i=1
while i<=a:
    bag=''
    j=1
    while j<=i:
        bag+='*'
        j+=1
    print(bag)
    i+=1

''''n = int(input())
i = 1
while i <= n:
    j = 1
    bag=''
    while j <= i:
        if i==1 or j==i:
            bag+='1'
            print(bag)
        elif j > 1 and j < i:
            bag+='2'
            print(bag)
        else:
            pass
        j = j + 1
    print()
    i = i + 1'''
a=4     #Reverse Right Angle
i=1
while i<=a:
    bag=''
    j=i
    while j<=a:
        bag+='*'
        j+=1
    print(bag)
    i+=1
