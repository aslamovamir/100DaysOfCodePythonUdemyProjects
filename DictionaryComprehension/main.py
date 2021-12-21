# Objective to use the Dictionary Comphrehension method to create a dictionary of words 
# and their respective lengths as the values, and finally write the dictionary into 
# a new file


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# split the string into a list of strings
sentence_list = sentence.split()
print(sentence_list)

# create a new dictionary consisting of the words from the list as the keys and the length
# of the words as the values of the keys
result = {word: len(word) for word in sentence_list}

# write a new file and write the obtained result in that FileExistsError
with open("./new_file.txt", "w") as new_file:
  new_file.write(str(result))
