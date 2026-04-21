import random

random.randint(1,100)

jackpot = random.randint(1,100)

guess = int(input("Chal guess kar:"))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess = int(input("Chal guess kar: "))
    counter+=1
    
print("Sahi Jawab")
print("You took",counter,"attempts")