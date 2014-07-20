#print the mean of the numbers given in a file

import sys

sum = 0
n = 0

#sum input values
for num in open('data.txt'): 
    sum += float(num) #convert number to a float
    n -= 1 #subtract a number from each

print sum / n #print the end sum divided by the n
