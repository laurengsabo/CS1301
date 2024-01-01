"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: intramuralGames()
Parameters: gameName (str), numFriends (int)
Returns: None (NoneType)
"""
def intramuralGames(gameName, numFriends):
    gameName = str(gameName)
    numFriends = int(numFriends)
    peopleperc = float(numFriends / 7)
    if (peopleperc < 0.25):
        print ("Let's choose something else.")
    elif (peopleperc <= 0.75):
        print ("We will try out {} for a little bit!".format (gameName))
    else :
        print ("Let's register for {}!!!".format (gameName))

#########################################

"""
Function Name: goShopping()
Parameters: item (str), quantity (int), budget (float)
Returns: moneyLeft (float) or error message (str)
"""
def goShopping(item, quantity, budget):
    item = str(item)
    quantity = float(quantity)
    budget = float(budget)

    if (item == "Shorts"):
        total = quantity * 13.00
    elif (item == "T-Shirts and Tanks"):
        total = quantity * 9.75
    elif (item == "Swimwear"):
        total = quantity * 20.00
    elif (item == "Sunglasses"):
        total = quantity * 7.50
    elif (item == "Slides"):
        total = quantity * 15.50

    if (total <= budget):
        moneyLeft = budget-total
        return (moneyLeft)
    elif (total > budget):
        return ("Not enough money!")

#########################################

"""
Function Name: getDinner()
Parameters: budget (float), diningOption (str)
Returns: restaurantName (str)
"""
def getDinner(budget, diningOption):
    budget = float(budget)
    diningOption = str(diningOption)
    restaurantName = str(restaurantName)
    dinetype = 0

    if (diningOption == "Indoor"):
        dinetype = 1
    elif (diningOption == "Outdoor"):
        dinetype = 2
    elif (diningOption == "Takeout"):
        dinetype = 3
    elif (diningOption == "Delivery"):
        dinetype = 4

    if (budget <= 10.00):
        if (dinetype == 1 or dinetype == 2):
            restaurantName = ("Moe's")
        elif (dinetype == 3 or dinetype == 4):
            restaurantName = ("Chick Fil A")
    elif (budget > 10.00 and budget <= 20.00):
        if (dinetype == 1 or dinetype == 3):
            restaurantName = ("Tin Drum")
        elif (dinetype == 2 or dinetype == 4):
            restaurantName = ("Umma's")
    elif (budget > 20.00 and budget<= 30.00):
        if (dinetype == 1 or dinetype == 2 or dinetype == 3): 
           restaurantName = ("Yeah Burger")
        elif (dinetype == 4):
            restaurantName = ("Flip Burger")
    elif (budget > 30.00 and budget <= 40.00):
        if (dinetype == 1):
            restaurantName = ("Two Urban Licks")
        elif (dinetype == 2 or dinetype == 3 or dinetype == 4):
            restaurantName = ("Gypsy Kitchen")

    return restaurantName
          

#########################################

"""
Function Name: backupRestaurant()
Parameters: budget (float), diningOption (str), backup (str)
Returns: decision (str)
"""
def getDinner(budget, diningOption):
    budget = float(budget)
    diningOption = str(diningOption)
    dinetype = 0
    restaurantName = ""

    if (diningOption == "Indoor"):
        dinetype = 1
    elif (diningOption == "Outdoor"):
        dinetype = 2
    elif (diningOption == "Takeout"):
        dinetype = 3
    elif (diningOption == "Delivery"):
        dinetype = 4

    if (budget <= 10.00):
        if (dinetype == 1 or dinetype == 2):
            restaurantName = ("Moe's")
        elif (dinetype == 3 or dinetype == 4):
            restaurantName = ("Chick Fil A")
    elif (budget > 10.00 and budget <= 20.00):
        if (dinetype == 1 or dinetype == 3):
            restaurantName = ("Tin Drum")
        elif (dinetype == 2 or dinetype == 4):
            restaurantName = ("Umma's")
    elif (budget > 20.00 and budget<= 30.00):
        if (dinetype == 1 or dinetype == 2 or dinetype == 3): 
           restaurantName = ("Yeah Burger")
        elif (dinetype == 4):
            restaurantName = ("Flip Burger")
    elif (budget > 30.00 and budget <= 40.00):
        if (dinetype == 1):
            restaurantName = ("Two Urban Licks")
        elif (dinetype == 2 or dinetype == 3 or dinetype == 4):
            restaurantName = ("Gypsy Kitchen")

    return (restaurantName)


def backupRestaurant(budget, diningOption, backup):
    budget = float(budget)
    diningOption = str(diningOption)
    backup = str(backup)
    restaurantName = getDinner(budget, diningOption)

    if (restaurantName == "Chick Fil A" or restaurantName == "Umma's" or restaurantName == "Gypsy Kitchen" or restaurantName == "Flip Burger"):
        return ("Yay, you can get dinner at your first choice, {}.".format(restaurantName))
    else:
        return ("You'll have to get dinner at {} instead.".format (backup))

#########################################

"""
Function Name: rideShare()
Parameters: number of riders (int), miles(int), rideShareOptionaA (str), rideShareOptionaB (str)
Returns: rideShareOption (str)
"""
def rideShare(riders, miles, rideShareOptionA, rideShareOptionB):
    riders = int(riders)
    miles = float(miles)
    rideShareOptionA = str(rideShareOptionA)
    rideShareOptionB = str(rideShareOptionB)
    priceA = 0.0
    priceB = 0.0

    if (rideShareOptionA == "Uber"):
        if (riders <= 3):
            priceA = (miles * 5.50 + 5)
        elif (riders > 3):
            priceA = (miles * 5.50)

    if (rideShareOptionB == "Uber"):
         if (riders <= 3):
            priceB = (miles * 5.50 + 5)
         elif (riders > 3 ):
            priceB = (miles * 5.50)
            
    if (rideShareOptionA == "Lyft"):
        priceA = 10 + miles * 1.50
        
    if (rideShareOptionB == "Lyft"):
        priceB = 10 + miles * 1.50

    if (rideShareOptionA == "Hitch"):
        if (riders <= 2):
            priceA = (miles * 7.50)
        elif (riders > 2):
            priceA = (miles * 7.50 - (10 * riders))

    if (rideShareOptionB == "Hitch"):
        if (riders <= 2):
            priceB = (miles * 7.50)
        elif (riders > 2):
            priceB = (miles * 7.50 - (10 * riders))

    if (rideShareOptionA == "Taxi"):
        priceA = (18 * miles)

    if (rideShareOptionB == 'Taxi'):
        priceB = (18 * miles)

    if (priceA > priceB):
        return (rideShareOptionB)
    elif(priceA < priceB):
        return (rideShareOptionA)
    elif(priceA == priceB):
        return (rideShareOptionA)

