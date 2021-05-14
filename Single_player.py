import random
# pip install random

roll_again = input("Do you want to roll? ")
res = []
while roll_again == "y" or roll_again == 'yes':
    s = random.randint(1, 6)
    res.append(s)
    print([s])
    roll_again = input("Do you want to roll again? ")
print("Sum of rolled numbers: ", sum(res))
print("rolled  numbers", res)
print("game has end!")
