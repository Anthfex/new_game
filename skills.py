currentskills = [
    "{basic_attack}",
    "{Parry}",
    "{new_skill_1}",
    "{new_skill_2}",
    "{new_skill_3}",
    "{new_skill_4}",
    "{new_skill_5}",
]

def skillpage():
    global currentskills
    print(currentskills)
    selection = input("which skill do you want to find information on? if you want to go back to the main menu, type ''exit''")
    if selection == "{basic_attack}":
        print({basic_attack_info})
    elif selection == "{new_skill_1}":
        print({new_skill_1_info})
    elif selection == "{new_skill_2}":
        print({new_skill_2_info})
    elif selection == "{new_skill_3}":
        print({new_skill_3_info})
    elif selection == "{new_skill_4}":
        print({new_skill_4_info})
    elif selection == "{new_skill_5}":
        print({new_skill_5_info})
    elif selection == "exit":
        mainmenu()
    else:
        print("!! invalid selection, please try again !!")
        skillpage()
    