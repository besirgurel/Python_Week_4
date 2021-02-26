import math,mul,div,sum,ad
while True:
    try:
        operation=input("Choose an operation(+,-,*,/) :")
        if operation!="+" and operation!="-" and operation!="*" and operation!="/":
            print(int(""))
        else:
            fn=float(input("Enter a number:"))
            sn=float(input("Enter another number:"))
            if operation=="+":
                a=sum.addition(fn,sn)
                if a=="N":
                    break
            elif operation=="-":
                a=ad.subtraction(fn,sn)
                if a=="N":
                    break
            elif operation=="*":
                a=mul.multiplication(fn,sn)
                if a=="N":
                    break
            else:
                a=div.division(fn,sn)
                if a=="N":
                    break
    except:
        print("Error detected. Please try again.")