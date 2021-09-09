import art
import random


def approximator(guess, number):

    if guess > number:
        print("The number you guessed is too big!")
    elif guess < number:
        print("The number you guessed is too small!")



def game():

    stop = True
    print(art.logo)
    print("I have a number between 1 and 100 in mind!" )
    while (stop):
        difficulty = input("What difficulty level would you like to play at? 'easy' or 'hard'?: ").lower()

        progression = True

        if difficulty == 'easy':
            stop = False
            print(f"\nThe difficulty level you chose: {difficulty.title()}")
            lives_left = 10
            print(f"Lives you have to guess the right number: {lives_left}")
            number = random.randint(1, 100)
            # print(f"HINT: {number}")

            while(progression):
                while lives_left != 0:
                    guess = int(input("Guess a number (To quit enter: -1): "))

                    if guess == -1:
                        print("Quitting the game...")
                        progression = False
                        stop = False

                        wish_to_play = input("Would you like to play the Guess Game again? ('yes' or 'no'): ").lower()
                        if wish_to_play == 'yes':
                            game()
                        else:
                            print("\nGoodbye!")
                            lives_left = 0
                            break

                    elif guess == number:
                        print(f"\nCongratulations! You guessed it right! The right number: {number}!")
                        progression = False
                        stop = False

                        wish_to_play = input("Would you like to play the Guess Game again? ('yes' or 'no'): ").lower()
                        if wish_to_play == 'yes':
                            game()
                        else:
                            print("\nGoodbye!")
                            lives_left = 0
                            break

                    else:
                        lives_left -= 1
                        if lives_left == 1 or lives_left == 0:
                            print(f"Incorrect guess! The life remaining: {lives_left}")
                            approximator(guess, number)
                        else:
                            print(f"\nIncorrect guess! The lives remaining: {lives_left}")
                            approximator(guess, number)
                        if lives_left == 0:
                            print(f"\nGame Over! You have wasted the lives! The right number: {number}!")

                            progression = False
                            stop = False

                            wish_to_play = input("Would you like to play the Guess Game again? ('yes' or 'no'): ").lower()
                            if wish_to_play == 'yes':
                                game()
                            else:
                                print("\nGoodbye!")
                                lives_left = 0
                                break

        elif difficulty == 'hard':
            stop = True
            print(f"\nThe difficulty level you chose: {difficulty.title()}")
            lives_left = 5
            print(f"Lives you have to guess the right number: {lives_left}")
            number = random.randint(1, 100)
            # print(f"\nHINT: {number}")

            while (progression):
                while lives_left != 0:
                    guess = int(input("Guess a number (To quit enter: -1): "))

                    if guess == -1:
                        print("Quitting the game...")
                        progression = False
                        stop = False

                        wish_to_play = input("Would you like to play the Guess Game again? ('yes' or 'no'): ").lower()
                        if wish_to_play == 'yes':
                            game()
                        else:
                            print("\nGoodbye!")
                            lives_left = 0
                            break


                    elif guess == number:
                        print(f"\nCongratulations! You guessed it right! The right number: {number}!")

                        progression = False
                        stop = False

                        wish_to_play = input("Would you like to play the Guess Game again? ('yes' or 'no'): ").lower()
                        if wish_to_play == 'yes':
                            game()
                        else:
                            print("\nGoodbye!")
                            lives_left = 0
                            break

                    else:
                        lives_left -= 1
                        if lives_left == 1 or lives_left == 0:
                            print(f"Incorrect guess! The life remaining: {lives_left}")
                            approximator(guess, number)
                        else:
                            print(f"\nIncorrect guess! The lives remaining: {lives_left}")
                            approximator(guess, number)
                        if lives_left == 0:
                            print(f"\nGame Over! You have wasted the lives! The right number: {number}!")

                            progression = False
                            stop = False

                            wish_to_play = input("Would you like to play the Guess Game again? ('yes' or 'no'): ").lower()
                            if wish_to_play == 'yes':
                                game()
                            else:
                                print("\nGoodbye!")
                                lives_left = 0
                                break

        else:
            print("\nInvalid entry! Let's try again.")




wish_to_play = input("Would you like to play Guess Game? ('yes' or 'no'): ").lower()
if wish_to_play == 'yes':
    game()
else:
    print("\nGoodbye!")
