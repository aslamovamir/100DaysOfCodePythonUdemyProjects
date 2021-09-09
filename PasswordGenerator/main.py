#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
difficulty_level = int(input("If you want the order of characters not randomized, type '0', otherwise type '1' if you want the order randomized: "))
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if difficulty_level == 0:
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password = list()

    for i in range(nr_letters):
        rand_index = random.randint(0, len(letters) - 1)
        password.append(letters[rand_index])
    for i in range(nr_symbols):
        rand_index = random.randint(0, len(symbols) - 1)
        password.append(symbols[rand_index])
    for i in range(nr_numbers):
        rand_index = random.randint(0, len(numbers) - 1)
        password.append(numbers[rand_index])


    password = ''.join(password)
    print(f"Password with the order of characters not randomized: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
elif difficulty_level == 1:

    password = list()
    ingredients = [letters, numbers, symbols]
    total_ingredients = nr_letters + nr_numbers + nr_symbols
    letters_used = 0
    numbers_used = 0
    symbols_used = 0


    for i in range(total_ingredients):
        while(True):
            rand_index = random.randint(0, 2)
            # print("RANDOM CHOICE INITIAL: " + str(rand_index))
            if rand_index == 0:
                if letters_used != nr_letters:
                    letters_used += 1
                    break
                elif letters_used == nr_letters:
                    continue
            elif rand_index == 1:
                if numbers_used != nr_numbers:
                    numbers_used += 1
                    break
                elif numbers_used == nr_numbers:
                    continue
            elif rand_index == 2:
                if symbols_used != nr_symbols:
                    symbols_used += 1
                    break
                elif symbols_used == nr_symbols:
                    continue

            # print(f"LETTERS USED: {letters_used} NUMBERS USED: {numbers_used} SYMBOLS USED: {symbols_used}")

        if (letters_used == nr_letters and numbers_used == nr_numbers and symbols_used == nr_symbols):
            rand_index = rand_index
            # print("IF - 1")
        elif (letters_used > nr_letters):
            # print("IF - 5")
            while (rand_index == 0):
                # print("CYCLE")
                rand_index = random.randint(0, 2)
                if (rand_index == 1):
                    if numbers_used == nr_numbers:
                        continue
                elif (rand_index == 2):
                    if symbols_used == nr_symbols:
                        continue
                # print("RAND: " + str(rand_index))
            if rand_index == 1:
                if numbers_used != nr_numbers:
                    numbers_used += 1
            elif rand_index == 2:
                if symbols_used != nr_symbols:
                    symbols_used += 1
        elif (numbers_used > nr_numbers):
            # print("IF - 6")
            while (rand_index == 1):
                # print("CYCLE")
                rand_index = random.randint(0, 2)
                if (rand_index == 0):
                    if letters_used == nr_letters:
                        continue
                elif (rand_index == 2):
                    if symbols_used == nr_symbols:
                        continue
                # print("RAND: " + str(rand_index))
            if rand_index == 0:
                if letters_used != nr_letters:
                    letters_used += 1
            elif rand_index == 2:
                if symbols_used != nr_symbols:
                    symbols_used += 1
        elif (symbols_used > nr_symbols):
            # print("IF - 7")
            while (rand_index == 2):
                # print("CYCLE")
                rand_index = random.randint(0, 2)
                if (rand_index == 0):
                    if letters_used == nr_letters:
                        continue
                elif (rand_index == 1):
                    if numbers_used == nr_numbers:
                        continue
                # print("RAND: " + str(rand_index))
            if (rand_index == 0):
                if letters_used != nr_symbols:
                    letters_used += 1
            elif (rand_index == 1):
                if numbers_used != nr_numbers:
                    numbers_used += 1
                # print("RAND_INDEX AFTER THE IF BLOCKS: " + str(rand_index))

        if rand_index == 0:
            rand_inner = random.randint(0, len(letters) - 1)
        elif rand_index == 1:
            rand_inner = random.randint(0, len(numbers) - 1)
        elif rand_index == 2:
            rand_inner = random.randint(0, len(symbols) - 1)

        password.append(ingredients[rand_index][rand_inner])
    # print(password)
    password = ''.join(password)
    print(f"Password with the order of characters randomized: {password}")
