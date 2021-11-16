def main_notes():   # to collapse the text below in the IDE
    """
    Arcade for IFT101 final project    
    November 2021                                      
    Written by Brandon, Carter, and R-Bay

    This document has some important things to note
    https://docs.google.com/document/d/1z0a9XA7nS2HSgqRiNl7OAoM2NchoCG0EkOCNeLv4DfM/edit?usp=sharing

    linux_mode disables a few things so this can run on there                  

    We are aware that this is a royal mess.
    In the future we hope to do better.

    Reaction time and maybe the music requires to be ran on Windows

    This game requires a few libraries, they can be found below.
    A batch file is included if you dont have them or are too
    lazy to to copy and pase the stuff below

    """
# SPAGHETTI CODE STATUS: ITALIAN
# HOURS WASTED ON DEBUGGING AND USELESS FEATURES SO FAR: 369


from threading import current_thread
import traceback    # prevents the terminal from closing if
try:                # there is an error so you can read it

    import webbrowser, random, pygame, time, sys, os
    from colorama import init                   # pip install colorama
    init()
    from colorama import Fore, Back, Style
    init(autoreset=True)
    pygame.init()                               # pip install pygame
    pygame.mixer.init()
    from time import perf_counter
    from statistics import mean
    from art import *                           # pip install art


    # options

    enable_music = 1
    rickroll = 1
    global_cut_music = 0            # see message below
    game_count = 5                  # used for some stuff (5 currently)
    enable_debug_flags_main = 0     # its sad that this is even a thing
    linux_mode = 0                  # only tested on Ubuntu, it works there
    music_vol = 0.7

    '''
    Enable this option if you don't have the music files, or are getting
    errors related to it. This option basically disables anything 
    relating to music so you can run the game without it.

    However the music does "improve" the experience
    The music is in the same zip file as this .py file
    '''

    # storage
    e_egg = 0


    def cc():   # shortened this long command to cc()
        os.system("cls" if os.name == "nt" else "clear")
        # however, it is required in some places
    cc()


    def cd():   # changes directory to where the .py file is
        abspath = os.path.abspath(sys.argv[0])
        dname = os.path.dirname(abspath)
        os.chdir(dname)


    def debug_flags():
        print(Fore.YELLOW + "          Message from def debug_flags")    # we had spaghetti code okay
        print(Fore.YELLOW + "          Linux compatibility Mode: " + str(linux_mode))
        print(Fore.YELLOW + "          Debugging mode: " + str(enable_debug_flags_main))
        print(Fore.YELLOW + "          e_egg progress: " + str(e_egg))
        print()
        print(Fore.YELLOW + "          Enable music: " + str(enable_music))
        print(Fore.YELLOW + "          Music nuke: " + str(global_cut_music))
        print(Fore.YELLOW + "          Rick Roll: " + str(rickroll))
        print(Fore.YELLOW + "          CWD: " + os.getcwd())


    def music_play():
        cd()
        global current_song
        global rand_song
        songs = ["Climate Nuclear.mp3", "The Egg.mp3", "Nuclear Death Toll.mp3"]
        rand_song = random.choice(songs)
        pygame.mixer.music.set_volume(music_vol)

        if enable_music == True:
            if global_cut_music == False:     # its in music_logic, but still needed. sometimes logic is skipped
                for x in range(1):
                    pygame.mixer.music.load(rand_song)   # egg
                    pygame.mixer.music.play(fade_ms = 4000)
                    pygame.event.wait()


    def music_logic():
        if global_cut_music == False and enable_music == True:       
                if rickroll == False: # so    many    ifs. I don't even understand my own code anymore
                    music_play()
                elif rickroll == True:
                    pygame.mixer.music.set_volume(music_vol)
                    cd()
                    pygame.mixer.music.load("wehadto.mp3")
                    pygame.mixer.music.play()
                    pygame.event.wait()
                    # Never gonna let you down     
    music_logic()


    def ingame_menu(replay_game):
        print()
        print("Would you like to:")
        print(Fore.GREEN + "a1: Play Again")
        print(Fore.BLUE + "2: Return to Menu")
        print(Fore.RED + "3: Quit the Program")
        ask_menu = input()
        if "1" in ask_menu:
            cc()
            replay_game()
            print("                     playing again")

        elif "2" in ask_menu:
            cc()
            main_menu()
        elif "menu" in ask_menu:
            cc()
            main_menu()
        else:
            quit = input("Are you sure? y/n ")
            if quit == "y":
                goodbye()
            else:
                ingame_menu(replay_game)


    def rps():
        """
        RPS By Brandon. Carter, and R-Bay
        V1.6-IFT
        November 2021

        This version has changes over the normal V1.6 because
        all of this version of the game has to go in a function
        and interface with an external menu.
        This screws some things up.
        """


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
        enable_rig = 0          # this is redundant since you can just read the input,
        player_history = []     # but this way you can do certain things with it
        comp_history = []


        print(Fore.BLUE + Back.YELLOW + "Rock Paper Scissors by Brandon, Carter, and R-Bay | V1.6-IFT101 | November 2021")
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
                    print('//launch.rockets [count=all arg- s- lightspeed] galactic-payload[asteroid 3(goal=spread)]')   #asteroid 3
                    time.sleep(0.1)
                    print("Operation Asteroid2 Complete.")               # "I mean, can you really disagree?" -Thanos, probably
                    time.sleep(2)
                    cc()    # You saw nothing. You saw nothing. You saw nothing. You saw nothing. You s
                    # teaching sand to think was a mistake


        class match_fixing:
            # added this feature just to practice. in reality its useless and a waste of time
            if skip_rig_ask == True:
                if enable_debug_flags_main == 1: print(Fore.YELLOW + "                          skip_rig_ask = " + str(skip_rig_ask))
            else:
                nonlocal enable_rig   # took me 20 minutes to figure out where this needed to go haha :sad:
                ask_for_rig = input("would you like to rig the game? y/n ")
                if ask_for_rig == "y":
                    enable_rig = True
                    print("Game is rigged: " + str(enable_rig))
                    Operation_Asteroid2()
                elif ask_for_rig == "menu":
                    ingame_menu(rps)
                else:
                    enable_rig = False


        def game():
            while True:
                print()
                print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                if enable_debug_flags_main == 1: print(Fore.YELLOW + "Game is rigged in def game(): " + str(enable_rig))
                # had issues with scopes earlier

                class player_entry:
                    # User inputs their play here
                    print("Enter " + rolla + ", " + rollb + ", " + Fore.RESET + "or " + rollc)

                class rng:
                    if enable_rig == False:
                        global comp_choice
                        p_comp_play = ["rock", "paper", "scissors"]
                        comp_choice = random.choice(p_comp_play)
                        if enable_debug_flags_main == 1: print("                      rng normal")

                    elif enable_rig == True:
                        p_comp_play_rigged = ["rock", "rock", "rock", "paper", "scissors"]
                        comp_choice = random.choice(p_comp_play_rigged)
                        if enable_debug_flags_main == 1: print("                      rng rigged")


                    if enable_debug_flags_main == True:
                        print("                      comp_choice = " + comp_choice)
                        if comp_choice == "rock": print("                      Roll Paper")
                        if comp_choice == "paper": print("                      Roll Scissors")
                        if comp_choice == "scissors": print("                      Roll Rock")


                    global player_input
                    player_input = input()
                    print()
                    if "menu" in player_input:
                        ingame_menu(rps)

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
                    if enable_debug_flags_main == 1: print("                      def main_logic")
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
                #if "menu" in cls_after_turn:    # this throws errors, not sure why
                    #ingame_menu(rps)
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
                    flip_reg_outcome = (random.randint(0,4)) # 20% chance to land the flip

                    for i in range(3):   # builds suspense
                        print(".", end =" ")
                        time.sleep(delay)


                    if flip_reg_outcome == 0:
                        time.sleep(suspense_delay)
                        print()
                        print("||")
                        print("You win")
                        global e_egg
                        e_egg += 1
                        ingame_menu(bottle_flip)
                    else:
                        time.sleep(suspense_delay)
                        print("==")
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
        "piano", "software"]

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
                    print(Fore.RED + "Already entered, try again")
                elif guess in chosen_word:
                    print(Fore.GREEN + "Correct guess")
                    guesses.append(guess)
                else:
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
                varied_delay = random.randint(1,5)
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
        print()
        print("The faces don't display properly in the Windows terminal :(")
        print("Maybe use an IDE or a different thingamabob")

        time.sleep(2)
        settings_menu()


    def settings_menu():
        global enable_music
        global rickroll
        global enable_debug_flags_main
        print("Settings options are:")
        print("1: Toggle Music")
        print("2: Toggle debugging mode")
        print("3: View Credits")
        print("4. Open Document explaining this game")
        print()
        print("5: Go back to main menu")
        print("6: Quit Game")
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
        elif "s" in which_setting:
            cc()
            main_menu()
        elif "5" in which_setting:
            cc()
            main_menu()
        elif "6" in which_setting:
            goodbye()
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
            # It's meant to show that linux mode is on.
            # not because its a stereotype that linux users
            # must announce that they are using linux          
    pls_ignore()


    def goodbye():
        bye_delay = 0.07

        if global_cut_music == False:
            for x in range(1):
                cd()
                pygame.mixer.music.load("GBsound.mp3")
                pygame.mixer.music.play()

        # help
        sys.stdout.write(Fore.RED +"G")
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


    def main_menu():    # also contains easter egg code
        print("Arcade for IFT101 by Carter, R-Bay, and Brandon")
        print("November 2021")
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
        print("Game options are:")
        print("1: Rock Paper scissors")
        print("2: Bottle Flip")
        print("3: Hangman")
        print("4: Reaction Time Test")  # Only works on Windows. Its complicated why. ok not really
        print("5. Dice")
        print()
        print("6: Settings")
        print("7: Quit Game")

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
            settings_menu()
        elif "s" in which_game: # you cant have <or> in one thing when next to <in>
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
        elif "7" in which_game:
            goodbye()
        elif "q" in which_game:
            goodbye()
        elif "r" in which_game and rickroll == True:
            cc()
            rickroll = 0         
            music_logic()
            main_menu()
        else:
            cc()
            print(Fore.RED + "Invalid input")
            main_menu()
    main_menu()


except Exception:
    print(traceback.format_exc())
    input("Press enter to exit")
