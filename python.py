import random  # Import the random module to use for selecting a random word

# Get the player's name as input and greet them
name = input("What is your name? ")
print("Good Luck !", name)

# List of possible words for the game
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Randomly select a word from the list for the player to guess
word = random.choice(words)

# Inform the player about the start of the guessing game
print("Guess the characters")

guesses = ''  # Variable to store all guessed characters
turns = 12    # Number of turns or attempts the player has

# Loop until the player runs out of turns or guesses the word
while turns > 0:

    failed = 0  # Counter to track characters yet to be guessed

    # Loop through each character in the chosen word
    for char in word:
        # Check if the character is one of the player's guesses
        if char in guesses:
            print(char, end=" ")  # If guessed correctly, display the character
        else:
            print("_", end=" ")   # If not, display an underscore
            failed += 1           # Increment the failed counter

    # If failed is 0, all characters have been guessed correctly
    if failed == 0:
        print("\nYou Win")               # Inform the player they won
        print("The word is:", word)      # Display the correctly guessed word
        break                            # End the game

    print()  # Print a newline for readability

    # Prompt the player to guess a character
    guess = input("Guess a character: ")

    guesses += guess  # Add the guessed character to the guesses string

    # If the guessed character is not in the word
    if guess not in word:
        turns -= 1  # De
