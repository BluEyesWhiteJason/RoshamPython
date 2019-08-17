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


def Throw(p1, p2):
    "Makes the player and the opponent throw"
    print("Alright, prepare for battle...")
    print("3...")
    print("2...")
    print("1...")
    print("THROW")

    urThrow = p1.ChooseThrow()

    print("You chose " + urThrow)
    print("Your opponent chose " + p2.ChooseThrow())

def WinLoseDraw(Throw):
    if p1.ChooseThrow() == p2.ChooseThrow():
        return 2
    
    if urThrow is "Rock":
        if p2.ChooseThrow() is "Scissors":
            return 0
        elif p2.ChooseThrow() is "Paper":
            return 1
    if urThrow is "Paper":
        if p2.ChooseThrow() is "Scissors":
            return 1
        elif p2.ChooseThrow() is "Rock":
            return 0
    if urThrow is "Scissors":
        if p2.ChooseThrow() is "Rock":
            return 1
        elif p2.ChooseThrow() is "Paper":
            return 0

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

p1 = User(name)
if num is 1:
    p2 = Rocky("Rocky")
elif num is 2:
    p2 = Rando("Randy")

WinLoseDraw(Throw(p1,p2)) 
