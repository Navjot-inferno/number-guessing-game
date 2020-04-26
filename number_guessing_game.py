# import modules.
import random  # used for generating random number that to be guessed.

while True:  # using while loop for replaying the game for infinite times
    # creating an input value to choose type of game that is stored in a variable named 'options'.
    options = str(input("""choose type of game:  
    1)'9' umber game(X) 
    2)'25' number game(Y) 
    >>> """)).upper()  # str() used to convert the value in a string, .upper() used to convert input value in uppercase.


    # separating the codes of the two types of games using if-elif statements .
    if options == "X":  # assigning the if condition for the input value of the variable(options) for first '9' number game.

        secret_number = random.randint(0, 9)  # a random integer from 0 to 9 is taken by random module as a secret number that is stored in variable 'secret_number'.

        tries = 0  # assigning value to variable 'tries' that further used for guessing_chances in game.

        while tries < 3:  # starting a while loop with giving/assigning chances(3) to guess in game.

            guessed_number = int(input("guess a number b/w 0-9: "))  # taking input from user for guessed number and storing in variable(guessed_number).

            if guessed_number == secret_number:   # assigning the if condition for the write guess.
                print("yeah! You won")
                break      # using break statement for ending game after write guess.

            elif guessed_number > secret_number:   # assigning the elif condition for the higher guess.
                print("you have guessed a higher number")

            elif guessed_number < secret_number:   # assigning the elif condition for the lower guess.
                print("you have guessed a lower number")

            tries += 1  # conditions of wrong guesses, this states that after each guess the value of 'tries' will be increased by 1.

        if not tries < 3:  # making condition for wrong guesses all the time.
            print('sorry you failed to guess, the number is:  ' + str(secret_number))  # str() here used to convert variable(secret_number) to string for to be printed.


    elif options == "Y":   # assigning the elif condition for the input value of the variable(options) for first '25' number game.

        secret_number = random.randint(0, 25)  # a random integer from 0 to 25 is taken by random module as a secret number that is stored in variable 'secret_number'.

        tries = 0  # assigning value to variable 'tries' that further used for guessing_chances in game.

        while tries < 5:  # starting a while loop with giving/assigning chances(5) to guess in game.

            guessed_number = int(input("guess a number b/w 0-25: "))  # taking input from user for guessed number and storing in variable(guessed_number).

            if guessed_number == secret_number:  # assigning the if condition for the write guess.
                print("yeah! You won")
                break  # using break statement for ending game after write guess.

            elif guessed_number > secret_number:  # assigning the elif condition for the higher guess.
                print("you have guessed a higher number")

            elif guessed_number < secret_number:  # assigning the elif condition for the lower guess.
                print("you have guessed a lower number")

            tries += 1  # conditions of wrong guesses, this states that after each guess the value of 'tries' will be increased by 1.

        if not tries < 5:  # making condition for wrong guesses all the time.
            print('sorry you failed to guess, the number is:  ' + str(secret_number))  # str() here used to convert variable(secret_number) to string for to be printed.
