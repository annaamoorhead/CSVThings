# main.py

from utilsPackage.utils import *

# Call the function and store what it returns 
# in a variable called dataSS

if __name__ == "__main__":
    data = read_CSV_file()
    # print the length of data
    # print the first and last element of data
    
    print("number of records read:", len(data))
    print(data[0])
    print(data[-1])
    
    # I want a List Comprehension expression that extracts the accident type
    # Edit List Comprehension to eliminate the blank accident
    myAccidentTypes = [row[6] for row in data]      # if len(row[6] > 0 could be used here
    myAccidentTypes = set(myAccidentTypes)    # Convert to set to remove duplicates
    myAccidentTypes.remove('')
    print(myAccidentTypes)
    
    #print the number of accidents with accidents type 1-Car
    print(len([row[6] for row in data if row[6]== "1-Car"]))
    print(len([row[4] for row in data if row[4]== "Weekday"]))
    
