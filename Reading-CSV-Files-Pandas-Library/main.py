# The project demonstrates the three ways Python can open and read csv files
# The first way is the built-in open method in python library
# The second way is to use the csv library installed with Python
# The Third way is with the use of the Pandas library not installed with Python
# The last way requires the installation of the Pandas package

# First Way
# open the file "data.csv" and put the data in a list
with open("./data.csv") as csv_file:
    csv_data = csv_file.readlines()

# Second Way
import csv
with open("./data.csv") as csv_file:
    csv_data = csv.reader(csv_file)
    temperatures = []
    for row in csv_data:
        if row[1] == 'temp':
            continue
        temperatures.append(int(row[1]))

print(temperatures)

# Third Way
import pandas
# get the pandas object of type "DataFrame"
data = pandas.read_csv("./data.csv")
print(type(data))
print(data["temp"])

# Convert the object to Python Dictionary
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Calculating the average temperature in the data

# Python way
avr_temp = sum(temp_list)/len(temp_list)
print(avr_temp)

# Pandas way
print(data["temp"].mean())

# Finding the max value in the data series
# Pandas way
print(data["temp"].max())

# Get Data in Columns
# Python way
print(data['condition'])
# Pandas way
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


# Getting separate info of a row
monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp * 9/5 + 32)
print(monday_temp)

# Create a dataframe from scratch
data_dict2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# Convert Python data to Pandas dataframe object
data2 = pandas.DataFrame(data_dict2)
print(data2)

# Save the Pandas dataframe object to a CSV file
# the parameter of the method takes in the path and name of the file
data2.to_csv("new_data.csv")
