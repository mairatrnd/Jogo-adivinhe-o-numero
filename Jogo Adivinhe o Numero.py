from random import randint
secret = randint(1,10)
print("Welcome!")
guess = 0
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You Win!")
    else:
        print("You Lose!")
    if guess < secret:
        print("Too Low!")
    else:
        print("Too High!")
print("Game Over!")
