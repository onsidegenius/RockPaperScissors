#!/usr/bin/python
# coding: utf-8
import os, sys
import random
import time
from pip._vendor.colorama import Fore
from enum import Enum


os.system("")


def getShapeFromString(mInput):
    return {
        "r": Shape.ROCK,
        "p": Shape.PAPER,
        "s": Shape.SCISSORS,
    }[mInput]

def getShapeFromInt(mNumber):
    return {
        1: Shape.ROCK,
        2: Shape.PAPER,
        3: Shape.SCISSORS,
    }[mNumber]

def getShapeString(mShape):
    return {
        Shape.ROCK: "Rock",
        Shape.PAPER: "Paper",
        Shape.SCISSORS: "Scissors",
    }[mShape]

def whoWins(playerShape, computerShape):
    if playerShape == computerShape:
        return Result.DRAW
    if playerShape == Shape.SCISSORS and computerShape == Shape.PAPER:
        return Result.PLAYER
    if playerShape == Shape.ROCK and computerShape == Shape.SCISSORS:
        return Result.PLAYER
    if playerShape == Shape.PAPER and computerShape == Shape.ROCK:
        return Result.PLAYER
    return Result.COMPUTER


class Result(Enum):
    PLAYER = 1
    COMPUTER = 2
    DRAW = 3

class Shape(Enum):
    SCISSORS = 1
    ROCK = 2
    PAPER = 3

class Game:
    print()
    print()
    print(
        "Rock(" + Fore.LIGHTMAGENTA_EX + "r" + Fore.RESET + "), Paper(" + Fore.LIGHTMAGENTA_EX + "p" + Fore.RESET + "), Scissors(" + Fore.LIGHTMAGENTA_EX + "s" + Fore.RESET + ")")
    print()
    print()
    time.sleep(1)

    playerScore = 0
    computerScore = 0
    currentRound = 1

    totalRounds = input("Rounds: ")
    while not totalRounds.isnumeric():
        print("Must be a number.")
        print()
        totalRounds = input("Rounds: ")
    print()
    totalRounds = int(totalRounds)
    time.sleep(0.5)

    while currentRound <= totalRounds:
        inputShape = input("Your shape: ")
        while inputShape != "r" and inputShape != "p" and inputShape != "s":
            print("Must be a legal shape.")
            print()
            inputShape = input("Your shape: ")
        playerShape = getShapeFromString(inputShape)
        print()
        time.sleep(0.5)

        print(Fore.MAGENTA + "Ro")
        time.sleep(0.25)
        print("Sham")
        time.sleep(0.25)
        print("Bo!")
        time.sleep(0.25)
        print(Fore.RESET)

        rnd = (random.randrange(1, 4))
        computerShape = getShapeFromInt(rnd)
        result = whoWins(playerShape, computerShape)

        if result == Result.DRAW:
            print(Fore.RESET + "You: " + Fore.CYAN + getShapeString(playerShape), end= "   ")
            print(Fore.RESET + "Computer: " + Fore.CYAN + getShapeString(computerShape))
            time.sleep(0.25)
            print(Fore.YELLOW + ";|")
            print(Fore.RESET)
            time.sleep(0.5)
            print("Score: " + str(playerScore) + " to " + str(computerScore))

        elif result == Result.PLAYER:
            playerScore = playerScore + 1
            currentRound = currentRound + 1
            print(Fore.RESET + "Du: " + Fore.GREEN + getShapeString(playerShape), end="   ")
            print(Fore.RESET + "Computer: " + Fore.RED + getShapeString(computerShape))
            time.sleep(0.25)
            print(Fore.YELLOW + ";)")
            print(Fore.RESET)
            time.sleep(0.5)
            print("Score: " + Fore.YELLOW + str(playerScore) + Fore.RESET + " to " + str(computerScore))

        elif result == Result.COMPUTER:
            computerScore = computerScore + 1
            currentRound = currentRound + 1
            print(Fore.RESET + "Du: " + Fore.RED + getShapeString(playerShape), end="   ")
            print(Fore.RESET + "Computer: " + Fore.GREEN + getShapeString(computerShape))
            time.sleep(0.25)
            print(Fore.YELLOW + ":(")
            print(Fore.RESET)
            time.sleep(0.5)
            print("Score: " + str(playerScore) + " to " + Fore.YELLOW + str(computerScore) + Fore.RESET)

        print()
        print()
        time.sleep(1)
        
        if playerScore > totalRounds / 2 or computerScore > totalRounds / 2:
            currentRound = totalRounds + 1

    if playerScore == computerScore:
        print(Fore.CYAN + "Draw! You'll have better luck next time.")
    elif playerScore > computerScore:
        print(Fore.GREEN + "You win! You are a true genius.")
    elif computerScore > playerScore:
        print(Fore.RED + "You loose! You need to practice a lot.")

    print(Fore.RESET)
