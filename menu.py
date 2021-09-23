menu = [
    "Stats",
    "Inventory",
    "Party",
    "Skills"
]

def mainmenu():
    global menu
    print(menu)
    selection = input("which menu would you like to select?")
    if selection == "stats":
        print(characterstats())
    elif selection == "inventory":
        print(inventory)
    elif selection == "party":
        print(partymenu)
    elif selection == "skills":
        print(skillmenu)
    else:
        print("!! invalid selection, please try again !!")
        mainmenu()
