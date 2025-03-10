port time

def pause(text, delay=1.5):
    print(text)
    time.sleep(delay)

def print_intro():
    print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    pause("Welcome to *Treasure Island*.")
    pause("Your mission is to find the legendary treasure hidden deep within the island.")

def show_lake():
    print(r'''
                         ~  ~    ~      ~    ~
                      ~      __/^\__       ~
               ~     ~     <`     '>  ~      ~
                      ~     \_.-._/    ~  ~
                     ~ ~    ~     ~       ~
               You’ve reached a tranquil lake shimmering under the moonlight.
''')

def show_house():
    print(r'''
        You find a mysterious house with three doors...

               __________     __________     __________
              |  __  __  |   |  __  __  |   |  __  __  |
              | |  ||  | |   | |  ||  | |   | |  ||  | |
              | |__||__| |   | |__||__| |   | |__||__| |
              |  __  __()|   |  __  __()|   |  __  __()|
              | |  ||  | |   | |  ||  | |   | |  ||  | |
              | |  ||  | |   | |  ||  | |   | |  ||  | |
              | |__||__| |   | |__||__| |   | |__||__| |
              |__________|   |__________|   |__________|
                 RED Door       BLUE Door     YELLOW Door
''')

def show_treasure():
    print(r'''
               _.+._
           (^\/^\/^\)
            \@*@*@/
            {_@_@_}
           /  \/  \
     __   /        \   __
    (__)_|  $$$$$$  |_(__)
         \  $$$$$$  /
          \________/
        You found the hidden treasure of Treasure Island! 🎉💰
''')

# Start of Game
print_intro()

choice1 = input('\nYou stand at a misty crossroads in a dark jungle. Do you go "left" or "right"?\n> ').lower()

if choice1 == "left":
    show_lake()
    choice2 = input('\nDo you "wait" for a boat or "swim" across the lake?\n> ').lower()

    if choice2 == "wait":
        pause("\nA ghostly boat arrives. You step aboard and drift silently to the island...")
        show_house()
        choice3 = input('\nWhich door do you choose: "red", "blue", or "yellow"?\n> ').lower()

        if choice3 == "red":
            pause("\nYou open the red door... Flames engulf the room! 🔥")
            pause("It's a trap. Game Over.")
        elif choice3 == "yellow":
            pause("\nYou slowly open the yellow door...")
            pause("It's eerily quiet. Suddenly, wild beasts leap from the shadows! 🐾")
            pause("Game Over.")
        elif choice3 == "blue":
            pause("\nYou open the blue door and step inside...")
            show_treasure()
            pause("🎉 YOU WIN! 🎉")
        else:
            pause("That door doesn't exist... The walls begin to close in.")
            pause("Game Over.")
    else:
        pause("\nYou jump into the lake. The water is cold and deep...")
        pause("Suddenly, an angry trout pulls you under! 🐟")
        pause("Game Over.")
else:
    pause("\nYou head right and fall into a hidden pit trap. There’s no escape.")
    pause("Game Over.")
