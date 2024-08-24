import random

N=random.randrange(1,100)

while True:
    userinput=int(input("Please choose a Number between 1 to 100 :"))

    if userinput==N:
        print('Congrats! You Win')
        break
    elif userinput<N:
        print('You choose a small number please choose a big number')

    else:
        print('You choose a big number please choose a small number')

print("-----Game Over-----")

