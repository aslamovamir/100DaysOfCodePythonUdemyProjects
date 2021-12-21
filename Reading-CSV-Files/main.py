# The project demonstrates the three ways Python can open and read csv files
# The first way is the built-in open method in python library
# The second way is to use the csv library installed with Python
# The Third way is with the use of the Pandas library not installed with Python
# The last way requires the installation of the Pandas package

# First Way
open the file "data.csv" and put the data in a list
with open("./data.csv") as csv_file:
    csv_data = csv_file.readlines()

# Second Way
# import csv
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

data = pandas.read_csv("./data.csv")
print(data["temp"])
