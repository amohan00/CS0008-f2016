# name       : Arun Mohan
# email      : arm198@pitt.edu
# date       : 10/28/16
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Take home assignment 2

#Here I define the two functions that I need to use

#This function accepts the name of a file and returns how many lines
#and the sum of all the distance of the file
def processFile(fh):
    pd = 0                   #variable for partial distance
    ptn = 0                  #variable for partial # of lines
    fo = open(fh, 'r')
    for line in fo:
        ptn += 1
        line = line.rstrip('\n')
        temp = line.split(",")