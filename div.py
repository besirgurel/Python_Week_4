import math

def division(x,y):
    result = math.ceil(x/y)
    print(f"Result = {result}")
    while True:
        reply = input("Would you like to do something else? (Y/N)")
        if reply == "N":
            return reply
        elif reply != "Y" and reply != "N":
            print("Print enter one of the characters Y and N.")
        else:
            break