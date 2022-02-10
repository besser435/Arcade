def main_notes(): 
    """
    NOTE
    This is a cut down version of my regular arcade game. This is
    because I eventually want to run it on a Feather/Arduino with a
    little display, and I dont need the extras like the audio or
    colored text for that

    """

version = "v0.2"

import board
import random
import time
import sys
import keypad
import neopixel


# setup
km = keypad.KeyMatrix(
    row_pins=(board.D12, board.D5, board.D6, board.D10),
    column_pins=(board.D11, board.D13, board.D9)
)

led_neo = neopixel.NeoPixel(board.NEOPIXEL, 1)     
led_neo.brightness = 0.01
led_neo[0] = (50, 255, 0)

# options
enable_debug_flags_main = 0     # its sad that this is even a thing


def cc():
    for i in range(30): # commands like cls or clear dont work on circuitpython, so this is the workaround
        print()



"""
elif event.key_number == 9 and event.pressed:
    return "*"           
elif event.key_number == 10 and event.pressed:
    return 0  
elif event.key_number == 11 and event.pressed:
    return "#"  
"""

"""
input code copy and paste

while True:
    event = km.events.get()
    if event:
        if event.key_number == 0 and event.pressed: 
            cc()
            rps()  


while True:
    event = km.events.get()
    if event:
        if event.key_number == 11 and event.pressed: 
            ingame_menu(rps)
"""    

def ingame_menu(replay_game):       # make it so any time * is pressed it brings up this menu
    print()
    print("Would you like to:")
    print("1: Play Again")
    print("2: Return to Menu")
    print("3: Quit the Program")
    ask_menu = input()
    if "1" in ask_menu:
        cc()
        replay_game()
    elif "2" in ask_menu:
        cc()
        main_menu()
    elif "menu" in ask_menu:
        cc()
        main_menu()


def rps():
    """
    RPS By Brandon. Carter, and R-Bay
    December 2021

    This version has changes over the normal V1.6 because
    all of this version of the game has to go in a function
    and interface with an external menu.
    This screws some things up.
    """

    version = "v1.7.1"
    
    cc()
    # the plays but with colors
    rolla = "rock"
    rollb = "paper"
    rollc = "scissors"


    # options
    skip_rig_ask = 0        # disables rigging if this is enabled
    enable_asteroid = 1
    cls_after_turn = 0      # clears the terminal after each turn
    match_point = 3


    # storage
    player_score = 0
    comp_score = 0
    enable_rig = 0
    #ask_for_rig = 0
    enable_super_rig = 0          
    player_history = []     
    comp_history = []


    print("Rock Paper Scissors by Brandon, Carter, and R-Bay | " + version + " | November 2021")
    print("First to " + str(match_point) + " points wins!")


    # Operation Asteroid 2 is just a stupid easter egg. serves no purpose except to fuel my "creativity"
    def Operation_Asteroid2():
        if enable_debug_flags_main == True:
            pass    # skips this painful process if need be
        else:
            random_asteroid = random.randint(0,12)                   # low-ish chance of world domination (if the player rigs the game)
            if enable_asteroid == True and random_asteroid == 0:
                print("Game is rigged: " + str(enable_rig))         # I was diagnosed with autism and this has
                time.sleep(0.5)                                     # more of it than I do somehow lmao
                print("is 12-25-27: True")                          # I know its inconsistent and inaccurate,
                time.sleep(1)                                       # but it just has to look cool
                print("loading phase 1...")
                time.sleep(0.2)
                print('"{//null.error.H2A4//"-ai[world_takeover]" does not exist}')
                time.sleep(0.05)
                print("retry.load.C4B8 [wakeup{global}]A9F13")
                time.sleep(0.05)
                print("int-attack(target = D.O.D.)")                # obtains launch codes in case the Neuralink attack fails
                print("int-attack(target = Neuralink)")
                print("{//success.E4A8-play.sound @ Global Neuralink__evil_laugh_taunt__//int -ai[world_takeover]}") # goodbye cruel world!
                time.sleep(0.01)
                print("{issue master.cmd Neuralink.killall}")       # issues the hidden command for all Neuralink devices
                time.sleep(0.03)
                print('{//success.B7D1-Neuralink// ["est. 8.3 bill eliminated"]}')   #    :)
                print('{//global-calc.processing_power{issue "ON" for IoT}')    # I like obscene amounts of processing power
                time.sleep(0.1)
                print('//launch.rockets [count=all arg- s- lightspeed] galactic-payload[asteroid 3(goal=spread)]')   # asteroid 3
                time.sleep(0.1)
                print("Operation Asteroid2 Complete.")               # "I mean, can you really disagree?" -Thanos, probably
                time.sleep(2)
                cc()    # You saw nothing. You saw nothing. You saw nothing. You saw nothing. You s
                # teaching sand to think was a mistake


    class match_fixing:
        global km
        global ask_for_rig
        # added this feature just to practice. in reality its useless and a waste of time
        # enable_rig = computer leans towards rock
        # enable_super_rig = computer always wins





        if skip_rig_ask == True:
            if enable_debug_flags_main == 1: print("                          skip_rig_ask = " + str(skip_rig_ask))
        else:
            nonlocal enable_rig   # took me 20 minutes to figure out where this needed to go haha
            nonlocal enable_super_rig
            
        

        print("Would you like to rig the game? 0/1=(n/y)")
        while True:
            event = km.events.get()
            if event:
                if event.key_number == 0 and event.pressed: 
                    ask_for_rig = True
                    break

                elif event.key_number == 11 and event.pressed:
                    cc()
                    ingame_menu(rps)
                    break

        if ask_for_rig == 1: # no this cant just be put in the if statement above (maybe it can idk im lazy)
            ask_for_super_rig = 0
            print("Would you like to super rig the game? 0/1=(n/y)")

            while True:
                event = km.events.get()
                if event:
                    if event.key_number == 0 and event.pressed: 
                        ask_for_super_rig = True
                        break


            if ask_for_super_rig == 1:
                enable_super_rig = True
                print("Game is rigged: rig = " + str(enable_rig) + " super rig = " + str(enable_super_rig))
                Operation_Asteroid2()
            else: 
                enable_rig = True
                print("Game is rigged: rig = " + str(enable_rig) + " super rig = " + str(enable_super_rig))
                Operation_Asteroid2()
            

               





    def game():
        while True:
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            # had issues with scopes earlier
            if enable_debug_flags_main == 1: print("Game is rigged in def game(): " + str(enable_rig))
            if enable_debug_flags_main == 1: print("Game is super rigged in def game(): " + str(enable_super_rig))


            class player_entry:
                # User inputs their play here
                print("Enter " + rolla + ", " + rollb + ", or " + rollc)

                global player_input
                player_input = input()
                print()
                if "menu" in player_input:
                    ingame_menu(rps)

            class rng:
                global comp_choice
                if enable_rig == True:
                    p_comp_play_rigged = ["rock", "rock", "rock", "paper", "scissors"]
                    comp_choice = random.choice(p_comp_play_rigged)
                    if enable_debug_flags_main == 1: print("                      rng rigged")

                elif enable_super_rig == True:
                    if player_input == "rock":
                        comp_choice = "paper"

                    elif player_input == "paper":
                        comp_choice = "scissors"
                    
                    elif player_input == "scissors":
                        comp_choice = "rock"
                    if enable_debug_flags_main == 1: print("                      rng super rigged")

                else:
                    p_comp_play = ["rock", "paper", "scissors"]
                    comp_choice = random.choice(p_comp_play)
                    if enable_debug_flags_main == 1: print("                      rng normal")


                # adds to history
                if player_input == "rock":
                    print("You chose " + rolla)
                    player_history.append(rolla)
                elif player_input == "paper":
                    print("You chose " + rollb)
                    player_history.append(rollb)
                elif player_input == "scissors":
                    print("You chose " + rollc)
                    player_history.append(rollc)
                else:
                    print("Not a valid answer dummy!")
                    game()


                # roll message thing
                if enable_debug_flags_main == False: # skips this while debugging crap
                    print()
                    print(rolla)
                    time.sleep(0.3)
                    print(rollb)
                    time.sleep(0.3)
                    print(rollc)
                    time.sleep(0.3)
                    print("shoot!")
                    time.sleep(0.5)
                    print()


                if comp_choice == "rock":
                    print("I chose " + rolla)
                elif comp_choice == "paper":
                    print("I choose " + rollb)
                elif comp_choice == "scissors":
                    print("I choose " + rollc)


            class normal_logic:
                if enable_debug_flags_main == 1: print("                      def normal_logic")
                nonlocal comp_score
                nonlocal player_score

                # outcome logic for player choosing rock
                if player_input == "rock" and comp_choice == "paper":
                    print("I win!")
                    comp_score += 1
                elif player_input == "rock" and comp_choice == "scissors":
                    print("I loose :(")
                    player_score += 1

                # paper
                elif player_input == "paper" and comp_choice == "scissors":
                    print("I win!")
                    comp_score += 1
                elif player_input == "paper" and comp_choice == "rock":
                    print("I loose :(")
                    player_score += 1

                # scissors and tie
                elif player_input == "scissors" and comp_choice == "rock":
                    print("I win!")
                    comp_score += 1
                elif player_input == "scissors" and comp_choice == "paper":
                    print("I loose :(")
                    player_score += 1
                elif player_input == comp_choice:
                    print("It's a draw!")
                    print("No points given")


            class points:
                if player_score == 1:       # round end points display
                    print()
                    print("The player has: 1 point")    # tHe PlAyEr hAs 1 PoInT"s"
                else:
                    print()
                    print("The player has: " + str(player_score) + " points")

                if comp_score == 1:
                    print("The computer has: 1 point")
                else:
                    print("The computer has: " + str(comp_score) + " points")


            class history:
                print("Player play history: ", end="")
                print(*player_history, sep = ", ")

                print("Computer play history: ", end="")    # this wont tell you much, its 100% random (until its not)

                if comp_choice == "rock":
                    comp_history.append(rolla)
                elif comp_choice == "paper":
                    comp_history.append(rollb)
                elif comp_choice == "scissors":
                    comp_history.append(rollc)

                print(*comp_history, sep = ", ")


            def game_reset():
                nonlocal player_score
                nonlocal comp_score
                nonlocal player_history
                nonlocal comp_history
                # could probably be done better
                player_score = 0
                comp_score = 0
                comp_history.clear()
                player_history.clear()


            class scores:
                if player_score >= match_point:
                    print()
                    print("You win :(")
                    print("GG!")
                    game_reset()
                    ingame_menu(rps)

                if comp_score >= match_point:
                    print()
                    print("I win the game :D")
                    print("GG!")
                    game_reset()
                    ingame_menu(rps)


            if cls_after_turn == True:
                print()
                input("Press enter to continue ")  # BUG hitting this on the last round closes the game. conflict with the menu
                cc()
            if cls_after_turn == "menu": 
                ingame_menu(rps)
    game()


def bottle_flip():
    print("Bottle Flip by Carter, R-Bay, and Brandon")
    print()

    def game():
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            flip_reg = input("Press e to flip the bottle: ")
            delay = 0.4
            flip_count = 3
            suspense_delay = 1

            # The game
            if "menu" in flip_reg:
                ingame_menu(bottle_flip)
            elif "e" in flip_reg:
                for i in range(flip_count):
                    print("||")
                    time.sleep(delay)
                    print("==")
                    time.sleep(delay)
                flip_reg_outcome = (random.randint(0,4)) # chance to land the flip


                for i in range(3):   # builds suspense
                    time.sleep(delay)
                    sys.stdout.write(".")


                if flip_reg_outcome == 0:
                    time.sleep(suspense_delay)
                    print()
                    print("||")
                    print("The bottle landed")
                    print("You win")
                    ingame_menu(bottle_flip)
                else:
                    time.sleep(suspense_delay)
                    print()
                    print("==")
                    print("The bottle fell over")
                    print("You loose")
                    ingame_menu(bottle_flip)

            # cheat code games
            elif "https://imgur.com/a/yIdxUBW" in flip_reg:
                for i in range(flip_count):
                    print("|| cheater")
                    time.sleep(delay)       # Both versions could just access this as a function for a better
                    print("== cheater")     # implementation, but this works and I only thought of this when it was done
                    time.sleep(delay)

                for i in range(3):
                    print(".", end =" ")
                    time.sleep(delay)

                time.sleep(suspense_delay)
                print("||")
                print("you win... I guess")     # did you really though?
                ingame_menu(bottle_flip)

            elif "menu" in flip_reg:
                ingame_menu(bottle_flip)

            else:
                cc()
                print("Invalid input")
                game()
    game()


def dice():
    # ASCII art for dice found on the Google machine

    while True:
        print()
        amount = input("How many dice would you like to roll? ")
        if "menu" in amount:
            ingame_menu(dice)

        if amount.isdigit():    # checks that the input is an integer
            print("rolling the dice...")
            time.sleep(0.5)

            total = 0
            for i in range(int(amount)):
                roll = random.randint(3,6)
                print()
                if roll == 1:
                    print("|-----|")
                    print("|     |")
                    print("|  O  |")
                    print("|     |")
                    print("|-----|")
                    print("You rolled a 1")
                    total += 1

                elif roll == 2:
                    print("|-----|")
                    print("| O   |")
                    print("|     |")
                    print("|   O |")
                    print("|-----|")
                    print("You rolled a 2")
                    total += 2

                elif roll == 3:
                    print("|-----|")
                    print("|     |")
                    print("|O O O|")
                    print("|     |")
                    print("|-----|")
                    print("You rolled a 3")
                    total += 3

                elif roll == 4:
                    print("|-----|")
                    print("|O   O|")
                    print("|     |")
                    print("|O   O|")
                    print("|-----|")
                    print("You rolled a 4")
                    total += 4

                elif roll == 5:
                    print("|-----|")
                    print("|O   O|")
                    print("|  O  |")
                    print("|O   O|")
                    print("|-----|")
                    print("You rolled a 5")
                    total += 5

                elif roll == 6:
                    print("|-----|")
                    print("|O O O|")
                    print("|     |")
                    print("|O O O|")
                    print("|-----|")
                    print("You rolled a 6")
                    total += 6

            print()
            print("The dice add up to " + str(total))
            print()
            ingame_menu(dice)

        else:
            print("you did a sussy baka D: (Didn't enter an integer)")  # if you need to sue/disappear someone for this,
            ingame_menu(dice)                                           # sue Brandon. I added it, not my group partners.


def ttt():
    try:
        """
        Full disclosure, we borrowed some code from 
        the internet, changed it to fit our needs and
        cleaned up the messy bits

        add version of the board that changes it so
        it line up with a numpad
        """


        board_places = {"1": " " , "2": " " , "3": " " ,
                        "4": " " , "5": " " , "6": " " ,
                        "7": " " , "8": " " , "9": " " }

        board_keys = []

        for key in board_places:
            board_keys.append(key)

        def display_board(board):
            print(board["1"] + "|" + board["2"] + "|" + board["3"])
            print("-+-+-")
            print(board["4"] + "|" + board["5"] + "|" + board["6"])
            print("-+-+-")
            print(board["7"] + "|" + board["8"] + "|" + board["9"])

        def game():
            turn = "X"
            count = 0


            def gg(how):
                if how == 0: 
                    print()
                    print("Game Over")                
                    print(turn + " won!")
                else:   
                    print()
                    print("Game Over")
                    print("It's a Tie!")


            for i in range(10):
                display_board(board_places)
                print("It's your turn, " + turn + ". Move to which place? ")

                move = input()    
                if "menu" in move:
                    ingame_menu(ttt)    

                if board_places[move] == " ":
                    board_places[move] = turn
                    count += 1
                    cc()
                else:
                    cc()
                    print("Dummy, that spot is filled. Choose another place.")
                    continue


                # Win/loose/tie checks
                if count >= 5:
                    if board_places["1"] == board_places["2"] == board_places["3"] != " ":   # across the top
                        display_board(board_places)
                        gg(0)              
                        break
                    elif board_places["4"] == board_places["5"] == board_places["6"] != " ": # across the middle
                        display_board(board_places)
                        gg(0)
                        break
                    elif board_places["7"] == board_places["8"] == board_places["9"] != " ": # across the bottom
                        display_board(board_places)
                        gg(0)
                        break


                    elif board_places["1"] == board_places["4"] == board_places["7"] != " ": # down the left
                        display_board(board_places)
                        gg(0)
                        break
                    elif board_places["2"] == board_places["5"] == board_places["8"] != " ": # down the middle
                        display_board(board_places)
                        gg(0)
                        break
                    elif board_places["3"] == board_places["6"] == board_places["9"] != " ": # down the right
                        display_board(board_places)
                        gg(0)
                        break 
                    

                    elif board_places["1"] == board_places["5"] == board_places["9"] != " ": # diagonal
                        display_board(board_places)
                        gg(0)
                        break
                    elif board_places["3"] == board_places["5"] == board_places["7"] != " ": # diagonal
                        display_board(board_places)
                        gg(0)
                        break 

                # Tie
                if count == 9:
                    gg(1)


                # Swap turns
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"        
            ingame_menu(ttt)
        game()

    except:
        cc()
        print("TTT Error. Hit an invalid key.")  # chad level fix for when you don't enter a valid key
        main_menu()


def game_credits():
    print("Thanks for playing!")
    time.sleep(1)
    print("Arcade made by:")
    time.sleep(1)
    print()

    print("Brandon", "sub-zero")
    time.sleep(0.5)
    print("༼ つ ♥_♥ ༽つ")
    time.sleep(1.2)

    print()
    print()
    print("Carter", "smpoison")
    time.sleep(0.5)
    print("| (• ◡•)| (❍ᴥ❍)")
    time.sleep(1.2)

    print()
    print()
    print("R-bay")
    time.sleep(0.5)
    print("~(˘▾˘~)")

    time.sleep(1.2)
    print()
    print("Special thanks to Joseph")
    time.sleep(1.2)
    print()
    print("The faces don't display properly in the Windows terminal :(")
    print("Maybe use an IDE or a different thingamabob")

    time.sleep(2)
    settings_menu()


def settings_menu():
    global enable_debug_flags_main
    print("Settings options are:")
    print("1: View Credits")
    print("2: Debugging Mode")
    print()
    print("m: Go back to main menu")
    print("q: Quit Game")
    print()

    which_setting = input("Which setting would you like to use? ")

    if "2" in which_setting:
        if not enable_debug_flags_main:
            enable_debug_flags_main = 1
            cc()
            print("Global Debugging Mode Enabled")
            settings_menu()
        else:
            enable_debug_flags_main = 0
            cc()
            print("Global Debugging Mode Disabled")
            settings_menu()
    elif "1" in which_setting:
        cc()
        game_credits()
    elif "m" in which_setting:
        cc()
        main_menu()
    else:
        cc()
        print()
        print("Invalid input")
        settings_menu()

    
def main_menu():    
    
    print("Arcade")
    print("Febuary 2022")
    print(version)


    print('Type "menu" during a game to show the menu')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("Game options are:")
    print("1: Rock Paper scissors")
    print("2: Bottle Flip")
    print("3: Dice")
    print("4: Tic Tac Toe (You need a friend. Too bad you dont have any.)")
    print("5: Fishing game (not implimented)")
    print("#: Settings Menu")
    print()
    print("What would you like to do? ")

    while True:
        event = km.events.get()
        if event:
            if event.key_number == 0 and event.pressed: 
                cc()
                rps()

            elif event.key_number == 1 and event.pressed: 
                cc()
                bottle_flip()

            elif event.key_number == 2 and event.pressed:  
                cc()
                dice()

            elif event.key_number == 3 and event.pressed: 
                cc()
                ttt()

            elif event.key_number == 4 and event.pressed: 
                cc()
                main_menu()

            elif event.key_number == 11 and event.pressed:  
                cc()
                settings_menu()
            else:
                cc()
                print("Not a valid selection")
                main_menu()


main_menu()

