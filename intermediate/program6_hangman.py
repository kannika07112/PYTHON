# Program 6: Hangman game

word = "python"
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print(" ".join(guessed))
    ch = input("Guess a letter: ")
    
    if ch in word:
        for i in range(len(word)):
            if word[i] == ch:
                guessed[i] = ch
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("You won! Word:", word)
else:
    print("You lost! Word was:", word)
