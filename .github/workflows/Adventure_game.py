import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(1)


def intro(item, option1, option2):
    print_pause("Midnight, you never thought of this case, but you\n")
    print_pause("need to resolve it - \n ")
    print_pause("the body of her laying on the floor of the second floor.\n")
    print_pause("you know her name " + option1 + " but you baraly knew her,\n")
    print_pause("she came to you week earlier to tell"
                "you about crime she saw\n"
                "two weeks later you found the place she told you about.\n")
    print_pause("In front of you to the left is a warehouse .\n")
    print_pause("To your right is a dock.\n")
    print_pause("In your hand you hold your 6 round (but not very"
                "effective) revolver.\n")


def dock(item, option1, option2):
    if "Thompson submachine gun" in item:
        print_pause("\nYou sneak cautiously into the dock.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an abondon dock"
                    " now.")
        print_pause("\nYou walk back the street.")
    else:
        print_pause("\nYou sneak cautiously into the dock.")
        print_pause("\nIt turns out to be only a abondon dock.")
        print_pause("\nYour eye catches a shadow"
                    "of a machine gun on the dockers table.\n")
        print_pause("\nYou have found!"
                    "Thompson submachine gun loaded with bullets!\n")
        print_pause("\nYou pick it up.")
        print_pause("\nYou walk back out to the street.")
        item.append("Thompson submachine gun")
    street(item, option1, option2)


def warehouse(item, option1, option2):
    print_pause("\nYou approach the back entrance of the warehouse.")
    print_pause("\nYou are about enter the warehouse quite,"
                "opens and see an " + option2 + "'s.")
    print_pause("\nDamm! This is the " + option2 + "'s warehouse!")
    print_pause("\nThe " + option2 + " starts shooting!\n")
    if "Thompson submachine gun" not in item:
        print_pause("You know you have no chance against these 10 men, "
                    "with only having a 6 round revolver.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "Thompson submachine gun" in item:
                print_pause("\nAs the " + option2 + " start shooting,")
                print_pause("\nyou take your new Thompson submachine gun"
                            "and hide behind"
                            "the crate on you right"
                            "to avoid to be hit by a bullet behid a crate")
                print_pause("\nThe Thompson submachine gun was helpfull."
                            "you keep shooting with a"
                            "confident into the targets.\n")
                print_pause("\nthe boss of " + option2 + "'s',"
                            "takes one look at you,")
                print_pause("\nand understands he left alone")
                print_pause("he rise his hands to surrender!\n")
                print_pause("\nYou defeated " + option2 + "'s'."
                            "You are victorious!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your 6 round revolver is not able to"
                            "handle of 10 " + option2 + "'s gang members.\n")
                print_pause("\nYou've been killed!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the street. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            street(item, option1, option2)
            break


def street(item, option1, option2):
    print_pause("Enter 1 to enter the warehouse.")
    print_pause("Enter 2 to sneak into the dock.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            warehouse(item, option1, option2)
            break
        elif choice1 == "2":
            dock(item, option1, option2)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option1 = random.choice(["Anne", "Alice", "Beatrice", "Amanda",
                            "Gina"])
    option2 = random.choice(["italian", "Russian", "Colombians"])
    intro(item, option1, option2)
    street(item, option1, option2)


play_game()
