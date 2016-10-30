# name       : Arun Mohan
# email      : arm198@pitt.edu
# date       : 10/28/16
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Take home assignment 2

# Here I define the two functions that I need to use

# This function accepts the name of a file and returns how many lines it has
# and the sum of all the distance of the file
def processFile(fh):
    pd = 0                          # variable for partial distance
    ptn = 0                         # variable for partial # of lines
    fo = open(fh, 'r')              # opening the file that the user inputs to be read
    for line in fo:                 # loop that reads through each line of the file
        ptn += 1                    # adds one to the partial line count for each line
        line = line.rstrip('\n')    # removes the \n from the end of each line
        temp = line.split(",")      # splits the line by the comma to create a list with two values
        dist = float(temp[1])       # creates a variable that takes the second value in the list, the distance
        pd += dist                  # adds the distance from each line to the partial distance
    return ptn, pd                  # returns the two values we need, partial distance and # of lines

# This function accepts two arguments to print all the information in the correct format
def printKV(key, value, klen = 0):
    kl = max(len(key), klen)        # assigns a variable to the length of the key or the key length variable
    if isinstance (value, str):     # checks data type of value and assigns variable to the correct format value
        fs = "20s"
    elif isinstance (value, float):
        fs = "10.3f"
    else:
        fs = ""
    print(format(key, str(kl) + "s"))   # prints the info with the correct formatting
    print(format(value, fs))

td = 0
tnl = 0
file = input("Please provide the file name :")
while (file and file != "quit" and file != "q"):
    file_object = open(file, "r")
    print("File read: ", file)
    number_of_lines, total_distance = processFile(file_object)
    printKV("Partial Total # of lines:", number_of_lines)
    printKV("Partial distance run", total_distance)
    file_object.close()
    td += total_distance
    tnl += number_of_lines
printKV("Total # of lines:", number_of_lines)
printKV("Total distance run", total_distance)