"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
"""

#########################################

"""
Function Name: dinnerParty()
Parameters: list of names and availabilities (list), day (str)
Returns: list of friends (list)
"""

def dinnerParty(availabilities, day):
    friends = []
    for num1 in range(len(availabilities)):
        for num2 in range(len(availabilities[num1][1])):
            if day == availabilities[num1][1][num2]:
                friends.append(availabilities[num1][0])
            else:
                continue

    return friends
        
    
#########################################

"""
Function Name: whatShouldIWear()
Parameters: list of temperatures (list), list of recommendations (list)
Returns: list of tuples (list)
"""
def whatShouldIWear(temps, recs):
    cold = (temps[0], recs[0])
    med = (temps[1], recs[1])
    hot = (temps[2], recs[2])
    return [cold, med, hot]
    
#########################################

"""
Function Name: cheapMeals()
Parameters: list of strings (list) and budget (float)
Returns: tuple containing menu items (tuple)
"""
def cheapMeals(menu, budget):
    new1menu = []
    new2menu = []
    new3menu = []
    new4menu = []
    for char in range(len(menu)):
        new1menu.append(menu[char].split(" - $"))

    for num in range(len(new1menu)):
       if  float(new1menu[num][1]) <= budget:
           new2menu.append(new1menu[num])
       else:
           continue

    for [element0, element1] in new2menu:
        new3menu.append([float(element1), element0])

    new3menu.sort()

    for num2 in range(len(new3menu)):
        new3menu[num2].remove(new3menu[num2][0])

    for num3 in range(len(new3menu)):
        new4menu.append(str(new3menu[num3][0]))
        
    return tuple(new4menu)

#########################################

"""
Function Name: wednesdays()
Parameters: list of tuples with dates and holidays (list)
Returns: list of holidays (list)
"""
import datetime

def wednesdays(holidays):
    holidaylist = []
    thisdate1 = 0
    thisdate2 = 0
    for (element0, element1, element2, element3) in holidays:
        thisdate1 = datetime.date(element3,element2,element1)
        thisdate2 = thisdate1.weekday()
        if thisdate2 == 2:
            holidaylist.append(element0)
    return holidaylist
        
#########################################

"""
Function Name: starbucksFanatic()
Parameters: list of starbucks menu items (list)
Returns: list of tuples containing menu item name and price (list)
Returns: True or False (bool)
"""
import starbucks

def starbucksFanatic(fallMenuItems):
    addon = ()
    totalprice = 0
    price = 0
    item = ""
    final = []
    
    for drinkpos in range(len(fallMenuItems)):
        item = fallMenuItems[drinkpos]
        price = starbucks.menu(item)
        if price == 0:
            continue
        addon = (fallMenuItems[drinkpos], price)
        totalprice += price
        final.append(tuple(addon))
    final.append(round(totalprice,2))
    return final

    










