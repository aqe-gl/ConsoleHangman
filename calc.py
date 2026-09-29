from random import choice
words = ["chicken", "banana", "lemonade", "television", "drink", "stupid"]

print("GUESS THE WORD")
print("One letter at a time ")

word = choice(words)
length = len(word)

tries = 5
censored = ''
for i in range(length):
        censored += '*'

print(censored)
solved = False
while not solved:
    print(f"Tries: {tries}")
    guess = input("Enter a letter from the word: ")
    if len(guess) > 1 or guess == "":
        print("Invalid input")
        continue
    lst = list(censored)
    for i in range(length):
        if word[i] == guess:
            lst[i] = guess
    censored = "".join(lst)
    print(censored)
    print()
    if guess in word:
        print("correct")
        #lst = list(censored)
        for i in range(length):
            if word[i] == guess:
                lst[i] = guess
        censored = "".join(lst)
        print(censored)
    else:
        print("incorrect")
        tries -= 1
        if tries <= 0:
            print("Game over")
            break
    print()
    for i in range(len(censored)):
        if '*' in censored:
            continue
        else:
            print("win")
            solved = True
            ask = input("Play again? y/n: ")
            if ask.lower() == 'y':
                solved = False
                tries = 5
                word = choice(words)
                length = len(word)

                censored = ''
                for i in range(length):
                    censored += '*'
                print(censored)
            elif ask.lower() == 'n':
                print("Thank you for playing")
                solved = True
            break
