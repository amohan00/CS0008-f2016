# Empty List to store the file names from the master file
file_names = []

# Variable to count the number of files
file_counter = 0

# Opening the master file
master_file = open("f2016_cs8_a3.data.txt", 'r')

# Loop to count the files in the master file and add the file names to the list
for header in master_file:
    file_counter += 1
    file_names.append(header.rstrip('\n'))

# Closing the master file
master_file.close()

# Variable to count the number of lines total
line_counter = 0

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

print(distances)
print(people)