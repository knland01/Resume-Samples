""""" CASE CLOSED """
import random
import time
import pygame
import os


# KARIS LAND: CHOOSE YOUR OWN ADVENTURE
def roll_dice():
    return random.randint(1, 20)

def add_sound(file_name):
    pygame.init()
    wav_new_message = pygame.mixer.Sound(file_name)
    wav_new_message.play()
    while pygame.mixer.get_busy():  # continues running program while music plays
        pass
    pygame.quit()


def add_image(file_name, width, height, x, y, duration):
    window_size = (width, height)  # Size of window
    screen = pygame.display.set_mode(window_size, pygame.NOFRAME)
    pygame.display.set_mode(window_size)  # Creates graphic window
    image = pygame.image.load(file_name)
    screen.blit(image, (x, y))  # image position
    pygame.display.update()  # have to update the display for display changes to take place
    duration = duration  # Seconds that display will stay open
    start_time = time.time()
    while time.time() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    pygame.quit()


def clear_screen():
    input("[Press ENTER to Continue]")
    print('------------------------------------------------------------------------------------\n' * 5)
    '''    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('cls')
    else:'''

def check_inventory(plr_inv_ls, needed_item):
    for item in plr_inv_ls:
        if item == needed_item:
            return True
    return False

def valid_number(user_num):
    while True:
        try:
            number = int(input(user_num))
            if 1 <= number <= 6:
                return number
            else:
                print("Perhaps we were mislead about your detective skills. That is not even one of the options!")
        except ValueError:  # if string is entered
            print("Um... ok... That's not even a number. Let's try that again, DETECTIVE.")


def valid_number2(lower, upper):
    while True:
        try:
            number = int(input(f"ENTER A NUMBER BETWEEN {lower} and {upper}: "))
            print("NUMBER:", number)
            if lower <= number <= upper:
                return number
            else:
                print("Perhaps we were mislead about your detective skills. That is not even one of the options!")
        except ValueError:  # if string is entered
            print("Um... ok... That's not even a number. Let's try that again, DETECTIVE.")


def create_inventory(items):
    if not items:
        print("LIST OF ITEMS:\n1. Backpack\n2. Particle Analyzer\n3. Reading Glasses\n4. Gun\n"
              "5. Handheld Voice Recorder\n6. Money (5 ducans <-- intergalactically recognized currency)")
        print("[YOU CAN ONLY PICK FOUR]")
        items = [valid_number("FIRST ITEM [enter its number]: "),
                 valid_number("SECOND ITEM [enter its number]: "),
                 valid_number("THIRD ITEM [enter its number]: "),
                 valid_number("LAST ITEM [enter its number] ")]
        items.sort()
        print(items)
    else:
        print("The item numbers you selected were", items)
    while True:
        choice = input("Did you make the selections you wanted to (yes or no): ")
        choice = choice.lower()
        if choice == 'no':
            print("LIST OF ITEMS:\n1. Backpack\n2. Particle Analyzer\n3. Reading Glasses\n4. Gun\n"
                  "5. Handheld Voice Recorder\n6. Money (5 ducans <-- intergalactically recognized currency)")
            items = [valid_number("FIRST ITEM [enter its number]: "),
                     valid_number("SECOND ITEM [enter its number]: "),
                     valid_number("THIRD ITEM [enter its number]: "),
                     valid_number("LAST ITEM [enter its number] ")]
            items.sort()  # sorts item numbers in sequential order
            print("The items you selected were: ", items)
        elif choice == 'yes':
            items.sort()
            break
    return items


def update_inventory_item(new_item, removed_item, first_time=False):
    if not first_time:
        for index in item_nums:  # converts numbers to their 'string' counterparts
            if 0 <= index < len(inventory_list):
                plr_inv_ls.append(inventory_list[index])
        for item in plr_inv_ls:
            if item == money6:
                plr_inv_ls.append(inventory_list[7])
                break
    if new_item != '':
        plr_inv_ls.append(new_item)
    if removed_item in plr_inv_ls:
        plr_inv_ls.remove(removed_item)
    print("UPDATED INVENTORY LIST: ")
    for item in plr_inv_ls:
        print(f"    * {item}")


def change_inventory_list(new_item, removed_item):
    if new_item != '':
        plr_inv_ls.append(new_item)
    if removed_item in plr_inv_ls:
        plr_inv_ls.remove(removed_item)
    print("UPDATED INVENTORY LIST: ")
    for item in plr_inv_ls:
        print(f"    * {item}")


def spend_money():
    for i in range(len(plr_inv_ls)):
        if plr_inv_ls[i] == money6:
            plr_inv_ls[i + 1] = plr_inv_ls[i + 1] - 1
            if plr_inv_ls[i + 1] < 1:
                update_inventory_item(none, money6, first_time=True)
            break


def choice_add_clue():
    while True:
        pygame.init()
        wav_new_message = pygame.mixer.Sound('new_message.wav')
        wav_new_message.play()
        while pygame.mixer.get_busy():  # continues running program while music plays
            pass
        choice = input(" >>>>>> ADD THIS TO YOUR CLUE BOOK [yes or no]: ")
        choice = choice.lower()
        if choice == 'yes':
            write_journal_entry(player)
            break
        elif choice == 'no':
            break
        else:
            print("[TYPE yes or no]")



def write_journal_entry(f_player):
    print("---------------------------------------------")
    print("INSTRUCTIONS: Enter all suspects and clues here.")
    print("You can add as many clues as you like to a particular suspect.")
    print("Just be sure to type suspect name THE SAME every time.")
    clear_screen()
    print("__________________________________________")
    print(f"*** DETECTIVE {f_player}'s CLUE BOOK ***")
    print("__________________________________________\n")
    # journal_entry = dict()
    # journal_entry[f_alien_name] = []
    while True:
        f_alien_name = input("SUSPECT NAME (type done if finished): ")
        f_alien_name = f_alien_name.rstrip()
        if f_alien_name == "done":
            for suspect, clue in journal_entry.items():
                print("_____________________________________________________")
                print("SUSPECT:", suspect)
                print("CLUES:", clue)
                print("_____________________________________________________")
            break
        f_clue = input("ADD CLUE: ")
        if f_clue == "done":
            for suspect, clue in journal_entry.items():
                print("\n\n\n\n\n")
                print("_____________________________________________________")
                print("SUSPECT:", suspect)
                print("CLUES:", clue)
                print("_____________________________________________________")
            break
        if f_alien_name in journal_entry:
            journal_entry[f_alien_name].append(f_clue)
        else:
            journal_entry[f_alien_name] = [f_clue]
        '''for k, v in journal_entry.items():
            print("_____________________________________________________")
            print("SUSPECT:", k)
            print("CLUES:", v)
            print("_____________________________________________________")'''
    return journal_entry

# AMY SIEMER: SEQUENCE GAME
def generate_sequence(length):
    sequence = []
    for _ in range(length):
        sequence.append(random.randint(1, 9))
    return sequence

def get_user_input(length):
    user_input = []
    for _ in range(length):
        while True:
            try:
                num = int(input("Enter the numbers in the sequence: "))
                break
            except ValueError:
                print("Sorry, please enter a number.")
        user_input.append(num)
    return user_input

def play_game():
    print("Greetings! My name is Alien_2. I understand you are looking for help. "
          "I could be willing if you complete my Sequence Game!")
    clear_screen()
    add_image('alien_2.jpg', 440, 700, 0, 0, 3)
    time.sleep(3)

    sequence_length = 3
    sequence = generate_sequence(sequence_length)
    print("Memorize the sequence:", sequence)
    print('clear output box')
    time.sleep(7)

    print("Let's test your memory!")
    while True:
        user_sequence = get_user_input(sequence_length)

        if user_sequence == sequence:
            print("Congratulations! You remembered the sequence correctly.")
            if sequence_length == 3:
                print("Alien_1 is in debt to his planets bankers, not a good situation, they'll need the money fast.")
                choice_add_clue()
            if sequence_length == 5:
                print("Zender has reached out to Alien_3, they have been looking for a new moon.")
                choice_add_clue()
            if sequence_length == 7:
                print("Wait, but Alien_4 is also in contact with Zender.")
                choice_add_clue()
            if sequence_length == 8:
                print("Alien_2 has been working on shrink ray technology, "
                      "maybe to sell it? Could be worth a lot of money.")
                choice_add_clue()
            if sequence_length == 9:
                exit()
            sequence_length += 1
            sequence.append(random.randint(1, 9))
            print("Memorize the new sequence:", sequence)
            print("clear output box")
            time.sleep(5)
        else:
            print('Game over! The correct sequence was:', sequence)
            break

# MAX KURTS: BLACK JACK - ALIEN 3

def calculate_hand_value(hand):
    total_value = 0
    ace_count = 0

    for card in hand:
        if card in ['K', 'Q', 'J']:
            total_value += 10
        elif card == 'A':
            total_value += 11
            ace_count += 1
        else:
            total_value += int(card)

    while total_value > 21 and ace_count > 0:
        total_value -= 10
        ace_count -= 1

    return total_value

def deal_card():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return random.choice(cards)

def display_hands(player_hand, alien_hand):
    print("Player's Hand:", player_hand)
    print("ALIEN 3's Hand:", alien_hand[0], "<card hidden>")

def player_choice():
    choice = input("Do you want to hit or stand? (h/s): ").lower()
    return choice

def play_blackjack():
    clear_screen()
    add_image('alien_3.jpg', 520, 700, 0, 0, 3)
    print("ALIEN 3: You're playin' with the big rollers here, kid. Best three of five, \n"
          "huh? Be careful whatcha wish for.")
    player_wins = 0
    alien_wins = 0

    while player_wins < 3 and alien_wins < 3:
        player_hand = [deal_card(), deal_card()]
        alien_hand = [deal_card(), deal_card()]

        display_hands(player_hand, alien_hand)

        while True:
            choice = player_choice()

            if choice == 'h':
                player_hand.append(deal_card())
                display_hands(player_hand, alien_hand)

                if calculate_hand_value(player_hand) > 21:
                    print("Player busts! You lose.")
                    alien_wins += 1
                    break

            elif choice == 's':
                break

        while calculate_hand_value(alien_hand) < 17:
            alien_hand.append(deal_card())

        print("\nFinal Hands:")
        print("Player's Hand:", player_hand)
        print("ALIEN 3's Hand:", alien_hand)

        player_value = calculate_hand_value(player_hand)
        alien_value = calculate_hand_value(alien_hand)

        if player_value > 21:
            print("Player busts! You lose.")
            alien_wins += 1
        elif alien_value > 21:
            print("ALIEN 3 busts! You win.")
            player_wins += 1
        elif player_value == alien_value:
            print("It's a tie!")
        elif player_value > alien_value:
            print("You win!")
            player_wins += 1
        else:
            print("You lose.")
            alien_wins += 1

    clues = ["ALIEN 3: Alright, you're not too bad kid. I've been hearing some rumors \n"
             "connecting ALIEN 1 to an industrial grade shrink ray. No tellin' what \n"
             "they've got in mind for that.",
             "ALIEN 3: Fine. You win, I guess. Apparently ALIEN 2 is in negotiations \n"
             "with that chop shop gang. You ain't hear that from me. Got it?",
             "ALIEN 3: I don't believe it. But I am an alien of my word, so here ya go. \n"
             "I've got it from a good source that ALIEN 5 has been spotted at sit-downs with\n"
             " that chop shop gang. Just keep that between us though, kid."]

    if player_wins >= 3:
        print(random.choice(clues))
        choice_add_clue()
    else:
        print("ALIEN 3: I've got no time for amateurs like you. Get lost kid.")

# AMAR LJUBOVIC: NUMBER MATCHING - ALIEN 4
alien_clues = {
    1: "Alien 1 has connections to a celestial chop shop.",
    2: "Alien 1 has a buyer in the market for a moon.",
    3: "Alien 5 really doesn't like Earth."
}

race_tracks = {
    "Nordschleife": {
        "At The Pit wall your opponent hits the brakes a little too late and goes wide": {
            1: "brake early and overtake opponent on inside",
            2: "brake early and overtake opponent on outside"
        },
        "You are going 200mph on a long straight away called foxhole, you see a car on the"
        " right side of the track braking down and has its right blinker on,\nfor a second "
        "the car is in the middle of the track with its right blinker still on": {
            1: "go to the left of the car",
            2: "go to the right side of the car"
        },
        "long right-hander(your opponent is on the outside of the corner with colder tires than you)": {
            1: "go on the inside with full throttle",
            2: "Go on the outside of your opponent"
        }
    },
    "Nurburgring": {
        "At the first sharp right corner a crash is starting behind you, one of "
        "the cars behind you and torwards the left side of the track did not hit its "
        "brakes in time and caused a massive crash,": {
            1: "Stay on the right side of the track and speed up",
            2: "Stay where you are and hope they dont hit you"
        },
        "You are in first place but an opponent is right beside you (side by side), \n"
        "you are going into a long right hand corner (your opponent has colder tires,\n"
        "this means they will not have enough grip as you)": {
            1: "Keep left",
            2: "Keep right"
        },
        "At the last corner you are behind your opponent and both of you have the same tires and performance statistics": {
            1: "Try and overtake in the corner",
            2: "Stay behind the car in the corner and use splitstream on the "
               "long straight to try and pass your opponent"
        }
    },
    "Spa": {
        "You are in second place with 5 laps remaining, and the person in front of you \n"
        "(1st place) still has not used their pit stop. Both of you have the same tire \n"
        "wear level (hint: sometimes the driver wins the race, not the car)": {
            1: "Next lap go in for a pit stop",
            2: "Push the limits of the car and try and finish the race on the worn tires"
        },
        "On the last lap you are in second place still but right behind First place, \n"
        "your opponent in front of you is on old tires but is keeping on the inside of \n"
        "every turn": {
            1: "Try and find an opening on the inside",
            2: "Go on outside"
        }
    }
}
# win conditions for each track (predetermined)
winning_conditions = {
    "Nordschleife": [1, 1, 1],
    "Nurburgring": [1, 2, 2],
    "Spa": [2, 2]
}

def play_race(track_name):
    print(f"You are racing on {track_name}!")
    track = race_tracks[track_name]
    race_choices = {}

    for corner, options in track.items():
        print(f"\n{corner}, what do you choose?")
        for num, option in options.items():
            print(f"{num}: {option}")

        while True:
            player_choice = int(input("Enter the number of your choice: "))
            if player_choice in options.keys():
                race_choices[corner] = player_choice
                break
            else:
                print("Invalid choice. Please select a valid number.")

    if all(race_choices.get(corner, 0) == condition for corner, condition in
           zip(track.keys(), winning_conditions[track_name])):
        print(f"\nCongratulations! You won the race on {track_name}!")
        return True
    else:
        print("\nYou lost the race. Better luck next time!")
        return False

def is_ready():
    while True:
        response = input("Are you ready to proceed to the next track? (yes/no): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

def race_car_game():
    print("Welcome to the Alien GT3 Racing Cup!")

    tracks_left = ["Nordschleife", "Nurburgring", "Spa"]
    player_progress = 0

    while player_progress < len(tracks_left):
        track_name = tracks_left[player_progress]
        if play_race(track_name):
            print(f"\nAlien 4 gives you a clue:")
            print(f"{alien_clues[player_progress + 1]}\n")
            choice_add_clue()
            if player_progress < len(tracks_left) - 1:
                if is_ready():
                    player_progress += 1
                else:
                    print("You can try again to win the race.")
                    break  # End the game
            else:
                player_progress += 1  # Move to the next track
        else:
            print("\nYou have to restart from the first race track.")
            player_progress = 0  # Restart from the first track

    if player_progress == len(tracks_left):
        print("Congratulations! You have won all three races and completed the game!")

# ALLISON NICHOLS - Rock Paper Scissors - Alien 5:
'''Sets CPU Choice'''
def get_option_cpu():
    var = random.randint(1, 4)
    if var == 1:
        choice = "rock"
    elif var == 2:
        choice = "paper"
    elif var == 3:
        choice = "scissors"
    elif var == 4:
        '''Yes, this is a FRIENDS reference if you get it :)'''
        choice = "fire"

    return choice

'''Gets player input'''
def get_option_p():
    choice = "unknown"
    print("*****************************************************")
    info = input("Please enter r for rock, p for paper, and s for scissors: ")

    while choice == "unknown":
        if info == "r":
            choice = "rock"
        elif info == "p":
            choice = "paper"
        elif info == "s":
            choice = "scissors"
        else:
            choice = "unknown"
            print("*****************************************************")
            info = input("Please enter r for rock, p for paper, and s for scissors: ")

    return choice

'''Sets the Scores'''
def get_score(player, cpu):
    if player == "rock":
        if cpu == "rock":
            score1 = 0
            score2 = 0
            scores = [score1, score2]
            print("You Lost!")
        elif cpu == "paper":
            score1 = 0
            score2 = 1
            scores = [score1, score2]
            print("You Lost!")
        elif cpu == "scissors":
            score1 = 1
            score2 = 0
            scores = [score1, score2]
            print("You Win!")
        elif cpu == "fire":
            score1 = 0
            score2 = 1
            scores = [score1, score2]
            print("You Lost!")
    elif player == "paper":
        if cpu == "rock":
            score1 = 1
            score2 = 0
            scores = [score1, score2]
            print("You Win!")
        elif cpu == "paper":
            score1 = 0
            score2 = 0
            scores = [score1, score2]
            print("You Lost!")
        elif cpu == "scissors":
            score1 = 0
            score2 = 1
            scores = [score1, score2]
            print("You Lost!")
        elif cpu == "fire":
            score1 = 0
            score2 = 1
            scores = [score1, score2]
            print("You Lost!")
    elif player == "scissors":
        if cpu == "rock":
            score1 = 0
            score2 = 1
            scores = [score1, score2]
            print("You Lost!")
        elif cpu == "paper":
            score1 = 1
            score2 = 0
            scores = [score1, score2]
            print("You Win!")
        elif cpu == "scissors":
            score1 = 0
            score2 = 0
            scores = [score1, score2]
            print("You Lost!")
        elif cpu == "fire":
            score1 = 0
            score2 = 1
            scores = [score1, score2]
            print("You Lost!")

    return scores





if __name__ == '__main__':
# KARIS LAND - CHOOSE YOUR OWN ADVENTURE: ALIEN 1
    # VARIABLES:
    journal_entry = dict()
    player_journal = dict()  # players journal
    player = "Player"
    item_nums = []  # stores inventory item numbers player has
    plr_inv_ls = []  # stores inventory names of items
    inventory_list = [0, 'Backpack', 'Particle Analyzer', 'Reading Glasses', 'Gun',
                      'Handheld Voice Recorder', 'Money:', 5]
    backpack1 = 'Backpack'
    analyzer2 = 'Particle Analyzer'
    glasses3 = 'Reading Glasses'
    gun4 = 'Gun'
    recorder5 = 'Handheld Voice Recorder'
    money6 = 'Money:'
    amt_money7 = 5
    beetles8 = 'Fairy Beetles (from Antaria)'
    fries9 = 'Fries with eel sauce'
    karma10 = 'Good Karma'
    badkarma11 = 'Bad Karma'
    badderkarma12 = 'Terrible Karma'
    none = ''
    guest_form = False
    found_backpack1 = False
    found_analyzer2 = False
    found_glasses3 = False
    found_gun4 = False
    found_recorder5 = False
    found_money6 = False
    found_amt_money7 = False
    found_beetles8 = False
    found_fries9 = False
    found_karma10 = False
    clues = ["CLUE 0: Motive: this alien is in debt to the Alien Bankers.",
             "CLUE 1: Shrink Ray: this alien has been working on shrink ray technology.",
             "CLUE 2: Celestial Chop Shop: has connections with a Celestial Chop Shop "
             "so they can disguise moon for something else.",
             "CLUE 3: This alien has had recent meetings with Zender, who has recently lost their moon and is the "
             "market for a new one.",
             "CLUE 4: alien hates Earth and all beings that live on it."]
    in_love = False
    # PYGAME PLACE SOUND
    pygame.init()  # initializes pygame for use in program
    window_width, window_height = 500, 300
    screen = pygame.display.set_mode((window_width, window_height))
    title = "CASE CLOSED: An Intergalactic Mystery"
    pygame.display.set_caption(title)
    wav_black_d = pygame.mixer.Sound('Ring02.wav')
    wav_black_d.play()
    while pygame.mixer.get_busy():  # continues running program while music plays
        pass  # python requires at least one line of code
        # inside while loop = placeholder

        # PYGAME WINDOW:
        window_size = (800, 600)  # Size of window
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_mode(window_size)  # Creates graphic window
        image = pygame.image.load('Case-Closed-Stamp.png')
        screen.blit(image, (85, 60))  # image position
        pygame.display.update()  # have to update the display for display changes to take place
        duration = 1  # Seconds that display will stay open
        start_time = time.time()
        while time.time() - start_time < duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        window_size = (800, 600)  # Size of window
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_mode(window_size)  # Creates graphic window
        image = pygame.image.load('alien_detective.png')
        screen.blit(image, (60, 5))  # image position
        pygame.display.update()  # have to update the display for display changes to take place
        duration = 2  # Seconds that display will stay open
        start_time = time.time()
        while time.time() - start_time < duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        pygame.quit()

    # OPENING SEQUENCE:
    clear_screen()
    print("****************************************************")
    print("CASE CLOSED - An Intergalactic Mystery")
    print("****************************************************\n\n\n")
    clear_screen()
    print("[YOU ARRIVE ON CELESTIAL PRIME, THE PRIMARY GOVERNING PLANET FOR THE ANDROMEDA GALAXY]")
    clear_screen()
    add_image("celestial_prime.jpg", 1280, 720, 0, 0, 3)
    print("[YOU ARE GREETED BY A TINY FLYING DRONE]")
    clear_screen()
    add_image("hitch.jpg", 800, 500, -40, 0, 3)
    print("FLYING DRONE: Thank you so much for coming! We are in desperate need of your help to keep the \n"
          "Andromeda and Milky Way Galaxies from going to war! And of course all the primary suspects are\n"
          " from Andromeda.")
    clear_screen()
    print("The Earth has been robbed of it's moon!\n  It is up to you to find the thief and "
          "return the moon before\n   the Earth collapses into the Sun. \n    You have 1 week.\n\n")
    clear_screen()
    player = input("What name should be print on your office door for you, \"Detective: ")
    clear_screen()
    print(f"\nWe are so fortunate to have you on the case Detective {player}.\n   We have heard great things!\n\n")
    clear_screen()

    print("Let me introduce you to your CLUE BOOK.")
    clear_screen()
    print("Your CLUE BOOK is where you will store all clues you come across to solve the mystery.\n"
          "DON'T FORGET TO WRITE SOMETHING DOWN.\n    You will only be given the clue once.\n\n")
    clear_screen()
    player_journal = write_journal_entry(player)
    print(player_journal)
    player_journal.clear()
    clear_screen()
    print("You can add as many clues as you want to the same suspect!")
    print("Just be sure to type the suspect name THE SAME every time.\n\n")
    clear_screen()
    '''print("Let's try it again.")
    write_journal_entry(player)
    for k, v in player_journal.items():
        print("Player Journal", k, v)
    print("Journal entry", journal_entry)'''

# MINI GAME:
''' Choose your own adventure. '''
print(f"Detective {player} our sources have provided you with a list of suspect:\n"
      f"1. alien_1\n2. alien_2\n3. alien_3\n4. alien_4\n5. alien_5")
print("[You an can just add a name and no clue by hitting enter when prompted for the clue.]")
choice_add_clue()
clear_screen()
print("[INTELLIGENCE]: We know the person who stole the moon would need to have these attributes:")
print("1. Motive\n2. A Shrink Ray\n3. Connections to a Celestial Chop Shop\n4. A Buyer"
      "\n5. Disdain for Earth and/or its inhabitants")
choice_add_clue()
clear_screen()
print("You'll need to decide what you want to bring for your investigation.\n")
print("But there's only so much you can carry. Choose wisely.\n\n")
clear_screen()
item_nums = create_inventory(item_nums)
clear_screen()
update_inventory_item(none, none, first_time=False)
choice = input("Are you sure these are the items you would like to take (yes or no): ")
if choice == "no":
    item_nums = create_inventory(item_nums)
clear_screen()
print("OK! Hope you made some wise decisions! We've got your ship gassed up and ready to head out!\n")
print("What's that? Who am I you ask?\n")
print("My name is Hitch! I am an AI Cogent Custodian here to supply you with information about your mission.\n")
clear_screen()
print("Speaking of missions! Let's get back to it, time is of the essence, Detective!\n")
print("I'll meet you at the Astronexus! We have prepared a ship for your journey. "
      "It's in the last docking module on the right.\n\n")
clear_screen()

# WALKING TO THE ASTRONEXUS:
pygame.init()  # initializes pygame for use in program
wav_intense = pygame.mixer.Sound('intense.mp3')
wav_intense.play()
while pygame.mixer.get_busy():  # continues running program while music plays
    pass  # python requires at least one line of code
    # inside while loop = placeholder
    window_size = (1000, 500)  # Size of window
    screen = pygame.display.set_mode(window_size, pygame.NOFRAME)
    pygame.display.set_mode(window_size)  # Creates graphic window
    image = pygame.image.load('walk_to_ship.png')
    screen.blit(image, (35, 32))  # image position
    pygame.display.update()  # have to update the display for display changes to take place
    duration = 5  # Seconds that display will stay open
    start_time = time.time()
    while time.time() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    pygame.quit()

# SEEING THE SHIP (video):
pygame.init()
wave = pygame.mixer.Sound('ship_music.wav')
wave.play()
while pygame.mixer.get_busy():  # continues running program while music plays
    pass  # python requires at least one line of code
    # inside while loop = placeholder
    add_image("golden_ticket2.JPG", 800, 500, 25, 25, 4)
pygame.quit()

print("HITCH: Nice to see you again, this is your ship, Golden Ticket!")
print("HITCH: As stated in your contract, the ship will be yours upon successful completion "
      "of your case!\n\n")
clear_screen()
print("HITCH: Would like to head straight to the home planet of alien_1,"
      " Nova Terra, or you would like to take time to read her bio first?")
while True:
    try:
        int_choice = int(input("[CHOICE]\n1. Head straight to alien_1's planet.\n2. Take time to read her bio first.\n"
                               "[ENTER 1 or 2]: "))
        if int_choice == 2:
            clear_screen()
            print("You find out from alien_1 bio that she loves chocolate covered Fairy Beetles "
                  "from Antaria.\n")
            choice_add_clue()
            clear_screen()
            choice2 = input("In light of this new information would you like to head to Antaria first and get some "
                            "Fairy Beetles \nto take to alien_1 before heading to "
                            "Nova Terra [yes or no]: ")
            choice2 = choice2.lower()
            break
        elif int_choice == 1:
            print("Alright let's get the engines up and running and head for Nova Terra.\n\n")
            # add_image()
            choice2 = 'no'
            clear_screen()
            break
        else:
            print(f"Now Detective {player}, I'm sorry, but that's just not an a choice "
                  f"we can make at this time.\n\n")
            clear_screen()
    except ValueError:  # if string is entered
        print("Um... ok... That's not even a number. Let's try that again, DETECTIVE.")
        clear_screen()

if choice2 == 'yes':
    clear_screen()
    print("YOU HEAD TO ANTARIA ---->>>> \n")
    clear_screen()
    add_image("antaria2.png", 950, 500, 0, 0, 3)
    print("As you look for a shop that sells Fairy Beetles you are taken \n"
          "with the cultural diversity of the place and how everyone seemed to be getting along \n"
          "quite peacefully!")
    clear_screen()
    print("[YOU FINALLY FIND A LITTLE STAND IN THE STREET MARKET SELLING THEM]")
    clear_screen()
    add_image("antaria_market.jpg", 1300, 720, 0, 0, 3)
    has_item = check_inventory(plr_inv_ls, backpack1)
    has_item2 = check_inventory(plr_inv_ls, money6)
    if has_item and has_item2:
        print("You pay 1 DOCAN for them and slide them into your BACKPACK to take them back to your ship.\n\n")
        spend_money()
        clear_screen()
        update_inventory_item(beetles8, none, first_time=True)
    else:
        print("OOPS! You don't have the necessary items!\n\n"
              "ITEMS NEEDED:\n* BACKPACK\n* MONEY (1 ducan)")
        clear_screen()

print("YOU HEAD TO NOVA TERRA TO MEET WITH alien_1 ----->>>>> \n\n")
clear_screen()
add_image("nova_terra6.JPG", 1280, 720, 0, 0, 3)
clear_screen()
print("[AS YOU MAKE YOUR WAY TO THE BUILDING YOU ARE STRUCK BY HOW CURIOUS AND \n"
      "BRAZEN THE SENTIENTS ON THIS PLANET ARE!]")
clear_screen()
add_image("nova_terra_streets.JPG", 630, 600, 0, 0, 3)
print("[YOU ENTER THE FRONT OFFICE OF alien_1. A RECEPTIONIST GREETS YOU.]\n\n")
clear_screen()
add_image("receptionist.jpg", 630, 650, 0, 0, 3)
choice = input("RECEPTIONIST (grumpy): Please fill out our standard guest form.\n"
               "[HE DOESN'T LOOK UP]\n")
clear_screen()
for item in plr_inv_ls:
    if item == glasses3:
        print("[You pull out your READING GLASSES and fill out the form]")
        clear_screen()
        found_glasses3 = True
        guest_form = True
        print("RECEPTIONIST (less grumpy): You know there's a bar down the street. "
              "It'll be about 40 mins before she can see you.")
        clear_screen()
        found_glasses3 = True
    if found_glasses3:
        break
if not found_glasses3:
    print("OOPS! You don't have your READING GLASSES!\n")
    clear_screen()
    for item in plr_inv_ls:
        if item == gun4:
            print("[HE LOOKS UP AT YOU, ANNOYED, "
                  "AND NOTICES THE GUN ON YOUR HIP]\n")
            print("RECEPTIONIST: Oh you're gonna need to leave that gun in our safe here at the front desk.")
            clear_screen()
            print("[RELUCTANTLY YOU HAND OVER YOUR GUN]\n")
            clear_screen()
            update_inventory_item(none, gun4, first_time=True)
            found_gun4 = True
            clear_screen()
            print("[AFTER WAITING FOR 20 MINS YOU ASK THE RECEPTIONIST HOW LONG IT WILL BE]\n\n")
            print("RECEPTIONIST (even grumpier): 40 mins to an hour (he doesn't look up).")
            clear_screen()
        if found_gun4:
            break


print("[CHOICE] WOULD YOU LIKE TO:\n1. Try to see what intel you can get from the grumpy receptionist.\n"
      "2. Find the local bar for a drink.\n")
choice = valid_number2(1, 2)
clear_screen()
if choice == 1:
    print("[AFTER 20 MINS OF THE RECEPTIONIST TELLING YOU HIS DISGRUNTLED OPINIONS \nABOUT"
          "POLITICS ON NOVA TERRA, HE DOES OFFER A HELPFUL TIP]")
    clear_screen()
    print("RECEPTIONIST: alien_1 truly hates it when people come to see her and don't \nask her"
          " how she's doing and what's new in her life before business talk.\n"
          "Personally I could go without small talk for the rest of my life!")
    choice_add_clue()
elif choice == 2:
    print("[YOU TELL RECEPTIONIST YOU WILL STEP OUT FOR A BIT AND COME BACK IN ABOUT 40 MINS]\n")
    print("[The receptionist grunts and tries to look like he's doing something important.]")
    clear_screen()
    print("[YOU HEAD TO THE LOCAL BAR ----- >>>>]\n\n")
    add_image("bar.png", 935, 525, 0, 0, 3)
    clear_screen()
    print("**** NOVA GRUB & GROB MENU **** \n1. Fries w/ eel sauce ...... ^1.000"
          "\n2. Spawn XX Beer ......... ^1.000\n"
          "3. Zoglot Grub Gratin...... ^20.000\n\n")
    print(["FRIES WITH EEL SAUCE?! YOUR FAVORITE!"])
    clear_screen()
    print("[YOU ORDER A BEER WITH FRIES]\n")
    add_image("bartender.png", 850, 580, 0, 0, 3)
    print("BARTENDER: That'll be 2 docans please, and quit floggin starin at me like "
          "a florkin Gorglimplits, ya scum blorp!\n")
    print("(((  Um.... WHAT? You think to yourself and cover your mouth to hide a smile.  )))\n")
    print("HITCH: Bar life on Nova Terra can be quite rough. I would say nothing.")
    clear_screen()
    has_item = check_inventory(plr_inv_ls, money6)
    if has_item:
        print("[YOU PULL OUT YOUR MONEY AND HAND HIM 2 DOCANS]")
        clear_screen()
        spend_money()
        spend_money()
        update_inventory_item(fries9, none, first_time=True)
        found_money6 = True
        clear_screen()
    else:
        print("[YOU REACH INTO AN EMPTY POCKET. AND REMEMBER YOU DIDN'T BRING ANY MONEY.]\n")
        clear_screen()
        print("YOU: \"Well you're never gonna believe this I forgot my docapouch on my ship.\n"
              "Would you let me come out back tomorrow and pay ya?\"")
        clear_screen()
        print("[WELL THAT GOES OVER ABOUT LIKE YOU'D IMAGINE]")
        clear_screen()
        print("BARTENDER: [JUMPS ON THE BAR AND GETS RIGHT IN YOUR FACE]\n"
              "Get the FLOG OUTTA MY BAR!!! Go back to "
              "whatever gloopish neonash galaxy ya floggin came from, FLERG!!")
        clear_screen()
    print("[ON YOUR WAY BACK TO THE OFFICE]\n")
    print("HITCH: Detective, I am detecting negative energy nearby. Approach with caution.")
    clear_screen()
    print("[!! SUDDENLY A GANG OF ALIENS JUMPS OUT FROM BEHIND A BUILDING !!]\n\n")
    add_image("gang2.jpg", 610, 410, 0, 0, 3)
    clear_screen()
    has_item = check_inventory(plr_inv_ls, gun4)
    if has_item:
        print("You pull out your GUN and yell that you are part of the Cosmic Enforcement Governship!")
        print("They back away slowly shaking their heads saying, \n"
              "'Sorry Guy you musta had the wrong idea.'")
        clear_screen()

    else:
        print("[YOU REACH FOR YOUR GUN, BUT IT'S NOT THERE!]\n\n")
        clear_screen()
        print("[OH NO! THEY TOOK ALMOST EVERYTHING YOU HAVE!]\n\n")
        plr_inv_ls = [fries9, money6, 1]
        clear_screen()
        print("UPDATED INVENTORY LIST:")
        for item in plr_inv_ls:
            print(f"* {item}")
        print("At least you still have your favorite snack, and your lucky DOCAN you always hide in your sock!")
        clear_screen()

    print("[JUST BEFORE YOU GET BACK TO THE OFFICE]\n")
    clear_screen()
    print("[YOU SEE A PODLESS ALIEN ON THE SIDE OF THE ROAD]\n")
    clear_screen()
    add_image("podless.jpg", 680, 700, 0, 0, 3)
    print("PODLESS ALIEN: Spare some docans?")

    print("[CHOICE] \n1. Give him a docan\n2. Offer him your fries \n3. Give nothing")
    choice = valid_number2(1, 3)
    if choice == 1:
        has_item = check_inventory(plr_inv_ls, money6)
        if has_item:
            print("You have received good karma for your deed!\n")
            clear_screen()
            update_inventory_item(karma10, none, first_time=True)
            spend_money()
            print("[YOU HEAD BACK TO THE OFFICE, wondering if the people who hired you "
                  "will stick to their payment contract\n"
                  " when all is said and done]")
        else:
            print("[YOU REACH IN YOUR POCKET AND REMEMBER YOU DON'T HAVE ANY MONEY!]")
            print("You apologize to the little alien and head back to the office.")
    elif choice == 2:
        has_item = check_inventory(plr_inv_ls, fries9)
        if has_item:
            print("You have received good karma for your deed.\n")
            update_inventory_item(karma10, fries9, first_time=True)
            print("[YOU HEAD BACK TO THE OFFICE, stomach growling, but feeling a sense of accomplishment]")
        else:
            print("You can't give something you don't have!")
            print("The podless alien looks at you with soft pleading eyes and you feel a sense of sorrow come over you.")
            clear_screen()
            print("[YOU HEAD BACK TO THE OFFICE, but not without looking back first and worrying about the little guy.]")
    else:
        print("Too bad, you might have needed that good Karma!")
        print("[THE PODLESS ALIEN SPITS A BLUE OOZE ON YOU]")
        clear_screen()
        print("[YOU SPIT BACK ON HIM]")
        clear_screen()
        print("[YOU HEAD BACK TO THE OFFICE FUMING. YOU HAVE NO TIME FOR THE NEEDS OF WEAKER BEINGS]")
        update_inventory_item(badkarma11, none, first_time=True)
        clear_screen()

    clear_screen()
    print("[BACK AT THE OFFICE]")
    clear_screen()

has_item = check_inventory(plr_inv_ls, fries9)
if has_item:  #fries9
    print("[THE RECEPTIONIST LOOKS UP AT YOU QUICKLY THIS TIME]\n")
    clear_screen()
    print("RECEPTIONIST: OOooOOH! Is that fries with eel sauce I smell?! Total favs!")
    print("[CHOICE]\n1. Give him fries\n2. Don't give him fries\n")
    choice = valid_number2(1, 2)
    if choice == 1:
        update_inventory_item(none, fries9, first_time=True)
        print("RECEPTIONIST: YES! Thanks man!")
        print("Here let me give you this extra ticket I have to this show"
              " in a couple days!")
        clear_screen()
        print("[HE HANDS YOU A TICKET]\n")
        print("** [TICKET] COSMIC CONJURERS THE AMAZING SHRINK RAY SPECTACLE ....^100.000 **")
        clear_screen()
        has_item = check_inventory(plr_inv_ls, glasses3)
        if has_item:
            print("[YOU PULL OUT YOUR GLASSES TO READ THE FINER PRINT]\n")
            clear_screen()
            print("FINER PRINT: Brought to you by alien_4, the great Galactive Dimensionist.\n"
                  "Pioneer of Shrinking Technology! Come see the show this Andromeday at 7 o'clicks.")
            clear_screen()
            update_inventory_item('Shrink Ray Tickets', none, first_time=True)
            clear_screen()
            choice_add_clue()
            found_glasses3 = True
        else:
            print("You strain your eyes but without your GLASSES, you can't make out the finer print.")
            clear_screen()
    elif choice == 2:
        print("YOU: Yeah their my favorite too.\n")
        print("[YOU SIT DOWN AND EAT THEM IN FRONT OF THE RECEPTIONIST]")
        print("[IT THRILLS YOU TO GET BACK AT THE LITTLE WEASEL AND HIS BAD ATTITUDE.")
        has_item = check_inventory(plr_inv_ls, karma10)
        if has_item:
            print("Too bad it has cost you your good karma points, but at least your belly is full!")
            update_inventory_item(none, karma10, first_time=True)
        if not has_item:
            print("HITCH: Hope that bad karma doesn't come back to haunt ya!")
            update_inventory_item(badkarma11, none, first_time=True)
    else:
        print("The receptionist doesn't acknowledge your return. Just keeps typing away on an ancient looking device.\n"
              "It looks like a box with a screen and has a button pad in front of it with letters on it.")
clear_screen()
add_sound('office_ding.wav')
clear_screen()
print("RECEPTIONIST: Oh. Look. She's ready for you. You can head on in.")
clear_screen()
print("[YOU HEAD INTO A LARGE BACK OFFICE THAT IS DECADENTLY DECORATED]")
clear_screen()
add_sound("secosmic_lo.WAV")
add_image("alien_1.png", 690, 690, 0, 0, 4)
print(f"alien_1: Hello there, Detective {player}. I've been expecting you.")
clear_screen()
print("[YOU'RE TAKEN BACK BY HER POISE AND GRACE, you stumble for your words.]")
print("[CHOICE]\n1. Get straight to the investigation\n2. Give her Fairy Beetles\n3. Ask her about her children")
choice = valid_number2(1, 3)
alien_annoyed1 = False
alien_annoyed2 = False
if not guest_form:
    alien_annoyed1 = True
    print("alien_1: I see it was just too much for you to fill out our standard form.")
    print("[SHE DOES NOT TRY TO DISGUISE HOW ANNOYED SHE IS]")
if choice == 1:
    print("[SHE IS ANNOYED WITH YOUR HASTY MANNERS]")
    alien_annoyed2 = True
if choice == 2:
    has_item = check_inventory(plr_inv_ls, beetles8)
    if has_item:
        if alien_annoyed1:
            print("[SHE IMMEDIATELY FORGIVES YOU FOR NOT FILLING OUT THE GUEST FORM]")
            clear_screen()
            alien_annoyed1 = False
        print("[SHE IS ABSOLUTELY DELIGHTED]")
        print("She tells you how she came to love them and that she was introduced to them by alien_3.\n"
              "Back in her early 20s hanging out at Nebula Nip and Tuck together, alien_3's parents\n"
              "shop.")
        clear_screen()
        print("HITCH: [whispers to you] Detective, that's a celestial chop shop... you know where they"
              "take planets and give them a facelift... or put another way... make a planet unrecognizable.")
        clear_screen()
        choice_add_clue()
    else:
        print("You can't give something you don't have!")
if choice == 3:
    print("alien_1 is deLIGHTED that you have asked about her children!")
    print("She goes on and on and at some point you zone out and begin to look at the art around the room...\n")
    print("...distracted by a particular painting.")
    clear_screen()
    has_item = check_inventory(plr_inv_ls, recorder5)
    if has_item:
        print("You get out your handheld recorder and record what's she's saying to review later.")
        clear_screen()
        print("When you review the tape later you find out she did actually say something useful.")
        print("alien_1: '...I mean you really just never know about sentients. The guy living next to you\n"
              " might decide he hates your children as much as he hates humans and earth. My friend Stera's\n"
              "children came out looking just like humans and the head of the HUMAN EXOFANATIC FRONT, alien_5\n"
              " tried to take them prisoner when they were just walking in a terrapark on Galandral."
              "I mean we all hate...[THE TAPE MAKES A SHUFFLING, SCRUBBING SOUND AND THE REST IS INAUDIBLE] \n"
              " ")
        clear_screen()
        print("HITCH: Detective, the Human Exofanatic Front, is an organization that thinks the\n"
              " galaxy would be a better place if we could rid it of humans. Believing that they\n"
              "are the cause for most disease spread and warlike thinking.")
        choice_add_clue()
    else:
        add_image("painting2.jpg", 410, 600, 0, 0, 3)
        print("You space off deeper and deeper into the dreaminess of the painting...")
        print("[UNTIL FINALLY YOU HEAR YOUR NAME]")
        clear_screen()
        print("alien_1: Detective, have you even listened to a word I've said?!")
        print("[YOU TELL HER HOW LOVELY HER CHILDREN SOUND AND ALL IS SAVED]")
        clear_screen()
print("[YOU LEAN IN FOR SOME DEEP INTERROGATION WORK]")
clear_screen()
if alien_annoyed1 and alien_annoyed2:
    print("[SHE IS TOO ANNOYED BY YOU TO ANSWER YOUR QUESTIONS]")
    print("[YOU REFUSED TO FILL OUT THE GUEST FORM AND YOU RUSHED HER INTO BUSINESS TALK]")
    print("[SHE SHOWS YOU THE DOOR]")
    print("[CHOICE]\n1. You use your gun to intimidate her\n2. You offer her Fairy Beetles\n"
          "3. You try your luck with flattery and see if karma is on your side\n")
    choice = valid_number2(1, 3)
    if choice == 1:
        has_item = check_inventory(plr_inv_ls, gun4)
        if has_item:
            print("[YOU JUMP UP AND PULL OUT YOUR GUN, AIMING DIRECTLY AT HER HEAD]")
            print("YOU: I need to know any information you know that is helpful to this investigation!")
            clear_screen()
            print("She throws up her hands and yells for help.")
            print("[AS YOU JUMPED UP YOU KNOCKED A STATUE OVER THAT BROKE ON THE FLOOR]")
            add_image("moon-rock.jpg", 510, 490, 0, 0, 3)
            clear_screen()
            print("[SHE SHRIEKS] Oh! That was a gift from alien_4!")
            print("Please leave!")
            clear_screen()
            print("[YOU GRAB THE BROKEN STATUE AND RUN OUT THE DOOR]")
        else:
            print("[YOU REACH FOR YOUR GUN INSTINCTUALLY, BUT IT'S NOT THERE]")
            print("alien_1: Missing something? Please leave.")
            print("[SHE PUSHES YOU OUT THE DOOR]")
            has_item = check_inventory(analyzer2)
            if has_item:
                print("The statue looks like it's made out of a strange rock and you feel heat "
                      "coming from it.")
                print("[YOU USE YOUR PARTICLE ANALYZER TO DETERMINE WHAT IT'S MADE OUT OF]")
                clear_screen()
                print("PARTICLE ANALYZER: Material is from the core of Earth's moon. \n"
                      "The material has piezoelectric capabilities far exceeding most\n"
                      " materials currently available in the Galaxy Exchange markets.")
                clear_screen()
                print("Detective, the only way to obtain this kind of material is through"
                      "aggressive forms of piezoelectric energy harvesting, which is very \n"
                      "hard on a celestial body. This kind of harvesting on the moon is currently limited\n"
                      "significantly by Earth's governing bodies.")
                clear_screen()
                print("(You think to yourself... well that would be a pretty good motive to STEAL IT!")
                choice_add_clue()
            else:
                print("As you look at the statue you feel heat resonating from it... as if\n"
                      "there was energy emanating from it. It reminds of moon rock...")
                clear_screen()
                print("You wish you had your PARTICLE ANALYZER so you could know more!")
                choice_add_clue()
    if choice == 2:
        has_item = check_inventory(plr_inv_ls, beetles8)
        if has_item:
            print("You pull out the Fairy Beetles and she immediately changes her tone.")
            print("alien_1: OOOOOOH MYYYYYY. Well why didn't ya tell me you brought these?!")
            clear_screen()
            print("After gesturing for you both to resume your conversation...")
            print("She tells you how she came to love them and that she was introduced to them by alien_3.\n"
                  "Back in her early 20s hanging out at Nebula Nip and Tuck together, alien_3's parents\n"
                  "shop.")
            clear_screen()
            print("HITCH: [whispers to you] Detective, that's a celestial chop shop... you know where they"
                  "take planets and give them a facelift... or put another way... make a planet unrecognizable.")
            clear_screen()
            choice_add_clue()
            print("[AFTER A LONG LINE OF QUESTIONING YOU FIND OUT THAT alien_4 has been mining the\n"
                  "the moon illegally. And has been talking about ways to increase this illegal mining.\n"
                  "Apparently mooncore rocks have incredible piezoelectric energy and is very valuable\n"
                  "in the dark market.")
            choice_add_clue()

        else:
            print("You don't have Fairy Beetles to give her!")
    if choice == 3:
        print("YOU: Madam, before I go, might I just say that you have the most stunning office!\n"
              "And your staff is just top notch. I really respect someone who knows how to run\n"
              "a good business!")
        has_item = check_inventory(plr_inv_ls, karma10)
        if has_item:
            chance = roll_dice()
            if chance > 3:
                print("She is completely taken off guard by your flattery and calms down.")
                print("alien_1: [smiling softly] Perhaps I got worked up over nothing. Let's continue.")
                clear_screen()
                print("[AFTER A LONG LINE OF QUESTIONING YOU FIND OUT THAT alien_4 has been mining the\n"
                      "the moon illegally. And has been talking about ways to increase this illegal mining.\n"
                      "Apparently mooncore rocks have incredible piezoelectric energy and is very valuable\n"
                      "in the dark market.")
                choice_add_clue()
            else:
                print("Even with your good Karma, Luck was just not on your side.")
                print("You head out the door.")
        has_item = check_inventory(plr_inv_ls, badkarma11)
        if has_item:
            chance = roll_dice()
            if chance > 16:
                print("[DESPITE YOUR BAD KARMA IT SEEMS YOU HAVE A TALENT FOR FLATTERY]")
                print("She is completely taken off guard by your flattery and calms down.")
                print("alien_1: [smiling softly] Perhaps I got worked up over nothing. Let's continue.")
                clear_screen()
                print("[AFTER A LONG LINE OF QUESTIONING YOU FIND OUT THAT alien_4 has been mining the\n"
                      "the moon illegally. And has been talking about ways to increase this illegal mining.\n"
                      "Apparently mooncore rocks have incredible piezoelectric energy and is very valuable\n"
                      "in the dark market.")
            else:
                print("With a little more Karma you might have had better luck.")
                print("You head out the door.")
        has_item = check_inventory(plr_inv_ls, badderkarma12)
        if has_item:
            chance = roll_dice()
            if chance > 19:
                print("[DESPITE YOUR TERRIBLE KARMA IT SEEMS YOU ARE A MASTER OF CHARM]")
                print("She is completely taken off guard by your flattery and calms down.")
                print("alien_1: [smiling softly] Perhaps I got worked up over nothing. Let's continue.")
                clear_screen()
                print("[AFTER A LONG LINE OF QUESTIONING YOU FIND OUT THAT alien_4 has been mining the\n"
                      "the moon illegally. And has been talking about ways to increase this illegal mining.\n"
                      "Apparently mooncore rocks have incredible piezoelectric energy and is very valuable\n"
                      "in the dark market.")
            else:
                print("With a more Karma you might have had better luck.")
                print("You hit a statue off a side table on the way out and it smashes to pieces on the ground!!")
                add_image("moon-rock.jpg", 510, 490, 0, 0, 3)
                clear_screen()
                print("It makes an unusually loud sound as it shatters.")
                add_sound('EXPLODE.WAV')
                print("[SHE SHRIEKS] Oh! That was a gift from alien_4!")
                print("LEAVE AND DON'T THINK ABOUT COMING BACK HERE!")
                clear_screen()
                print("[YOU GRAB A PIECE OF THE BROKEN STATUE AND ANGRILY SLOW WALK OUT THE DOOR]")
                has_item = check_inventory(analyzer2)
                clear_screen()
                print("[ONCE SAFELY OUTSIDE THE BUILDING]")
                print("You look at the statue piece and feel heat resonating from it... as if\n"
                      "there was energy emanating from it. It reminds of moon rock...")
                print("You feel a sense of power within your hands. You know that feeling.")
                print("You want more of that feeling.")
                clear_screen()
                print("Something compels you to lick it.")
                print("A spark of electricity takes you by surprise!")
                clear_screen()
                print("HITCH: Oh my Detective! It appears that rock has some piezoelectric energy. Rocks with that\n"
                      " power are very valuable on the dark market. I wonder where it came from?")
                clear_screen()
                print("YOU: I'm thinking the MOON!")
                print("HITCH: Didn't she say that was a gift from alien_4?")
                choice_add_clue()
else:
    if alien_annoyed1 or alien_annoyed2:
        print("[SHE RESPONDS WITH SHORT ANSWERS THAT ARE TO THE POINT, CLEARLY READY FOR YOU TO FINISH AND LEAVE]")
    print("[AFTER A LONG LINE OF QUESTIONING YOU FIND OUT THAT alien_4 has been mining the\n"
          "the moon illegally. And has been talking about ways to increase this illegal mining.\n"
          "Apparently mooncore rocks have incredible piezoelectric energy and is very valuable\n"
          "in the dark market.")
    choice_add_clue()
    clear_screen()
    if not alien_annoyed1 or alien_annoyed2:
        print("You find yourself completely captivated by this sh'male. She has such a presence about\n"
              " her. You can see how she could get almost anyone to do something for her. And you find\n"
              " yourself... wanting to get to know her better...\n")
        print("HITCH [WHISPERS]: I'm detecting strange vitals from you detective. I think it is best you\n"
              "stay focused on the task at hand!")
        clear_screen()
        print("[alien_1 TAKES YOUR HAND]")
        print(f"alien_1: I feel it too Detective {player}.")
        has_item = check_inventory(plr_inv_ls, beetles8)
        if has_item:
            print("[YOU SUDDENLY REMEMBER YOU HAVEN'T GIVEN HER THE FAIRY BEETLES YET]")
            clear_screen()
            print("YOU: I've brought you something I think you might like.")
            print("[YOU PULL OUT THE FAIRY BEETLES FROM ANTARIA]")
            clear_screen()
            print("[SHE JUMPS UP AND SHRIEKS WITH JOY, GRABBING YOU BY THE COLLAR AND GIVING YOU A VERY INVOLVED KISS]")
            print("[IT'S SO INTENSE YOU FEEL DIZZY]")
            in_love = True
            clear_screen()
            add_image("dizzy3.jpg", 1600, 720, 150, 0, 4)
            print("HITCH: Oh my.")
            clear_screen()
            print("alien_1: OH THIS HAS TRULY BEEN A DELIGHTFUL DAY!")
            clear_screen()
            print("[ONCE YOU HAVE BOTH CALMED BACK DOWN AND ARE SEATED AGAIN] She tells you how she came to love\n"
                  " them and that she was introduced to them by alien_3. Back in her early 20s hanging out at\n"
                  " Nebula Nip and Tuck together, alien_3's parent's shop.")
            clear_screen()
            print("HITCH: [whispers to you] Detective, that's a celestial chop shop... \n"
                  "planets are taken to give them a facelift... \n"
                  "or put another way... make a planet unrecognizable.")
            clear_screen()
            choice_add_clue()
            clear_screen()
            print("[AFTER A LONG CHAT GOING VERY MUCH OFF TOPIC]")
            print("HITCH: I really think we need to be going, Detective! Time is ticking.")
            clear_screen()
            print("[AS YOU SAY YOUR GOODBYES SHE PULLS YOU TO HER AND LOOKS DEEP INTO YOUR EYES]")
            print("alien_1: Come back to see me when you're done with this dreadful case. I would love to show you\n"
                  "what I've been working on... where we can speak privately, of course [SHE GLARES AT HITCH].")
            clear_screen()
            print("alien_1: I'd like for you to have this. A gift.")
            print("[SHE PLACES A SMALL STATUE IN YOUR HAND")
            add_image("moon-rock.jpg", 510, 490, 0, 0, 3)
            clear_screen()
            print("[AWKWARDLY CLEAR YOUR THROAT, THANK HER FOR THE GIFT WITH A BOW AND LEAVE, \n"
                  "later wondering, sheepishly, why on Galagal you BOWED to her?!]")
            clear_screen()
            has_item = check_inventory(plr_inv_ls, analyzer2)
            if has_item:
                print("[ONCE OUTSIDE THE BUILDING]")
                print("The statue looks like it's made out of a strange rock and you feel heat "
                      "coming from it.")
                print("[YOU USE YOUR PARTICLE ANALYZER TO DETERMINE WHAT IT'S MADE OUT OF]")
                clear_screen()
                print("PARTICLE ANALYZER: Material is from the core of Earth's moon. \n"
                      "The material has piezoelectric capabilities far exceeding most\n"
                      " materials currently available in the Galaxy Exchange markets.")
                clear_screen()
                print("Detective, the only way to obtain this kind of material is through"
                      "aggressive forms of piezoelectric energy harvesting, which is very \n"
                      "hard on a celestial body. This kind of harvesting on the moon is currently limited\n"
                      "significantly by Earth's governing bodies.")
                clear_screen()
                print("(You think to yourself... well that would be a pretty good motive to STEAL IT!")
                choice_add_clue()

        else:
            print("[YOU QUICKLY CLEAR YOUR THROAT AND ANNOUNCE IT'S PROBABLY ABOUT TIME TO GET GOING]")
            clear_screen()

print("[TAKE A MOMENT TO JOT DOWN ANY ADDITIONAL NOTES AND REVIEW THE CLUES YOU'VE UNCOVERED?]")
choice_add_clue()

print("HITCH: Alright! Time to move on to your next suspect. Unfortunately this is where I\n"
      " must leave you Detective. I have another new client to provide orientation services to.\n"
      "Good luck with the case! I truly believe we picked the right detective for the job!")
clear_screen()
print("[YOU HEAD BACK TO YOUR SHIP AND ON TO THE NEXT SUSPECT]")
add_image("leave.jpg", 1300, 800, -40, 0, 3)


# AMY SIEMER: SEQUENCE GAME - ALIEN 2
add_image('underwater.jpg', 1300, 750, 0, 100, 3)
print("[YOU ARRIVE ON TERRA MINOR TO SPEAK WITH ALIEN 2")
print("[PUT ON YOUR ASTRO-SCUBA SUIT, YOU'RE HEADED UNDER WATER FOR THIS SUSPECT!")
clear_screen()

play_game()
print("[YOU LEAVE AND HEAD OUT TO INTERROGATE THE NEXT SUSPECT]")
clear_screen()
add_image("leave.jpg", 1300, 800, -40, 0, 3)

# MAX KURTS: BLACK JACK - ALIEN 3
add_image("city3.jpg", 1300, 800, 0, 20, 3)
print("[YOU ARRIVE ON VORTRAN TO SPEAK WITH ALIEN 3]")
clear_screen()

play_blackjack()
print("[YOU LEAVE AND HEAD OUT TO INTERROGATE THE NEXT SUSPECT]")
clear_screen()
add_image("leave.jpg", 1300, 800, -40, 0, 3)

# AMAR LJUBOVIC: NUMBER SEQUENCE - ALIEN 4
add_image("city4 3.jpg", 1300, 800, 70, 0, 3)
print("[YOU ARRIVE ON AETHERA TO SPEAK WITH ALIEN 4, this time you're headin' to the Tracks!")
clear_screen()
print("[YOUR GREETED BY ALIEN 4 AND HE'S A BUSY SENTIENT, RUNNING A RACE TRACK]")
print("[YOU'RE GONNA HAVE TO GET INVOLVED IF YOU WANT TO GET CLUES OUT OF HIM]")
clear_screen()
add_image('alien_4.jpg', 540, 700, 0, 0, 3)

race_car_game()
print("[YOU LEAVE AND HEAD OUT TO INTERROGATE THE NEXT SUSPECT")
clear_screen()
add_image("leave.jpg", 1300, 800, -40, 0, 3)


# ALLI NICHOLS - Rock Paper Scissors - Alien 5:
add_image('city 5.jpg', 1300, 750, 0, 0, 3)
print("[YOU ARRIVE ON PURRIYA TO MEET WITH YOUR NEXT SUSPECT]")
clear_screen()
''' This is the beginning sequence of the game :) Sets the Tone :)'''
print("*The dark and mysterious figure in front of you seemed to appear from thin air*")
clear_screen()
add_image('alien_5.jpg', 480, 600, 0, 0, 3)
time.sleep(3)
print('"I hear you need some information on the Aliens", They say to you.')
time.sleep(3)
print('"Yes", You reply.')
time.sleep(3)
print('"Well, I may as well make purrrrfectly fun for myself.", They says laughing.')
time.sleep(3)
print('*They kind of creep you out and seem super sketchy. They for sure have something up their sleeve,'
      'but you agree to play.*')
time.sleep(3)
print('"You only get clues if you win, so let the games begin"')

'''This is the variables needed for the loop'''
GameCont = True
PlayerTotalScore = 0
CPUTotalScore = 0
ClueOne = False
ClueTwo = False
ClueThree = False

'''This is where the game actually starts'''
while GameCont:
    PlayerChoice = get_option_p()
    CPUChoice = get_option_cpu()

    '''The alien you play is supposed to read minds, so any tie or 'fire' is them winning! It's supposed to take
    more than 3-6 plays to win this portion :)'''
    GameScore = get_score(PlayerChoice, CPUChoice)

    PlayerScore = GameScore[0]
    CPUScore = GameScore[1]

    PlayerTotalScore = PlayerTotalScore + PlayerScore
    CPUTotalScore = CPUTotalScore + CPUScore

    if PlayerTotalScore == 1 and ClueOne == False:
        print('"UGH! How did you beat me already..." *A claw pops out of their "hand" *')
        time.sleep(3)
        print('"Fine, the first clue I can give you is that Alien 1 has been scorned by people on earth '
              'over and over. They have a rather large hatred for earth now."')
        choice_add_clue()
        time.sleep(3)
        print('"Well, lets continue because I have two more clues I can give you"')
        time.sleep(3)
        print("*You are still freaked out by the figure, but take note of the information*")
        time.sleep(3)
        ClueOne = True

    elif PlayerTotalScore == 2 and ClueTwo == False:
        print('"This was not how this was supposed to go!" they hissed.')
        time.sleep(3)
        print('"Well fine, the next piece of information is Alien 3 has a severe distaste of humankind.\n'
              ' He just '
              'wants to ruin something for them to get back at them. Just as promised."')
        choice_add_clue()
        time.sleep(3)
        print("*Something seems off about the figure still, but you again note the clue he told you*")
        time.sleep(3)
        ClueTwo = True

    elif PlayerTotalScore == 3 and ClueThree == False:
        print('"I am supposed to be able to read minds!!!" they shouted.')
        time.sleep(3)
        print('*You are perplexed until their hood and mask come off revealing they are Alien 5!*')
        time.sleep(3)
        print('*They hiss and growl at you for beating them.*')
        time.sleep(3)
        print('"Well, I guess this is the last piece of information you need from me."')
        time.sleep(3)
        print('"Alien 2 has built a shrink ray and hae tested it with great success."')
        choice_add_clue()
        time.sleep(3)
        print("*They disappear as fast as they appeared, now it seems cat-like, not creepy, "
              "but at least you got the information*")
        ClueThree = True
        GameCont = False

'''Then we would transition to the next game :)'''





print(["AFTER THE FINAL INTERROGATION YOU HEAD BACK TO CELESTIAL PRIME"])
print("[TAKE A LOOK AT YOUR CLUE BOOK TO SEE WHO YOU THINK THE THIEF IS]")
clear_screen()
print(player_journal)
print("[CHOICE]\nWHO IS THE THIEF:\n1. Alien 1\n2. Alien 2\n3. Alien 3\n4. Alien 4\n5. Alien 5\n"
      "6. None of them\n7. Hitch\n8. The Leaders of Celestial Prime\n9. Humans did it to start a war")
choice = valid_number2(1, 9)
if choice == 1:
    print("YOU SOLVED THE MYSTERY! Congratulations, Golden Ticket is now your ship and you"
          "are paid ^1,000,000 Docans for stopping an entire war between Galaxies.\n"
          "The authorities are headed there now to arrest her and get the moon back in\n"
          "orbit around the Earth.")
    clear_screen()
    print("[YOU HEAD OFF FOR A MUCH NEEDED VACATION]")
    clear_screen()
    add_image('alien_landscape.jpg', 1300, 750, 0, 0, 3)
    if in_love:
        clear_screen()
        print("[HOWEVER, A DEEP SENSE OF REGRET COMES OVER YOU. YOU KNOW THAT ALIEN 2 WAS YOUR SOULMATE.\n"
              "AND THAT YOU WILL NEVER SEE HER AGAIN...]")
else:
    print("OOOOOh. I'm so sorry. You don't quite have enough evidence for that to be the thief.")
    clear_screen()
    print("[IN THE COMING MONTHS YOU WATCH ANDROMEDA AND THE MILKY WAY GALAXIES GO TO WAR]")
    clear_screen()
    print("[THE TIMES OF CHAOS AND DESTRUCTION FALL UPON YOU AND EVERYONE ELSE]")
    clear_screen()
    print("[AND YOU HAVEN'T EVEN YOUR OWN SHIP TO ESCAPE IT]")
    clear_screen()
    print("[YOU HAVE LOST THE GAME AND, MORE IMPORTANTLY, LOST MILLIONS OF LIVES]")
    clear_screen()
    add_image('earth_sun.jpg', 1000, 550, 0, 0, 3)
    add_image('spacewar.jpg', 1050, 650, 0, 0, 3)

print("THE END")
print("THE CREATORS:\n* Karis Land\n* Amy Siemer\n* Max Kurts\n* Amar Ljubovic\n* Alli Nichols")
print("Thank you for playing CASED CLOSED")
