

import math

# The variable represents the switch to run the program in a loop
key = 1

# Functions for collecting information
def myinput():
    choice = input('Please select the calculation type: (1-time calculation, 2-manpower calculation）')
    if choice == '1':
        size = float(input('Please enter the item size: (1 represents the standard size, please enter a decimal)'))
        number = int(input('Please enter the number of manpower: (please enter an integer)'))
        time = None
        return size,number,time
      
    if choice == '2':
        size = float(input('Please enter the item size: (1 represents the standard size, please enter a decimal)'))
        number = None
        time = float(input('Please enter the number of working hours: (please enter a decimal)'))
        return size,number,time
        

# Function to complete the calculation
def estimated(my_input):
    # Take out the data in the tuple
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    # Manpower calculation
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('The project size is %.1f standard projects. If it needs to be completed in %.1f working hours, the number of manpower required is: %d people' %(size,time,number)) 
    # Working hours calculation
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('The project size is %.1f standard projects, and if %d is used to complete the project, the number of working hours required is: %.1f' %(size,number,time))  

# Function that asks whether to continue
def again():
    # Declare the global variable key in order to modify the variable
    global key
    a = input('Do you want to continue to calculate? Please enter y to continue, and enter other keys to end the program. ')
    if a != 'y':
        # If the user do not enter'y', then assign the key to 0
        key = 0  

# The mian function
def main():
    print('Welcome to the workload calculator！')
    while key == 1:
        my_input = myinput()
        estimated(my_input)
        again()
    print('Thanks for using the workload calculator! ')

main()