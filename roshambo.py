import random


class Player:
    def __init__(self, name):
        self.name = name
    def ChooseThrow():
        pass
    def GetName():
        pass

class Rocky(Player):
    def __init__(self, name):
        self.name = name
    @staticmethod
    def ChooseThrow():
        return "Rock"
    def GetName():
        return "Rocky"

class Rando(Player):
    def __init__(self, name):
        self.name = name
    @staticmethod
    def ChooseThrow():
        num = random.randint(0,2)
        print(num)
        if num is 0:
            return "Rock"
        elif num is 1:
            return "Paper"
        elif num is 2:
            return "Scissors"
    def GetName():
        return "Randy"

class User(Player):
    def __init__(self, name):
        self.name = name
    @staticmethod
    def ChooseThrow():
        while True:
            sel = input("Enter r/p/s for rock, paper or scissors")
            if sel is "r":
                return "Rock"
            elif sel is "p":
                return "Paper"
            elif sel is "s":  
                return "Scissors"
            else:
                print("Invalid, please select one of r/p/s")
    def GetName():
        return "Jason"



r = Rocky("Rocky")
rand = Rando("Randy")

u = User("Jason")

print("Welcome to ROSHAMBO")
print()
name = input("What is your name?")

print("Alright," + name)

print()
print("Which oppenent would you like to face in the ring?")
print("1) Rocky - the God of rocks I guess")
print("OR")
print("2) Randy - Dude's a wildcard")

num = 0

#eventually need range i guess
while True:
    try:
        print("Please input either 1 or 2")
        num = int(input())
        break
    except ValueError:
        print("That's not an int")




