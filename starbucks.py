# import and use the following function for your HW05!
# please do not turn this file in when submitting!

def menu(menuItem):
    prices = {
            'pumpkin spice latte': 4.78,
            'apple crisp macchiato': 5.23,
            'iced apple crisp macchiato': 4.33,
            'pumpkin cream cold brew': 6.18,
            'vanilla sweet cream nitro cold brew': 4.56,
            'bacon, gouda & egg sandwich': 5.45,
            'double-smoked bacon, cheddar & egg sandwich': 5.89,
            'iced pumpkin spice latte': 5.50
    }
    return prices.get(menuItem, 0)
