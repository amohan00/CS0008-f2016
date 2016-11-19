# Empty List to store the file names from the master file
file_names = []

# Variable to count the number of files
file_counter = 0

# Opening the master file
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
del distances[0], distances[150], distances[300], people[0], people[150], people[300]

# Calculating total number of participants
# Convert the list people to a set to get rid of doubles
people_no_duplicates = set(people)
# Find the length of the set of all the people
total_part = len(people_no_duplicates)

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
max_dist = max(distances)
min_dist = min(distances)
# Assigns which person has the index of the max and min distances
max_part = people[distances.index(max_dist)]
min_part = people[distances.index(min_dist)]

# Finding how many names repeat
# Empty List to copy the list with names
people_copy = []
# For loop to go through each line of the list
for thing in people:
    # Adds the line to the copy of the list
    people_copy.append(thing)
# Sorts the list alphabetically
people_copy.sort()
# Variables to count how many names appear more than once
repeats = 0
count = 0
# While loop to go through the sorted list until the second to last one
while count < len(people_copy) - 1:
    # Counts a repeat only if the name is the same as the one after it and not before it, to avoid doubles
    if people_copy[count] == people_copy[count + 1] and people_copy[count] != people_copy[count - 1]:
            repeats += 1
    # Counter to stop the loop
    count += 1

# Printing all the information with the correct formatting
print("Number of Input files read   :", file_counter)
print("Total number of lines read   :", line_counter)
print("\ntotal distance run           :", total_distance)
print("\nmax distance run             :", max_dist)
print("  by participant             :", max_part)
print("\nmin distance run             :", min_dist)
print("  by participant             :", min_part)
print("\nTotal number of participants :", total_part)
print("Number of participants")
print("with multiple records        :", repeats)