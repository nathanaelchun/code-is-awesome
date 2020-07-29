answer = input("Any number you write will be multiplied from 1 to 9.   ")
print(type(answer))
y = int(answer)

for x in range(1,10):
    a = str(y)
    b = str(x)
    c = a+"*"+b+"="
    d = x*y
    e = str(d)
    print(c+e)
    
