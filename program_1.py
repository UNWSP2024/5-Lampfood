#Elliott Morris, 1/29/2026, Kilometer Converter
#this program asks the user to enter a kilometer value and converts it to miles

def kilometer_conversion(kilometers):
    miles = 0.0
    miles = kilometers * 0.6214

    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    print('in main')
    #get user input
    kilometers = float(input('Enter kilometers: '))
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    miles = kilometer_conversion(kilometers)
    #display user input
    print(f"{kilometers} kilometers is {miles:.4f} miles") #uses an f string to display
