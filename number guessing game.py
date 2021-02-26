import random
import time

counter=0
a=list(range(1,21))

computer=random.choice(a)

print("""The computer choose a number between 1 and 20.
What number do you think this is?""")
input("Press Enter key to start:")
start=time.time()
while True:
    counter+=1
    try:
        reply=int(input("Enter your number:"))
        if reply<0 or reply>20:
            print("Please enter a number between 1 and 20.")
        else:
            if reply<computer and computer-reply>=5:
                print("Your number is too low.")
            elif reply<computer:
                print("You have an entered a low number.")
            elif reply>computer and reply-computer>=5:
                print("Your number is very high.")
            elif reply>computer:
                print("You have entered a high number.")
            else:
                end=time.time()
                print("""Congratulations, you've found the number!
Total number of predictions: {}
The passing time: {}""".format(counter,round(end-start)))
                break
    except:
        print("Please enter integer.")
