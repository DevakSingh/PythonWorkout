import random
number = random.randint(0,100)
while True:
    guess = input('Hi! Guess a whole number between 0 and 100. ')
    guess = int(guess)
    
    if guess == number:
        print('Just Right')
        break
    if guess > number:
        print('Too high')
    if guess < number:
        print('Too low')

