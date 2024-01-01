"""
Georgia Institute of Technology - CS1301
Homework 10 - Object Oriented Programming
"""

class Pokemon:
    def __init__ (self, name, level, type, bag, health=50.0, isAlive=True):
        self.name = name
        self.level  = level
        self.type = type
        self.Bag = bag
        self.whiteFlag = Bag.whiteFlag
        self.health = health
        self.isAlive = isAlive

    def loseHealth (self, number):
        if self.isAlive == True:
            self.health -= 5*number
            if self.health <= 0:
                self.isAlive = False

    def gainHealth (self):
        if self.isAlive == False:
            print("{} has fainted! Cannot gain health!".format(self.name))
        elif self.isAlive == True and self.healthPotion == 0.0:
            print("Sorry, {} has no health potions!".format(self.name))
        elif self.isAlive == True and self.healthPotion != 0.0 and self.health <= 30.0:
            self.health += 20.0
            self.healthPotion -= 1.0
        elif self.isAlive == True and self.healthPotion != 0.0 and self.health <= 50.0:
            self.health = 50.0
            self.healthPotion -= 1.0

    def surrender (self):
        self.whiteFlag = True

    def __eq__ (self, other):
        return self.name == other.name and self.type == other.type

    def __str__ (self):
        return "This is {} type Pokemon {} with level {}, current health is {}.".format(self.type, self.name, self.level, self.health)
    

                        
class Bag:

    def __init__(self, healthPotion, whiteFlag):
        self.healthPotion = healthPotion
        self.whiteFlag = whiteFlag
        
    def __eq__(self, other):
        return self.healthPotion == other.healthPotion and self.whiteFlag == other.whiteFlag



class Lobby:
    def __init__ (self, roomName, pokeA, pokeB):
        self.roomName = roomName
        self.pokeA = pokeA
        self.pokeB = pokeB

    def battle (self):
        if self.pokeA.type == "Fire":
            if self.pokeB.type == "Water":
                self.pokeA.loseHealth(2.0)
                self.pokeB.loseHealth(0.5)
            if self.pokeB.type == "Grass":
                self.pokeA.loseHealth(0.5)
                self.pokeB.loseHealth(2.0)
            if self.pokeB.type == "Fire":
                self.pokeA.loseHealth(1.0)
                self.pokeB.loseHealth(1.0)

        if self.pokeA.type == "Water":
            if self.pokeB.type == "Grass":
                self.pokeA.loseHealth(2.0)
                self.pokeB.loseHealth(0.5)
            if self.pokeB.type == "Fire":
                self.pokeA.loseHealth(0.5)
                self.pokeB.loseHealth(2.0)
            if self.pokeB.type == "Water":
                self.pokeA.loseHealth(1.0)
                self.pokeB.loseHealth(1.0)

        if self.pokeA.type == "Grass":
            if self.pokeB.type == "Fire":
                self.pokeA.loseHealth(2.0)
                self.pokeB.loseHealth(0.5)
            if self.pokeB.type == "Water":
                self.pokeA.loseHealth(0.5)
                self.pokeB.loseHealth(2.0)
            if self.pokeB.type == "Grass":
                self.pokeA.loseHealth(1.0)
                self.pokeB.loseHealth(1.0)

        self.gameOver()

    def gameOver (self):
        final = ""
        if self.pokeA.health and self.pokeB.health <= 0.0:
            final = "It's a tie!"
    
        if self.pokeA.whiteFlag == True and self.pokeB.whiteFlag == True:
            final= "It's a tie!"
        
        if (self.pokeA.health == 0.0 or self.pokeA.whiteFlag == True) and self.pokeB.health != 0.0:
            self.pokeB.level += 1
            final = ("{} won the battle".format(self.pokeB.name))

        if (self.pokeB.health == 0.0 or self.pokeB.whiteFlag == True) and self.pokeA.health != 0.0:
            self.pokeA.level += 1
            final = ("{} won the battle".format(self.pokeA.name))
        print(final)

    def __eq__ (self, other):
        return self.roomName == other.roomName
    
pokemon = Pokemon("Squirtle",10,"Water",Bag(10,False))
print(pokemon.Bag)



    
