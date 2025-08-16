import random

# Word bank
word_bank = [
    # Animals
    "tiger", "lion", "elephant", "giraffe", "monkey", "zebra", "panda", "kangaroo", "crocodile", "dolphin", "shark", "whale",
    "penguin", "ostrich", "parrot", "eagle", "peacock", "sparrow", "butterfly", "cheetah", "wolf", "bear",
    # Countries & Cities
    "bangladesh", "india", "pakistan", "nepal", "bhutan", "sri lanka", "china", "japan", "korea", "canada",
    "brazil", "argentina", "italy", "france", "germany", "spain", "portugal", "australia", "new zealand",
    "london", "paris", "berlin", "dhaka", "tokyo", "beijing",
    # Sports
    "cricket", "football", "basketball", "tennis", "hockey", "rugby", "baseball", "golf", "boxing", "wrestling",
    # Fruits & Foods
    "apple", "banana", "mango", "pineapple", "grape", "orange", "strawberry", "watermelon", "cherry", "guava",
    "papaya", "lemon", "coconut", "peach", "pear", "plum", "kiwi", "fig", "dragonfruit",
    # Colors
    "red", "blue", "green", "yellow", "purple", "violet", "indigo", "black", "white", "orange", "brown", "silver", "gold",
    # Random things
    "computer", "internet", "python", "programmer", "developer", "keyboard", "mouse", "monitor", "laptop",
    "book", "story", "school", "university", "teacher", "student", "friend", "family", "superman", "batman",
    "ironman", "spiderman", "thor", "hulk", "captain", "avengers", "marvel", "dc"
]

# Hangman ASCII art for different stages
HANGMAN_ART = [
    """
      ------
      |    |
           |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
           |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
           |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
    =========
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
           |
    =========
    """
]

def play_hangman():
    # Check if word bank is empty
    if not word_bank:
        print("Error: Word bank is empty!")
        return

    # Pick random word
    word = random.choice(word_bank).lower()
    guessed = ["_" if char.isalpha() else char for char in word]
    attempts = 6  # Reduced to 6 to match hangman art stages
    used_letters = set()

    # Get player name
    try:
        name = input("Enter Your Name: ").strip()
        if not name:
            name = "Player"
    except EOFError:
        name = "Player"

    print(f"\nWelcome {name} to HANGMAN!")
    print("#" * 50)
    print(f"You have {attempts} attempts to guess the word.\n")

    # Game loop
    while attempts > 0 and "_" in guessed:
        # Display current state
        print(HANGMAN_ART[6 - attempts])  # Show hangman art based on remaining attempts
        print("Word: ", " ".join(guessed))
        print("Used letters:", ", ".join(sorted(used_letters)) or "None")
        print(f"Remaining Attempts: {attempts}")

        # Get guess
        try:
            guess = input("Guess a letter: ").lower().strip()
            if not guess:
                print("❌ Please enter a letter.\n")
                continue
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Enter a single valid letter.\n")
                continue
            if guess in used_letters:
                print("⚠️ You already guessed that letter.\n")
                continue

            used_letters.add(guess)

            # Check if guess is correct
            if guess in word:
                for i, char in enumerate(word):
                    if char == guess:
                        guessed[i] = guess
                print("✅ Good guess!\n")
            else:
                attempts -= 1
                print("❌ Wrong guess!\n")
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Exiting...")
            return

    # Final result
    print(HANGMAN_ART[6 - attempts])
    print("Word: ", " ".join(guessed))
    if "_" not in guessed:
        print(f"🎉 Congratulations, {name}! You guessed the word: {word}")
    else:
        print(f"💀 Game Over! The word was: {word}")

    # Ask to play again
    try:
        play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
        if play_again.startswith('y'):
            print("\n" + "#" * 50 + "\n")
            play_hangman()
    except (EOFError, KeyboardInterrupt):
        print("Thanks for playing!")

# Run the game
play_hangman()