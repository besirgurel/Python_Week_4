import math

def pn(xn):
    if xn<=0:
        xn=int("jlkj")
    return xn
print("Enter 4 positive numbers one by one.")

while True:
    try:
        n=int(input("First number:"))
        n=pn(n)
        n2=int(input("Second number:"))
        n2=pn(n2)
        n3=int(input("Third number:"))
        n3=pn(n3)
        n4=int(input("Fourth number:"))
        n4=pn(n4)
        gcd=math.gcd(n,n2,n3,n4)
        lcm=(n*n2*n3*n4)/gcd
        print("LCM:",int(lcm))
        break
    except:
        print("You entered incorrectly.")


