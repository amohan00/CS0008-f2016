# definition of the class participant
class participant:
    """ participant class"""

    # properties
    # name of the participant
    name = "unknown"
    # total distance run by the participant
    distance = 0
    # total number of runs by the participant
    runs = 0

    # methods
    # initializer methods
    def __init__(self, name, distance=0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0:
            # set distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1
            # end if

    # end def __init__

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
            # end if

    # end def addDistance

    # addDistances method
    def addDistances(self, distances):
        # loops over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
                # end if
                # end for

    # end def addDistance

    # return the name of the participant
    def getName(self):
        return self.name

    # end def getName

    # return the total distance run computed
    def getDistance(self):
        return self.distance

    # end def getDistance

    # return the number of runs
    def getRuns(self):
        return self.runs

    # end def getRuns

    # stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
        # end def __init__

    # convert to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
    # end def tocsv

# end class participant

# Empty List to store the file names from the master file
file_names = []

# Variable to count the number of files
file_counter = 0

# Opening the master file
file_input = input("Please input the name of the master file: ")
master_file = open(file_input, 'r')

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
test = []

# For loop to go through and open each file
for line in file_names:
    names = open(line, 'r')

    # For loop to go through each file line by line
    for row in names:
        # Exclude the header
        if "distance" in row:
            # Skips line
            continue
        # Splits each line by the comma and assigns the values to a list
        temp = row.split(',')
        # Removes the new line character from the distance and adds it to a list
        distances.append(temp[1].rstrip('\n'))
        # Removes the space from the names and adds them to a list
        people.append(temp[0].strip(' '))
        #
        test.append({'name': temp[0].strip(' ')})
        # Adds one to the line counter
        line_counter += 1
    # Closes the file
    names.close()

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
output = open("f2016_cs8_arm193_a3.data.output.csv", 'w')
# For loop to go through each name
for each in people:
    # Writes the person's name, how many times their name repeats (or 1 if it doesn't repeat), and their distance
    output.write(each + ", " + str(repeats.get(each, 1)) + ", " + distances[people.index(each)]+'\n')
# Closes the file
output.close()