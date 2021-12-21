# Objective: to read through the string input and create a list of strings correspondent to
# the characters of the string input

# import the pandas library
import pandas

# read the file as a pandas object with the csv read method
data = pandas.read_csv("./nato_phonetic_alphabet.csv")

# create a new dictionary to store the letters as keys and the strings as values
EncoderDict = {}

# loop through the pandas object with the "iterrows" method to get hold of the "letter"
# to be stores as a key, and the "code" to be stored as the corresponding value

# 1: standard method with a for loop
for (index, row) in data.iterrows():
  EncoderDict[row.letter] = row.code

# 2: dictionary comprehension method
EncoderDict2 = {row.letter: row.code for (index, row) in data.iterrows()}

# now get the input name from the user
# make the input uppercase for functionality purposes
user_input = input("Enter your name: ").upper()

# now create a new list to store the result
# 1: standard method with a for loop
result = []
for letter in user_input:
  result.append(EncoderDict[letter])

# 2. list comprehension method
result2 = [EncoderDict2[letter] for letter in user_input]

print(result)
print(result2)
