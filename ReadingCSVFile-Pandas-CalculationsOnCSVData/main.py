# read the data with the Pandas library
import pandas

# get the pandas object of type dataframe
data = pandas.read_csv("./data.csv")

# get the rows of data only for the color of Gray
DataGray = data[data.PrimaryFurColor == 'Gray']
freqGray = DataGray.HectareSquirrelNumber.to_list()
freqTotalG = sum(freqGray)

# get the rows of data only for the color of Cinnamon
DataCinnamon = data[data.PrimaryFurColor == 'Cinnamon']
freqCinnamon = DataCinnamon.HectareSquirrelNumber.to_list()
freqTotalC = sum(freqCinnamon)

# get the rows of data only for the color of Black
DataBlack = data[data.PrimaryFurColor == 'Black']
freqBlack = DataBlack.HectareSquirrelNumber.to_list()
freqTotalB = sum(freqBlack)

# create dataframe (Dictionary) from scratch
# Note: keys of the Dictionary are columns, and the values [list of strings, nums]
# are the corresponding column data
newData = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [freqTotalG, freqTotalC, freqTotalB]
}

# convert Python data to Pandas dataframe object
pandasObj = pandas.DataFrame(newData)
print(pandasObj)

# save the pandas dataframe object to a CSV file
# the parameter of the method takes in the path and the name of the file
pandasObj.to_csv('./New Data')
