#guess the number
import random
import string
a=0
nums=random.choice(list(range(0,101)))
def numm(a):
    while (a!=nums):
        a=int(input("Enter a number: \n"))
        if (nums-a ==0):
            print("congrats")
            exit(0)
        elif (nums-a <-10 and nums-a > -20):
            print("Think higher")
            continue
        elif (nums-a<10 and nums-a>0):
            print("A bit low")
            continue
        elif (nums-a>10 and nums-a <20):
            print("Think Higher")
            continue
        elif (nums-a>20 ):
            print("Too low")
            continue
        elif (nums-a< -20):
            print('Too high')
            continue
        elif (nums-a> -10  and nums-a <0):
            print("A bit high")
            continue
        else:
            print("not really")
            exit(0)
numm(a)


