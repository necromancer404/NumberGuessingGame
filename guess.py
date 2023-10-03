#guess the number
import random
import string
nums=random.choice(list(range(0,101)))
print(nums)
a=int(input("guess a number:\n"))
def numm(a):
    while (a!=nums):
        a=int(input("Enter a number: \n"))
        if (nums-a ==0):
            print("congrats")
            exit(0)
        elif (nums-a<10 and nums-a>0):
            print("A bit low")
            continue
        elif (nums-a>10 ):
            print("Too low")
            continue
        elif (nums-a< -10):
            print('Too high')
            continue
        elif (nums-a> -10 and nums-a <0):
            print("A bit high")
            continue
        else:
            print("not really")
            exit(0)
numm(a)


