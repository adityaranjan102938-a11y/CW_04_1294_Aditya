a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))

if (a>b and a>c):
    print("maximum=",a)
elif(b>a and b>c):
    print("maximum=",b)
else:
    print("maximum=",c)
    
    
if (a<b and a<c):
    print("minimum=",a)
elif(b<a and b<c):
    print("minimum=",b)
else:
    print("minimum=",c)