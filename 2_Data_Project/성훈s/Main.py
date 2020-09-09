list = input().split()
a = int(list[0])
b = int(list[1])

if (a > b) :
    for i in list :
        i = b
        print (b, end=" ")
        i += 1
else :
    for i in list :
        i = a
        print (a, end=" ")
        i += 1