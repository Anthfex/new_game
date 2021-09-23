inventorylist = [
    "INVENTORY",
    "{item1}",
    "{item2}",
    "{item3}",
    "{item4}",
    "{item5}",
    "{item6}",
    "{item7}",
    "{item8}",
    "{item9}",
    "{item10}",
    "{item11}",
    "{item12}",
    "{item13}",
    "{item14}",
    "{item15}",
    "BAG SPACE: {currentitemcount} / 15"
    "GOLD: {currentgold}"
]

def inventory():
    global inventorylist
    print(inventorylist)
    invselection = input("which item do you want to inspect?, if you want to go back to the main menu type ''exit''")
    if invselection == "{item1}":
        print({item1_info})
    elif invselection == "{item2}":
        print({item2_info})
    elif invselection == "{item3}":
        print({item3_info})
    elif invselection == "{item4}":
        print({item4_info})
    elif invselection == "{item5}":
        print({item5_info})
    elif invselection == "{item6}":
        print({item6_info})
    elif invselection == "{item7}":
        print({item7_info})
    elif invselection == "{item8}":
        print({item8_info})
    elif invselection == "{item9}":
        print({item9_info})
    elif invselection == "{item10}":
        print({item10_info})
    elif invselection == "{item11}":
        print({item11_info})
    elif invselection == "{item12}":
        print({item12_info})
    elif invselection == "{item13}":
        print({item13_info})
    elif invselection == "{item14}":
        print({item14_info})
    elif invselection == "{item15}":
        print({item15_info})
    elif invselection == "exit":
        mainmenu()
    else:
        print("!! invalid selection, please try again !!")
        inventory()