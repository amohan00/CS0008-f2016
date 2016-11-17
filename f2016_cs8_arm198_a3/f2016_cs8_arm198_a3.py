# Empty List with the file names from the master file
file_names = []

# Variable to count the number of files
file_counter = 0

# Opening the master file
master_file = open("f2016_cs8_a3.data.txt", 'r')

# Loop to count the files and add the file names to the list
for header in master_file:
    file_counter += 1
    file_names.append(header.rstrip('\n'))