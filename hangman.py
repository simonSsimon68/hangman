from generate_word import generate_word

used_letters = ""
word = generate_word().strip()
dis = ""
max_attempts = 6
attempts = max_attempts
correct_letters_g = 0
iterations = 0

print("Welcome to hangman.")
print("You have " + str(max_attempts) + " attempts to guess the right word. Providing a wrong letter makes you lose an "
                                        "attempt")
print("Here is your word: ")

for letter in word:
    dis = dis + " _ "

temp = list(dis)
print(dis)

while 1:
    dis = list(dis)

    guess = input("Please enter your guess: ")

    if len(list(guess)) > 1:
        print("Please enter a single letter\n")
        continue
    elif guess.isdigit():
        print("Please enter a letter\n")
        continue
    elif guess.lower() not in used_letters:
        if iterations == 0:
            used_letters = used_letters + guess
        else:
            used_letters = used_letters + ", " + guess
    else:
        print("That letter has already been guessed, try another\n")
        continue
    print("")

    correct_letters = 0
    i = 0

    for letter in word:
        if guess.lower() == letter.lower():
            k = 0
            c = 0
            for char in temp:
                if char == "_":
                    if k == i:
                        dis[c] = letter
                    k += 1
                c += 1

            correct_letters += 1
            correct_letters_g += 1
        i += 1

    if correct_letters == 0:
        attempts += -1

    dis = "".join(dis)

    if dis.replace(" ", "") == word.replace(" ", ""):
        print(dis)
        print("Congrats, you have guess the word: " + word)
        break
    if attempts == 0:
        print("\nSorry, you have ran out of attempts")
        print("The answer is: " + word)
        break

    if correct_letters_g == 1:
        print("You have guessed " + str(correct_letters_g) + " letter right")
    else:
        print("You have guessed " + str(correct_letters_g) + " letters right")
    print("You have " + str(attempts) + " attempts left")
    print("Your guesses: " + used_letters)
    print(dis + "\n")
    iterations += 1
