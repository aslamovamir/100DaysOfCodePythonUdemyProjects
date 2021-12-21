# Objective: To read two files in the directory of the main file and fetch the data from the files.
#            To create a new list of numbers common in both of the files
#            To create a new file txt with the common data in the same directory as the main file


# open the file 1 and store the lines in a list
with open('./file1.txt') as file1:
  file1_content = file1.readlines()

print(file1_content)

# open the file 2 and store the lines in a list
with open('./file2.txt') as file2:
  file2_content = file2.readlines()

# convert the two lists to numbers in two new lists
# list comprehension method
file1_nums = [int(num.strip()) for num in file1_content]
file2_nums = [int(num.strip()) for num in file2_content]

print(file1_nums)
print(file2_nums)

# now combine the two lists into one list with the nums common to both the lists
result = [num for num in file1_nums if num in file2_nums]

print(result)

# now create a new file the obtained data
# create a new file object with the action of "write"
new_file_obj = open("new_file.txt", "w")
# write the result in str form to the file opened by the file object
for num in result:
  new_file_obj.write(str(num) + '\n')
# close the file object
new_file_obj.close()
