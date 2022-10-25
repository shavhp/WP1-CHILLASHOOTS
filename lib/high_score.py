def get_high_score():
    # Default high score
    high_score = 0

    # Try to read high score from file
    try:
        high_score_file = open("/high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There is a file, but we don't understand the number
        print("I'm confused. Starting with no high score.")

    return high_score

def save_high_score(new_high_score):
    try:
        # Write file to disk
        high_score_file = open("/high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Can't write it
        print("Unable to save high score.")

def main():
    ''' Main program here '''
    # Get high score
    high_score = get_high_score()

    # Get score from current game
    current_score = 0
    try:
        # Ask user for their score
        current_score = int(input("What is your score?"))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")

    # See if we have a new high score
    if current_score > high_score:
        # There is a new high score, save to disk
        print("Congrats! New high score!")
        save_high_score(current_score)
    else:
        print("Try again?")

# Call main function, start the game
if __name__ == "__Chillashoots__":
    main()