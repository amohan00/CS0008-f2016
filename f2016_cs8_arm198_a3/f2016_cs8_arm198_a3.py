#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: never assume that numebr of files and file size stay constants!!!
#


# Empty List to store the file names from the master file
file_names = []

# Variable to count the number of files
file_counter = 0

# Opening the master file
# MN: why not asking the user for the master list file name?
master_file = open("f2016_cs8_a3.data.txt", 'r')

# Loop to count the files in the master file and add the file names to the list
for header in master_file:
    # Adds one to the number of files
    file_counter += 1
    # Removes the new line character and adds the file name to the list
    file_names.append(header.rstrip('\n'))

# Closing the master file
master_file.close()

# Variable to count the total distance and number of lines
line_counter = 0
dist_total = 0

# Empty lists to hold all the distances and names
distances = []
people = []

# For loop to go through and open each file
for line in file_names:
    names = open(line, 'r')

    # For loop to go through each file line by line
    for row in names:
        # Splits each line by the comma and assigns the values to a list
        temp = row.split(',')
        # Removes the new line character from the distance and adds it to a list
        distances.append(temp[1].rstrip('\n'))
        # Removes the space from the names and adds them to a list
        people.append(temp[0].strip(' '))
        # Adds one to the line counter
        line_counter += 1
    # Closes the file
    names.close()

# Deleting the headers from each list
# MN: you are assuming that all your files have exactly 150 lines plus the header
#     what if the file change and has a differnt number of lines?
del distances[0], distances[150], distances[300], people[0], people[150], people[300]

# Calculating the total distance ran
# Variables for the index and the total distance
index = 0
total_distance = 0
# While loop that goes through every index of distances and adds the values
while index < len(distances):
    # Converts every distance to a float and adds to total
    total_distance += float(distances[index])
    # Adds one to the index
    index += 1

# Calculating who ran the furthest and least
# Variables for the max and min runners and distances
# MN: here you find the mac and min single distance, not the total distance run by the participants 
max_dist = max(distances)
min_dist = min(distances)
# Assigns which person has the index of the max and min distances
# MN: this method works as long as you do not have 2 participants with the same distance run
max_part = people[distances.index(max_dist)]
min_part = people[distances.index(min_dist)]

# Finding how many names repeat and total names
# Empty list and dictionary to count repeats
total_part = []
repeats = {}
# For loop to go through every name in the list
for stuff in people:

    # If statement to check for repeats
    if stuff not in total_part:
        # If this is the first time seeing the name, it is added to the list of all participants
        total_part.append(stuff)
    # MN: with the following 2 if blocks, you assume that the maximum repeats is 3
    #     what if you have a participant that has more than 3 records?
    #     Never assume anythin, always expect the exception to your assumtions
    elif stuff in total_part and stuff not in repeats:
        # If this is the second time, it is added to repeats with a value of 2
        repeats[stuff] = '2'
    elif stuff in total_part and stuff in repeats:
        # If this is the third time, it is added to repeats with a value of 3
        repeats[stuff] = '3'

# Printing all the information with the correct formatting
print("Number of Input files read   :", file_counter)
print("Total number of lines read   :", line_counter)
print("\ntotal distance run           :", total_distance)
print("\nmax distance run             :", max_dist)
print("  by participant             :", max_part)
print("\nmin distance run             :", min_dist)
print("  by participant             :", min_part)
print("\nTotal number of participants :", len(total_part))
print("Number of participants")
print("with multiple records        :", len(repeats))

# Writing an output file with the information
# Opens a file to be written
output = open("f2016_cs8_arm198_a3.data.output.csv", 'w')
# For loop to go through each name
for each in people:
    # Writes the person's name, how many times their name repeats (or 1 if it doesn't repeat), and their distance
    output.write(each + ", " + str(repeats.get(each, 1)) + ", " + distances[people.index(each)]+'\n')
# Closes the file
output.close()
