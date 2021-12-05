import random
r = random.Random()
secret = r.randint(1, 100)
print(secret)
max = 100
min = 1
win = False
for i in range(5):
    print("please enter number between"+str(min)+"~"+str(max))
    num = int(input())
    if num > secret:
        max = num
    elif num < secret:
        min = num
    else:
        win = True
        break
if win:
    print("you win")
else:
    print("you lose")