import pygame
from pygame.locals import *
import pygame as pg
import random

guesses = 0

myname = input("Hello! What is your name? ")

number = random.randint(1,100)
print(f"I have a special game for you today {myname}. I am thinking of a number between 1 and 100, and I want you to guess it. I will give you 10 guesses.")

for guesses in range(10):
    guess = int(input("Take a guess "))

    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too high")

    if guess == number:
        break




if guess == number:
    guesses += 1
    print(f"Good job {myname}! You guessed it in {guesses} guesses!")

if guess != number:
    print(f"Sorry. The number I guessed was {number}")


