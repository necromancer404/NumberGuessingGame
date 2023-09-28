#guess the number
import random
import string
nums=random.choice(list(range(0,101)))
print(nums)
a=int(input("Enter a number: \n"))
if (nums-a ==0):
    print("congrats")
    exit(0)
else:
    print("not really")
    exit(0)


