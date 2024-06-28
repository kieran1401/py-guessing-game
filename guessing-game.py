# our secret word for the game
secret_word = "panda"

# variable to store the users guesses, count, and limit
guess = ""
guess_count = 0
guess_limit = 9

# if it goes to true, they are out the game
out_of_guesses = False

print("Welcome to my guessing game. You have 9 guesses or you lose, good luck!")

# Keeps looping as long as the user DOESNT guess the secret_word and they arent out of guesses (true). guess.lower() allows the user to type panda or Panda
while guess.lower() != secret_word and not (out_of_guesses):
    # as long as guess_count, is less than the limit (9), then user can have another guess
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1

        # provides a hint if guess_count reaches 3
        if guess_count == 3:
            print("Hint: It's a big animal!")

        if guess_count == 6:
            print("Last Hint: This animal is black and white and very clumsy!")

    # if guess_count reaches limit, out_of_guesses changes to true
    else:
        out_of_guesses = True

# outcome after the loop (if out_of_guesses becomes True, IF will print)
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win, you guessed the word! Panda Panda Panda")
