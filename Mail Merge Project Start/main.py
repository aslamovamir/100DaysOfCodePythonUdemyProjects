# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# First, we will get the contents of the starting letter template and save it in a variable locally
# open the file "starting_letter.txt"
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

print(letter)

# Second,we will fetch the contents of the files with the names listed and store them
# in an array locally
# open the file "invited_names.txt", read line by line, and append the names to a list
data = []
with open("./Input/Names/invited_names.txt") as file:
    data = file.readlines()

print(data)
# now we will loop through the data and trim each name, removing any whitespaces,
# and store them in a different list
names = []
for item in data:
    names.append(item.strip())

print(names)

# Third, we will loop through the list of names, and at each iteration, we will modify
# the starting letter with the replaced name, create a new file with the name of the person as
# the name if this file, and write the modified letter onto it
for name in names:
    # modify the letter
    new_letter = letter.replace('[name]', name, 1)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode = 'w') as file:
        file.write(new_letter)
