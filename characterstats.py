characterstatmenu = [
    "Name: {name}",
    "Level: {currentLVL}"
    "EXP: {currentEXP}",
    "to next level:{expto}",
    "Health:{currenthealth} / {maxhealth}"
    "armour: {currentarmour} / {currentARM} damage protection.",
    "weapon: {currentweapon} / {currentDMG} damage.",
]

def characterstats():
    global characterstatmenu
    global mainmenu
    print(characterstatmenu)
    selection = input("do you want to go back to the main menu?")
    if selection == "yes":
        mainmenu()
    elif selection == "no":
        characterstats()
    else:
        print("!! invalid selection, please try again !!")
        characterstats()