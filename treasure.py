print("Welcome to the treasure Island")
print("Your mission is to find the treasure")
input1 = input("You are at a cross road please select where you want to go? Left or Right\n").lower()
if input1 == "left":
    input2 = input("You have come to the lake, There is a Island in the middle of the lake, Type wait for waiting to the boat, Type swim to swimm to the Island\n").lower()
    if input2 == "wait":
        input3 = input("You have arrived unharmed to the Island. There is a Room with three doors with three colors. Which color do you Pick? Red, Yellow and Blue\n").lower()
        if input3 == "yellow":
            print("    .......   .......    ......     ....        .....   .....      ")
            print("      .....   ...  ....  ....      ....       .....    .....       ")
            print("       ....   ....   ... ...      ....     ....  ..  ....        ")
            print("         .......    .......      ....    .....   ......          ")
            print("\nHurray..! You have won ..! Go get a life instead of wasting your time checking this game..")
        elif input3 =="red" or "yellow":
            print("Game Over, You have opened the door for ragnarok!")
        else:
            print("Unrecognized Input..!")
    elif input2 == "swim":
        print("Game Over..! Lake if filled with Phiranas..")
    else: print("Unrecognized Input..!")
elif input1 == "right":
    print("Game Over, You have lost, This road leads to Pakistan Kaboooom..! : (   try again...!")
else: print("Unrecognized Input..!")
