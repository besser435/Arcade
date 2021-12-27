

# If it's worth doing, it's worth overdoing.
# Thats why this is so long and painful.


def main_notes():   # to collapse the text below in the IDE  
    """
    NOTE
    Arcade for IFT101 final project
    Submitted on 12-4-21
    Written by Brandon, Carter, and R-Bay
    https://github.com/besser435/Arcade.py


    This document has some important things to note:
    https://docs.google.com/document/d/1z0a9XA7nS2HSgqRiNl7OAoM2NchoCG0EkOCNeLv4DfM/edit?usp=sharing

    linux_mode disables a few things so this can run on there.
    Hasn't been tested or implimented for a while, this might not run on linux anymore
    The GUI stuff might not work regardless
    Who am I kidding it doesnt work at all

    We are aware that this is a royal mess.
    In the future we hope to do better.

    Reaction time and maybe the music requires to be ran on Windows

    This game requires a few libraries, they can be found below.
    A batch file is included if you dont have them or are too
    lazy to copy and paste the stuff below

    """
    # SPAGHETTI CODE STATUS: ITALIAN
    # HOURS WASTED ON DEBUGGING AND USELESS FEATURES SO FAR: 614

version = "v1.5.3"

import traceback    # prevents the terminal from closing if
try:                # there is an error so you can read it

    import webbrowser, keyboard, random, pygame, time, sys, PIL, os   # pip install gtts
    from colorama import init                   # pip install colorama
    init()
    from colorama import Fore, Back, Style
    init(autoreset=True)
    pygame.init()                               # pip install pygame
    pygame.mixer.init()
    import pygame_menu                          # pip install pygame_menu
    from time import perf_counter
    from statistics import mean
    from PIL import ImageGrab                   # pip install pillow
    from art import *                           # pip install art
    from tkinter import *                       # pip install tk
    from tkinter import messagebox
    import tkinter.font as font
    import tkinter as tk


    # options
    enable_music = 1
    rickroll = 1
    global_cut_music = 0            # see message below
    game_count = 8                  # used for e_egg
    enable_debug_flags_main = 0     # its sad that this is even a thing
    linux_mode = 0                  # only tested on Ubuntu, it works there
    music_vol = 0.7

    """
    Enable this option if you don't have the music files, or are getting
    errors related to it. This option basically disables anything 
    relating to music so you can run the game without it.

    However the music does "improve" the experience
    The music is in the same zip file as this .py file
    """

    # storage
    e_egg = 0


    def cc():   # shortened this long command to cc()
        os.system("cls" if os.name == "nt" else "clear")
        # the long version is required in some places
    cc()


    def cd():   # changes directory to where the .py file is. for the audio
        try:
            abspath = os.path.abspath(sys.argv[0])
            dname = os.path.dirname(abspath)
            os.chdir(dname)
        except:
            print(Fore.RED + "cd error")
    cd()


    def debug_flags():
        print(Fore.YELLOW + "          Message from def debug_flags")    # we had spaghetti code okay
        print(Fore.YELLOW + "          Linux compatibility Mode: " + str(linux_mode))
        print(Fore.YELLOW + "          Debugging mode: " + str(enable_debug_flags_main))
        print(Fore.YELLOW + "          e_egg progress: " + str(e_egg))
        print()
        print(Fore.YELLOW + "          Music nuke: " + str(global_cut_music))        
        print(Fore.YELLOW + "          Enable music: " + str(enable_music))
        print(Fore.YELLOW + "          Rick Roll: " + str(rickroll))
        print(Fore.YELLOW + "          CWD: " + os.getcwd())


    def music_play():
        #try:    # music stuff can be prone to errors, so thats why it is special and gets its own thing
            global current_song
            global rand_song
            global music_vol
            songs = ["Climate Nuclear.mp3", "The Egg.mp3", "Nuclear Death Toll.mp3"]
            rand_song = random.choice(songs)
            pygame.mixer.music.set_volume(music_vol)
            #print(music_vol)
            
            if enable_music == True:
                if global_cut_music == False:     # its in music_logic, but still needed. sometimes logic is skipped
                    for x in range(1):  #IDK why but PyGame needs audio in loops (I think)
                        pygame.mixer.music.load(rand_song)   # egg
                        pygame.mixer.music.play(fade_ms = 4000)
                        pygame.event.wait()
        #except:
            #print(Fore.RED + "music_play error")    


    def music_logic():
        try:
            if global_cut_music == False and enable_music == True:       
                    if rickroll == False: 
                        music_play()
                    elif rickroll == True:
                        # You know the rules and so do I
                        pygame.mixer.music.set_volume(music_vol)
                        pygame.mixer.music.load("wehadto.mp3")
                        pygame.mixer.music.play()
                        pygame.event.wait()
                        # Never gonna let you down               
        except:
            print(Fore.RED + "music_logic error")    
    music_logic()


    def gui_music(): 
        # NOTE toggle not hooked up, volume broken
        def toggle_music_gui():
            global enable_music
            global rickroll
            if not enable_music:
                enable_music = 1
                cc()
                if global_cut_music == False: print("Music On")
                music_play()

                size = len(rand_song)   # this only works sometimes for some reason
                mod_string = rand_song[:size - 4] # removes file extension
                print("Now playing: " + Fore.LIGHTMAGENTA_EX + mod_string)

                #settings_menu() BUG causes runtime error

            else:
                cc()
                enable_music = 0
                if global_cut_music == False: print("Music Off")
                pygame.mixer.music.fadeout(750)
                rickroll = 0


        cc()
        print("Close GUI to continue...")   # cant do anything else while its open
        try:    # throws errors unde the rug so the rest of the code can continue.
            root = Tk()
            while True:
                # options
                buttonFont = font.Font(family="Comic Sans MS", size=15) # button text properties
                set_cursor = "heart"    # trek
                btn_color = "green"
                btn_background = "gray60"
                background_color = "gray15"

                
                # window setup
                root.title("peak ui design")
                root.geometry("284x234")
                root["bg"] = "gray15"   # keep this idk what it does

                
                label_font = font.Font(family="Comic Sans MS", size=15)
                label1 = tk.Label(master=root, text="Music Options", bg=background_color,font=label_font,fg = "green2")
                label1.grid(column=0, row=0)


                def change_vol(vol):
                    global music_vol
                    music_vol = float(vol)
                    #print(vol)
                    music_play()


                def dark_mode():  #regular buttons. will go to light_mode if light mode is enabled in the options menu
                    # Toggle
                    btn_tog = Button(text = "Toggle Music", # this is kind of redundant because of the slider but ehhhhh
                        fg = "green", command=toggle_music_gui, bg=btn_background, height=1, width=11, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=1)

                    # New Song
                    btn_new = Button(root, text = "New Song",
                        fg = btn_color, command=music_play, bg=btn_background, height=1, width=11, font=buttonFont, cursor=set_cursor)
                    btn_new.grid(column=2, row=1)

                    # Close - this is so errors arent thrown. use this instead of the X in Windows
                    btn_new = Button(root, text = "Close",
                        fg = "red3", command=root.destroy, bg=btn_background, height=1, width=11, font=buttonFont, cursor=set_cursor)
                    btn_new.grid(column=2, row=2)

                    # Volume 
                    label_font = font.Font(family="Comic Sans MS", size=19)
                    vol_lab = tk.Label(root, text="Volume", bg=background_color,font=label_font,fg = "green2")
                    vol_lab.grid(column=0, row=5)

                    # Can't get past 0.4 for some reason. But it's so broken and useless I don't really care
                    vol_scale = Scale(root, command=change_vol, orient=HORIZONTAL,bg="gray60", length=135, width=15, 
                    sliderlength=10, from_=0, to=1.0, resolution=0.1, tickinterval=0.2)
                    vol_scale.set(music_vol)
                    
                    vol_scale.grid(column=0, row=6)
                                        

                dark_mode()
                root.mainloop()
        except:
            cc()
            settings_menu()


    def ingame_menu(replay_game):
        print()
        print("Would you like to:")
        print(Fore.GREEN + "1: Play Again")
        print(Fore.BLUE + "2: Return to Menu")
        print(Fore.RED + "3: Quit the Program")
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
        elif "q" in ask_menu:
            goodbye()




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
        rolla = Fore.GREEN + "rock"
        rollb = Fore.BLUE + "paper"
        rollc = Fore.RED + "scissors"


        # options
        skip_rig_ask = 0        # disables rigging if this is enabled
        enable_asteroid = 1
        cls_after_turn = 0      # clears the terminal after each turn
        match_point = 3


        # storage
        player_score = 0
        comp_score = 0
        enable_rig = 0
        enable_super_rig = 0          
        player_history = []     
        comp_history = []


        print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon, Carter, and R-Bay | " + version + " | November 2021")
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
            # added this feature just to practice. in reality its useless and a waste of time
            # enable_rig = computer leans towards rock
            # enable_super_rig = computer always wins
        
            if skip_rig_ask == True:
                if enable_debug_flags_main == 1: print(Fore.YELLOW + "                          skip_rig_ask = " + str(skip_rig_ask))
            else:
                nonlocal enable_rig   # took me 20 minutes to figure out where this needed to go haha
                nonlocal enable_super_rig
                
                ask_for_rig = input("Would you like to rig the game? y/n ")

                if ask_for_rig == "y":
                    ask_for_super_rig = input("Would you like to super rig the game? y/n ")
                    if ask_for_super_rig == "menu":
                        ingame_menu(rps)

                    if "y" in ask_for_super_rig:
                        enable_super_rig = True
                        print("Game is rigged: rig = " + str(enable_rig) + " super rig = " + str(enable_super_rig))
                        Operation_Asteroid2()
                    else: 
                        enable_rig = True
                        print("Game is rigged: rig = " + str(enable_rig) + " super rig = " + str(enable_super_rig))
                        Operation_Asteroid2()
                elif "menu" in ask_for_rig:
                    ingame_menu(rps)


        def game():
            while True:
                print()
                print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                # had issues with scopes earlier
                if enable_debug_flags_main == 1: print(Fore.YELLOW + "Game is rigged in def game(): " + str(enable_rig))
                if enable_debug_flags_main == 1: print(Fore.YELLOW + "Game is super rigged in def game(): " + str(enable_super_rig))


                class player_entry:
                    # User inputs their play here
                    print("Enter " + rolla + ", " + rollb + ", " + Fore.RESET + "or " + rollc)

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
                        if enable_debug_flags_main == 1: print(Fore.YELLOW + "                      rng rigged")

                    elif enable_super_rig == True:
                        if player_input == "rock":
                            comp_choice = "paper"

                        elif player_input == "paper":
                            comp_choice = "scissors"
                        
                        elif player_input == "scissors":
                            comp_choice = "rock"
                        if enable_debug_flags_main == 1: print(Fore.YELLOW + "                      rng super rigged")

                    else:
                        p_comp_play = ["rock", "paper", "scissors"]
                        comp_choice = random.choice(p_comp_play)
                        if enable_debug_flags_main == 1: print(Fore.YELLOW + "                      rng normal")


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
                        print(Fore.RED + "Not a valid answer dummy!")
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
                    if enable_debug_flags_main == 1: print(Fore.YELLOW + "                      def normal_logic")
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
                        print(Fore.YELLOW + "It's a draw!")
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
                        global e_egg
                        e_egg += 1
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
                        global e_egg
                        e_egg += 1
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


    def hangman():
        print("Hangman by Brandon, Carter, and R-Bay")
        print("There are also phrases, not just words!")
        print()
        words = ["apple", "computer", "nature", "forest", "music", "china",
        "eat the rich", "sadness", "happy", "puppies", "cookie", "python", "keyboard",
        "holiday", "chicken", "display", "jeff bezos", "tax fraud", "engine", "science"
        "piano", "software", "technology", "color", "ignorant", "american"] 
        # "Those last two words have zero correlation" -An American, 2021

        chosen_word = random.choice(words)          # random word list

        guesses = []
        wrong_guesses = []
        guesses_left = 6    # if this hits 0 the game ends and you loose

        def win():
                print("Nice" + Fore.RED + " +100 social credit score")
                print(Fore.GREEN + "You win! The word was " + chosen_word)
                ingame_menu(hangman)

        while guesses_left > 0:
            output = ""
            if enable_debug_flags_main == 1: print(Fore.YELLOW + "chosen word is: " + chosen_word)

            print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for letter in chosen_word:
                if letter in guesses:
                    output = output + letter
                else:
                    output = output + "_"

            if output == chosen_word:
                break

            print("Word: ", output)
            print(guesses_left, "guesses left")
            guess = input("Enter lowercase letter, complete word, or phrase: ")
            if "menu" in guess:
                ingame_menu(hangman)

            if guess == chosen_word:
                global e_egg
                e_egg += 1
                win()

            else:
                if guess in guesses or guess in wrong_guesses:
                    cc()
                    print(Fore.RED + "Already entered, try again")
                elif guess in chosen_word:
                    cc()
                    print(Fore.GREEN + "Correct guess")
                    guesses.append(guess)
                else:
                    cc()
                    print(Fore.RED + "Incorrect guess")
                    guesses_left = guesses_left - 1     # revolutionary tech
                    wrong_guesses.append(guess)
                print()


        if guesses_left:
            win()
            e_egg += 1
            ingame_menu(hangman)
        else:
            print(Fore.RED + "You lost :(  the word was " + chosen_word)
            ingame_menu(hangman)


    def reaction_time_test():
        print("Reaction Time Test by Brandon, R-Bay, and Carter")
        print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        try:
            while True:
                print() # I hate everything about this. I know it looks bad
                print("This will do 5 runs and average them")
                print("You will hit enter when you see the alert")
                print("The time between the runs will vary")
                print("Python isn't that fast, so don't trust the results too much")

                ready = input("Press enter when you are ready ")
                print("test starting...")
                if "menu" in ready:
                    ingame_menu(reaction_time_test)
                time.sleep(1)
                cc()    # clears the gibberish from above

                
                time_start = 0
                time_stop = 0
                times = []
                alert = (Fore.RED + Back.WHITE + "⠀⠀⠀⠀⠀HIT ENTER⠀⠀⠀⠀⠀" + Fore.RESET + Back.RESET)
                if linux_mode == True: print("You can cheat now lol")
                for i in range(5):  # num = how many times to test
                    varied_delay = random.randint(1, 5)
                    time.sleep(varied_delay)

                    if linux_mode == False:
                        import msvcrt           # msvcrt is Windows only. IDK what to do for others
                        while msvcrt.kbhit():   # clears the input buffer so you can't cheat
                            msvcrt.getch()      # Only works on Windows
                    
                    # the test
                    t_start = perf_counter()
                    input(alert)
                    t_stop = perf_counter()
                    cc()
                    time_start = t_start
                    time_stop = t_stop

                    pre_round = time_stop - time_start
                    post_round = round(pre_round, 3)    # We don't need 290384209 million point precision

                    # turns seconds into ms (if more than 1 second, things get screwy and im too stupid to fix)
                    second_with_ms = str(post_round)
                    result_ms = second_with_ms.replace("0.", "")
                    print(result_ms + "ms")
                    times.append(result_ms)     # all of this is so bad


                for i in range(0, len(times)):  # converts times list to int
                    times[i] = int(times[i])
                
                avg = mean(times)
                cc()
                print("Your average reaction time is " + str(avg) + "ms")
                print("All of your times were: ", end="")
                print(*times, sep = "ms, ", end="")
                print("ms")     # adds ms to the last number. the line above only adds ms between nums, not after

                if avg <= 400:  # Good luck!
                    global e_egg
                    e_egg += 1
                if avg <= 200:
                    print("This time is literally impossible. (without cheating)")
                ingame_menu(reaction_time_test)
        except:
            print(Fore.RED + "reaction_time_test error")
            main_menu()


    def dice():
        # ASCII art for dice found on the Google machine
        global e_egg
        e_egg += 1

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


    def nft():
        # not really an arcade game, this is just us taking shots at millennials 
        capture_key = "s"
        save_name = "ctrl+c.png"

        cc()
        cd()

        def message():
            print(Fore.LIGHTGREEN_EX + "Free image finder by R-Bay, Carter, and Brandon")
            print()
            print("This will get you a free image, for FREE!")
            print("It is going to open an NFT website")
            print("Once it loads and NFTs are visible, hit " + capture_key)
            print("Step 4: Profit.")
            print("???")
            print()
        message()


        ready = input(Fore.RED + "Hit enter to continue " + Fore.RESET)
        if "menu" in ready:
            ingame_menu(nft)


        webbrowser.open("https://opensea.io/assets", autoraise=True) # shows NFTs
        print("Waiting for keypress (" +  Fore.YELLOW + capture_key + ")")


        def screenshot():
            image = ImageGrab.grab(bbox=())
            image.save(save_name)    # just copies the NFTs lol

            image = PIL.Image.open(save_name)
            image.show()             # shows NFTs to you for FREE! You now own an image for FREE!


        def end():
            os.system("cls" if os.name == "nt" else "clear")
            print("Congrats! You now own pixels that you didn't have to pay for!")
            print("Image saved in: " + os.getcwd())


        while True:     # thanks google
            try:        # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed(capture_key):  
                    screenshot()
                    end()
                    break 
            except:
                break   # if user pressed a key other than the given key the loop will break
 
        ingame_menu(nft)


    def inator():
        # You need to have watched Phineas and Ferb to understand this
        # Pretty much everyone in my generation will understand and appreciate it
        # If you don't know what I'm talking about, here is this: https://bit.ly/3ldUkDa
        # The best inator in my opinion: https://www.youtube.com/watch?v=n4TNdWxMX1Q
        global inatorify
        global e_egg
        e_egg += 1

        print("The Inator-Inator!")
        print()
        
        inatorify = input("What would you like to inatorify? ")

        rand_msg = random.randint(0,5)

        if "menu" in inatorify:
            ingame_menu(inator)

        if rand_msg == 0:
            print("Perry, I present to you the...")
            time.sleep(1)
            print(inatorify.upper() + "-INATOR!!!")

        elif rand_msg == 1:
            print("This is the " + inatorify + "-inator!!!")

        elif rand_msg == 2:
            print("BEHOLD! THE " + inatorify.upper() + "-INATOR")

        elif rand_msg == 3:
            print("Perry the Platypus, this is my " + inatorify + "-inator!")

        
        """ 
        Future dohickey.  audio inatorificator-inator
        add gtts to bat file
        
        pygame.mixer.music.load("behold.mp3")
        pygame.mixer.music.play()
        time.sleep(1)

        tts = gtts.gTTS(inatorify)
        tts.save("inatorify.mp3")
        pygame.mixer.music.load("inatorify.mp3")
        pygame.mixer.music.play()

        time.sleep(1.5) # Find a way to just wait until previous sound is done. hard coding it is bad
        pygame.mixer.music.load("inator.mp3")
        pygame.mixer.music.play()
        """
        

        ingame_menu(inator)


    def ttt():
        try:
            """
            Full disclosure, we borrowed some code from 
            the internet, changed it to fit our needs and
            cleaned up the messy bits

            add version of the board that changes it so
            it line up with a numpad
            """


            global e_egg
            e_egg += 1


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
                        print(Fore.YELLOW + "Game Over")                
                        print(Fore.GREEN + turn + " won!")
                    else:   
                        print()
                        print(Fore.YELLOW + "Game Over")
                        print(Fore.GREEN + "It's a Tie!")


                for i in range(10):
                    display_board(board_places)
                    print(Fore.YELLOW + "It's your turn, " + turn + ". Move to which place? ")

                    move = input()    
                    if "menu" in move:
                        ingame_menu(ttt)    

                    if board_places[move] == " ":
                        board_places[move] = turn
                        count += 1
                        cc()
                    else:
                        cc()
                        print(Fore.RED + "Dummy, that spot is filled. Choose another place.")
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
            print(Fore.RED + "TTT Error. Hit an invalid key.")  # chad level fix for when you don't enter a valid key
            main_menu()




    def game_credits():
        print("Thanks for playing!")
        time.sleep(1)
        print("Arcade made by:")
        time.sleep(1)
        print()

        tprint("Brandon", "sub-zero")
        time.sleep(0.5)
        print("༼ つ ♥_♥ ༽つ")
        time.sleep(1.2)

        print()
        print()
        tprint("Carter", "smpoison")
        time.sleep(0.5)
        print("| (• ◡•)| (❍ᴥ❍ʋ)")
        time.sleep(1.2)

        print()
        print()
        tprint("R-bay")
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
        global enable_music
        global rickroll
        global enable_debug_flags_main
        print(Fore.LIGHTGREEN_EX + "Settings options are:")
        print("1: Toggle Music")
        print("2: Toggle debugging mode")
        print("3: View Credits")
        print("4: Notes about this program")
        print("5: Music but in a bad gooey (very broken)")
        print()
        print("m: Go back to main menu")
        print("q: Quit Game")
        print()
        if global_cut_music == True:
            print("Music toggle disabled for compatibility")

        which_setting = input("Which setting would you like to use? ")
        if "1" in which_setting:
            if not enable_music:
                enable_music = 1
                cc()
                if global_cut_music == False: print("Music On")
                music_play()
                settings_menu()
            else:
                cc()
                enable_music = 0
                if global_cut_music == False: print("Music Off")
                pygame.mixer.music.fadeout(750)
                rickroll = 0
                settings_menu()
        elif "2" in which_setting:
            if not enable_debug_flags_main:
                enable_debug_flags_main = 1
                cc()
                print(Fore.YELLOW + "Global Debugging Mode Enabled")
                settings_menu()
            else:
                enable_debug_flags_main = 0
                cc()
                print("Global Debugging Mode Disabled")
                settings_menu()
        elif "3" in which_setting:
            cc()
            game_credits()
        elif "4" in which_setting:
            cc()
            print("Opened Doc in browser")
            webbrowser.open("https://docs.google.com/document/d/1z0a9XA7nS2HSgqRiNl7OAoM2NchoCG0EkOCNeLv4DfM/edit?usp=sharing", autoraise=False)
            settings_menu()
        elif "5" in which_setting:
            cc()
            gui_music()
        elif "s" in which_setting:
            cc()
            main_menu()
        elif "m" in which_setting:
            cc()
            main_menu()
        elif "q" in which_setting:
           goodbye()
        else:
            cc()
            print()
            print(Fore.RED + "Invalid input")
            settings_menu()


    def pls_ignore():
        if linux_mode == True:
            tprint("ATTENTION,   I   AM   USING   LINUX")
            time.sleep(3)
            # It's meant to show that linux mode is enabled.
            # not because its a stereotype that linux users
            # must announce that they are using linux or anything        
    pls_ignore()


    def goodbye():
        bye_delay = 0.07

        if global_cut_music == False:
            for x in range(1):
                pygame.mixer.music.load("GBsound.mp3")
                pygame.mixer.music.play()
        # help
        sys.stdout.write(Fore.RED + "G")
        time.sleep(bye_delay)
        sys.stdout.write(Fore.YELLOW + "o")
        time.sleep(bye_delay)
        sys.stdout.write(Fore.GREEN + "o")
        time.sleep(bye_delay)
        sys.stdout.write(Fore.BLUE + "d")
        time.sleep(bye_delay)
        sys.stdout.write(Fore.MAGENTA + "b")
        time.sleep(bye_delay)
        sys.stdout.write(Fore.RED + "y")
        time.sleep(bye_delay)
        sys.stdout.write(Fore.YELLOW + "e")
        time.sleep(1.5) # waits for sound to be done
        sys.exit()


    def new_mm_gui():
        try:
            surface = pygame.display.set_mode((600, 800), pygame.RESIZABLE)
            pygame.display.set_caption("Arcade " + version)

            menu = pygame_menu.Menu(
                height=500,
                theme=pygame_menu.themes.THEME_DARK,
                title="Main Menu",
                width=600
            )

            def close():    # this doesnt work o irngpiw tnpigvbu2 4np 4pq
                menu.disable()
    
            def about():
                cc()
                print("Opened Doc in browser")
                webbrowser.open("https://docs.google.com/document/d/1z0a9XA7nS2HSgqRiNl7OAoM2NchoCG0EkOCNeLv4DfM/edit?usp=sharing", autoraise=True)
    
            # window resize stuff
            def on_resize():
                window_size = surface.get_size()
                # border size multipliers
                new_w, new_h = 0.9 * window_size[0], 0.92 * window_size[1]
                menu.resize(new_w, new_h)
                print(f"New menu size: {menu.get_size()}")

            # options and buttons
            menu.add.button("Rock Paper Scissors", rps)
            menu.add.button("Bottle Flip", bottle_flip)
            menu.add.button("Hangman", hangman)
            menu.add.button("Reaction Time Test", reaction_time_test)
            menu.add.button("Dice", dice)
            menu.add.button("Free Images", nft)
            menu.add.button("Inator Inator!", inator)
            menu.add.button("",)    # creates a space between games and options
            menu.add.button("Settings", settings_menu)
            menu.add.button("Notes about this program", about)
            menu.add.button("Return to CLI Menu", close)
            menu.add.button("Quit", pygame_menu.events.EXIT)

            menu.enable()
            on_resize()  

            # more window resize stuff
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                    if event.type == pygame.VIDEORESIZE:
                        surface = pygame.display.set_mode((event.w, event.h),
                        pygame.RESIZABLE)
                        on_resize()

                    # border color
                    surface.fill((100, 20, 240))
                    menu.update(events)
                    menu.draw(surface)
                    pygame.display.flip()
            
        except:
            print(traceback.format_exc())
            print(Fore.RED + "New Main Menu GUI Error")

 
    def old_mm_gui():   # shouldn't even be a thing, tkinter is so old and broken...
        # I'm keeping the old one in for reasons
        try:    # throws errors under the rug so the rest of the code can "continue"
            root_mg = Tk()
            while True:
                # options
                buttonFont = font.Font(family="Comic Sans MS", size=15) # button text properties
                set_cursor = "heart"    # trek
                btn_color = "green"
                btn_background = "gray60"
                background_color = "gray15"

                # window setup
                root_mg.title("peak ui design")
                root_mg.geometry("400x500")
                root_mg["bg"] = "gray15"   # keep this idk what it does


                def return_cli_menu():  # doesnt even work
                    cc()
                    root_mg.destroy
                    main_menu()

                def goodbye_gui():  # also doesnt even work
                    root_mg.destroy
                    goodbye()
                    
                label_font = font.Font(family="Comic Sans MS", size=20)
                label1 = tk.Label(master=root_mg, text="Pick an Option:", bg=background_color,font=label_font,fg = "green2")
                label1.grid(column=0, row=0)

                def gui_main_menu():  # regular buttons. will go to light_mode if light mode is enabled in the options menu
                    # FB
                    btn_tog = Button(root_mg, text = "Return to CLI Menu", # this is kind of redundant because of the slider but ehhhhh
                        fg = "blue4", command=return_cli_menu, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=1)
                    # RPS
                    btn_tog = Button(root_mg, text = "Rock Paper Scissors", # this is kind of redundant because of the slider but ehhhhh
                        fg = "green", command=rps, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=2)
                    # BF
                    btn_tog = Button(root_mg, text = "Bottle Flip", # this is kind of redundant because of the slider but ehhhhh
                        fg = "green", command=bottle_flip, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=3)
                    # Hangman
                    btn_tog = Button(root_mg, text = "Hangman", # this is kind of redundant because of the slider but ehhhhh
                        fg = "green", command=hangman, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=4)
                    # RTT
                    btn_tog = Button(root_mg, text = "Reaction Time Test", # this is kind of redundant because of the slider but ehhhhh
                        fg = "green", command=reaction_time_test, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=5)
                    # Dice
                    btn_tog = Button(root_mg, text = "Dice", # this is kind of redundant because of the slider but ehhhhh
                        fg = "green", command=dice, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=6)
                    # NFTs
                    btn_tog = Button(root_mg, text = "Free images", # this is kind of redundant because of the slider but ehhhhh
                        fg = "green", command=nft, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=7)
                    # Settings
                    btn_tog = Button(root_mg, text = "Settings", # this is kind of redundant because of the slider but ehhhhh
                        fg = "blue4", command=settings_menu, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=8)
                    # Quit
                    btn_tog = Button(root_mg, text = "Quit", # this is kind of redundant because of the slider but ehhhhh
                        fg = "red4", command=goodbye_gui, bg=btn_background, height=1, width=15, font=buttonFont, cursor=set_cursor)
                    btn_tog.grid(column=0, row=15)
                    root_mg.destroy
                

                # old menu code from a different project. thats why its janky and doesnt match stuff. I don't wanna delete it for reasons
                def how_to_play():
                    how_toPlay_msgbox = messagebox.askquestion("RPS Help", "Are you serious?!?!")
                    if how_toPlay_msgbox == "yes":
                        sys.exit()
                    elif how_toPlay_msgbox == "no":
                        print("Good.")

                def flashbang():
                    print("hello")
                    new= Toplevel()
                    new.geometry("7680x4320") # 8K because why not. but by doing this the whole screen is flled with white
                    new.title("I did warn you")
                    # Create a Label in New window
                    Label(new, text="Get flashbanged lol", font=("Tahoma 17 bold")).pack(pady=30)

                def about():
                    cc()
                    print("Opened Doc in browser")
                    webbrowser.open("https://docs.google.com/document/d/1z0a9XA7nS2HSgqRiNl7OAoM2NchoCG0EkOCNeLv4DfM/edit?usp=sharing", autoraise=True)
        

                # top menu bar
                menu = Menu(root_mg)
                root_mg.config(menu=menu)

                optionmenu = Menu(menu)
                optionmenu = Menu(menu, tearoff = 0)
                menu.add_cascade(label="Options", menu=optionmenu)
                optionmenu.add_command(label="Light Mode (Seriously don't click this)", command=flashbang)
                #optionmenu.add_command(label="Other Light Mode", command=gui_main_menu)

                helpmenu = Menu(menu)
                helpmenu = Menu(menu, tearoff = 0)
                menu.add_cascade(label="Help", menu=helpmenu)
                helpmenu.add_command(label="How to Play", command=how_to_play)
                helpmenu.add_command(label="About", command=about)
    
                gui_main_menu()
                root_mg.mainloop()
        except:
            cc()
            print(Fore.RED + "Old Main Menu GUI Error")
            main_menu()


    def main_menu_gui():    
        if enable_debug_flags_main == False:
            cc()
            print("300 GW time")
            time.sleep(0.8)
            print("Reactor #4 style")
            time.sleep(0.8)
            print("(errors incoming)")
            time.sleep(0.8)
            print("No longer supported, not being updated to match CLI")
            print()

            oldnew = input("Do you want the old GUI or the new one? o/n ")
            # I'm keeping the old one in for reasons
            if "n" in oldnew:
                new_mm_gui()

            print("New Menu GUI opened in new window")
        else:
            cc()
            oldnew = input("Do you want the old GUI or the new one? o/n ")
            # I'm keeping the old one in for reasons
            if "n" in oldnew:
                new_mm_gui()
            
            print("Menu GUI opened in new window")
        old_mm_gui()
    
        
    def main_menu():    # also contains easter egg code
        print("Arcade for IFT101 by Carter, R-Bay, and Brandon")
        print("December 2021")
        print(version)
        global rickroll
        global enable_music
        if enable_debug_flags_main == True:
            debug_flags()
        print()
        if enable_music == True and global_cut_music == False: # this prevents errors caused by displaying the song
                if rickroll == True:
                    print("🎵 You know the rules, and so do I 🎵")
                    print("Enter r to change to normal music")    # why would you want to lol
                else:
                    size = len(rand_song)
                    mod_string = rand_song[:size - 4] # removes file extension
                    print("Now playing: " + Fore.LIGHTMAGENTA_EX + mod_string)


        print('Type "menu" during a game to show the menu')
        print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print(Fore.LIGHTGREEN_EX + "Game options are:")
        print("1: Rock Paper scissors")
        print("2: Bottle Flip")
        print("3: Hangman")
        print("4: Reaction Time Test")  # Only works on Windows. Its complicated why. ok not really
        print("5: Dice")
        print("6: Free images")
        print("7: Inator Inator!")   # doof
        print("8: Tic Tac Toe (You need a friend. Too bad you dont have any.)")
        print()
        print("s: Settings")
        print("n: Notes about this program")
        print("x: Throw more errors than Reactor #4")  # Thank you to my friend Joseph for this FLAWLESS message
        print("q: Quit Game")

        which_game = input("What would you like to do? ")

        if "1" in which_game:
            cc()
            rps()
        elif "2" in which_game:
            cc()
            bottle_flip()
        elif "3" in which_game:
            cc()
            hangman()
        elif "4" in which_game:
            cc()
            reaction_time_test()
        elif "5" in which_game:
            cc()
            dice()
        elif "6" in which_game:
            cc()
            nft()
        elif "7" in which_game:
            cc()
            inator()
        elif "8" in which_game:
            cc()
            ttt()
        elif "d" in which_game:
                enable_music = 0
                if global_cut_music == False:
                    pygame.mixer.music.fadeout(750)
                    rickroll = 0
                    cc()
                    print("Music Off")
                    main_menu()
        elif "s" in which_game: 
            cc()
            settings_menu()
        elif which_game == ":D":
            if enable_debug_flags_main == False:
                if e_egg >= game_count:  # yes you could play a game multiple times to get to game_count, but this is simple
                    cc()                    
                    webbrowser.open("https://imgur.com/a/mYYsmRu", autoraise=False) # why
                    main_menu() # autoraise option does nothing. Windows moment
                else:
                    cc()
                    print(Fore.RED + "You need to win/play all the games first!")
                    main_menu()
            else: # bypasses the play all games requirement to open easter egg
                cc()
                webbrowser.open("https://imgur.com/a/mYYsmRu", autoraise=False) # why
                main_menu()
        elif "q" in which_game:
            goodbye()
        elif "r" in which_game and rickroll == True:                                
            rickroll = 0         
            music_logic()
            cc()
            main_menu()
        elif "x" in which_game:
            main_menu_gui()
            #new_mm_gui()
        elif "n" in which_game:
            cc()
            print("Opened Doc in browser")
            webbrowser.open("https://docs.google.com/document/d/1z0a9XA7nS2HSgqRiNl7OAoM2NchoCG0EkOCNeLv4DfM/edit?usp=sharing", autoraise=False)
            main_menu()
        elif "a" in which_game:  # shortcut to current work
            gui_music()     
        else:
            cc()
            print(Fore.RED + "Invalid input")
            main_menu()
    main_menu()


except Exception:
    print(traceback.format_exc())
    print(Fore.RED + "Global Error")
    input("Press enter to exit")
