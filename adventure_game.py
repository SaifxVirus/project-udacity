# Import the necessary modules
import time
import random

# Function for the field scenario
def field(item, option, score):
    print("Enter 1 to get back to the room.")
    time.sleep(1)
    print("Enter 2 to go downstairs.")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            score = room(item, option, score)
            break
        elif choice1 == "2":
            score = downstairs(item, option, score)
            break
    return score

# Function to display the game introduction
def intro(item, option):
    print("you wake up in the middle of the night.\n")
    time.sleep(1)
    print("you hear noises downstairs.\n")
    time.sleep(1)
    print("you are trying to get to your shotgun but something is moving in front of your bedroom door.\n")
    time.sleep(1)
    print("you grab your pocket knife.\n")
    time.sleep(1)
    print("you got up from the bed and stand behind the door.\n")
    time.sleep(1)
# Function for the room scenario
def room(item, option, score):
    print("\nYou get to the door.")
    time.sleep(1)
    print("\nThe door is opened, and a " + option + " is inside your room.")
    time.sleep(1)
    print("\nThe " + option + " attacks you!\n")
    time.sleep(1)
    if "shatgun" not in item:
        print("You try to use the pocket knife, but the " + option + " throws it away.\n")
        time.sleep(1)
    while True:
        choice2 = input("Would you like to (1) save your house or (2) run away?")
        if choice2 == "1":
            if "shatgun" in item:
                print("\nAs the " + option + " attacks you, you shoot it with your gun.")
                time.sleep(1)
                print("\nIt gets injured and jumps out of the window.")
                time.sleep(1)
                print("\nThe " + option + " never comes back!")
                time.sleep(1)
                print("\nYou are victorious!\n")
                time.sleep(1)
                score += 20  # Increase the score for defeating the enemy
            else:
                print("\nYou do your best...")
                time.sleep(1)
                print("but your knife is no match for the " + option + ".")
                time.sleep(1)
                print("\nYou have died!\n")
                time.sleep(1)
                score -= 10  # Decrease the score for being defeated
            return score
        if choice2 == "2":
            print("\nYou stand behind the door.\n")
            time.sleep(1)
            return 0  # Return a default score value of 0 if the player runs away without finding the shotgun
        

# Function for downstairs
def downstairs(item, option, score):
    if "shatgun" in item:
        print("\nYou open the door.")
        time.sleep(1)
        print("\nYou remember that you went down.")
        time.sleep(1)
        print("\nYou walk back to the room.\n")
        time.sleep(1)
    else:
        print("\nYou open the door.")
        time.sleep(1)
        print("\nyou are sprinting to get your shotgun.")
        time.sleep(1)
        print("\nyou get it and load it.")
        time.sleep(1)
        print("\nYou put your knife in your pocket.")
        time.sleep(1)
        print("\nYou walk back up to the room.\n")
        time.sleep(1)
        item.append("shatgun")
        score += 15  # Increase the score for finding the shotgun
    return field(item, option, score)
    

# Function to ask the player if they want to play again
def play_again():
    while True:
        choice = input("Would you like to play again? (y/n) ")
        time.sleep(1.5)
        if choice.lower() == "y":
            print("\n\n\nRestarting the game ...\n\n\n")
            time.sleep(1.5)
            return True
        elif choice.lower() == "n":
            print("\n\n\nThanks for playing.\n\n\n")
            time.sleep(1.5)
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Function to start a new game session
def play_game():
    item = []
    option = random.choice(["Witch", "psychopath", "slenderman"])
    intro(item, option)
    score = 0 # Initialize the score to 0
    score = field(item, option, score)  # Update the score with the returned value
    return score

# Main function to run the game
def main():
    scores = []  # List to store scores
    while True:
        score = play_game()
        scores.append(score)
        total_score = sum(scores)
        print("\nYour total score: " + str(total_score))
        if not play_again():
            break

# Start the game
main()
