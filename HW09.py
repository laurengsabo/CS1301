"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

#########################################

"""
Function Name: add()
Parameters: list of ints (list)
Returns: total (int)
"""
def add(numlist):
    if len(numlist) == 0:
        return 0
    else:
        return numlist[0] + add(numlist[1:])

#########################################

"""
Function Name: decoder()
Parameters: encryption (str)
Returns: codeword (str)
"""
def decoder(encrylist):
    if len(encrylist) == 0:
        return ''
    else:
        if encrylist[0].isalpha():
            return encrylist[0] + decoder(encrylist[1:])
        else:
            return decoder(encrylist[1:])
    
#########################################

"""
Function Name: pirateTreasure()
Parameters: directions (list)
Returns: distance_to_treasure (int)
"""
def pirateTreasure(direct):
    if len(direct) == 0:
        return 0
    else:
        if direct[0] == "up":
            return 1 + pirateTreasure(direct[1:])
        elif direct[0] == "down":
            return (-1) + pirateTreasure(direct[1:])

#########################################

"""
Function Name: lengthDict()
Parameters: list of names (list)
Returns: dictionary mapping names to length (dict)
"""
def lengthDict(names):
    if len(names) == 0 :
        return {}
    else:
        enddict = lengthDict(names[1:])
        enddict[names[0]] = consonF(names[0])
    return enddict

def consonF(name):
    count = 0
    for char in name:
        if char.lower() not in "aeiou":
            count += 1
    return count
        
#########################################

"""
Function Name: balancedStr()
Parameters: string of characters (str)
Returns: isBalanced (bool)
"""
def balancedStr(word):
    if len(word) == 1 or 0:
        return True
    else:
        if word == "":
            return True
        if word[0].islower() == word[len(word)-1].islower() or word[0].isupper() == word[len(word)-1].isupper():
            return balancedStr(word[1:(len(word)-1)])
        else:
            return False
    

