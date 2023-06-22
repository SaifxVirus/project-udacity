# Import the necessary modules
import time
import random

# Function to print a message and add a pause
def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(1.5)

# Function to display the game introduction
def intro(item, option):
    print_pause("you wake up in the middle of the night.\n")
    print_pause("you hear noises down stairs.\n")
    print_pause("you are trying to get to your shotgun but something is moving in front of your bedroom door.\n")
    print_pause("you grap your pocket knife.\n")
    print_pause("you got up from the bed and stand behind the door.\n")

# Function for the door
def downstairs(item, option, score):
    if "shatgun" in item:
        print_pause("\nYou open the door.")
        print_pause("\nYou remember that you went down .")
        print_pause("\nYou walk back to the room.\n")
    else:
        print_pause("\nYou open the door.")
        print_pause("\nyou are sprinting to get your shotgun.")
        print_pause("\nyou get it and load it.")
        print_pause("\nYou put youe knife in your pocket.")
        print_pause("\nYou walk back up to the room.\n")
        item.append("shatgun")
        score += 15  # Increase the score for finding the shotgun
    field(item, option, score)

# Function for the room scenario
def room(item, option, score):
    print_pause("\nYou get to the door.")
    print_pause("\nthe door is opened, and a " + option + " is inside your room.")
    print_pause("\nThe " + option + " attacks you!\n")
    if "shatgun" not in item:
        print_pause("You trying to use the pocket knife and " + option + " threw it away.\n")
    while True:
        choice2 = input("Would you like to (1) save your house or (2) run away?")
        if choice2 == "1":
            if "shatgun" in item:
                print_pause("\nAs the " + option + " attacks you, you shoot it your gun.")
                print_pause("\nHe get's injured and jumps from the window.")
                print_pause("\nThe " + option + "  never came bake!")
                print_pause("\nYou are victorious!\n")
                score += 20  # Increase the score for defeating the enemy
            else:
                print_pause("\nYou do your best...")
                print_pause("but your knife is no match for the " + option + ".")
                print_pause("\nYou have been died!\n")
                score -= 10  # Decrease the score for being defeated
            play_again(score)
            break
        if choice2 == "2":
            print_pause("\nYou sleep again  , you feel Happy for saving the house.\n")
            field(item, option, score)
            break

# Function for the field scenario
def field(item, option, score):
    print_pause("Enter 1 to get back to the room.")
    print_pause("Enter 2 to to go down stairs.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            room(item, option, score)
            break
        elif choice1 == "2":
            downstairs(item, option, score)
            break

# Function to calculate the total score
def calculate_total_score(scores):
    total_score = sum(scores)
    return total_score

# Function to ask the player if they want to play again
def play_again(score):
    print("Your score: " + str(score))
    while True:
        choice = input("Would you like to play again? (y/n) ")
        if choice.lower() == "y":
            print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
            return True
        elif choice.lower() == "n":
            print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Main function to run the game
def main():
    scores = []  # List to store scores
    while True:
        score = play_game()
        scores.append(score)
        total_score = calculate_total_score(scores)
        print("\nYour total score: " + str(total_score))
        if not play_again(total_score):
            break

# Function to start a new game session
def play_game():
    item = []
    option = random.choice(["Witch", "phsycopath", "slenderman"])
    score = 0  # Initialize the score to 0
    intro(item, option)
    field(item, option, score)
    return score

# Start the game
main()
