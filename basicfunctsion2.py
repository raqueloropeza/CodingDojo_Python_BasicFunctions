#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]
#for loop range will start at input number and end at -1 to include 0.


count = []
def countdown(num):
    for i in range (num,-1,-1):
        count.append(i)
    return count
print (countdown(15))

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2
def printreturn(list):
    if len(list) == 2:
        print (list[0])
        return (list[1])
    else:
        print ("list must be two numbers")
print (printreturn([2,4]))

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def firstLength (list):
    return ((list[0]) + len(list))
print (firstLength([1,2,3,4,5]))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
#define function for a list
#create a for loop to go through each index in the list 
#compare the current index to the next index.
#whichever is greater append to the new list
#increment by 2 
#print the length of the new list
#return the new array

newList = []
def greaterThanSecond (list):
    if  len(list)<2:
        return False
    for i in range (0,len(list),2):
        if list[i]> list[i+1]:
            newList.append(list[i])
        else:
            newList.append(list[i+1])
    print(len(newList))
    return newList
print (greaterThanSecond([5,2,3,2,1,4]))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]
newList = []
def lengthValue(size, value):
    for i in range (size,0, -1):
        newList.append(value)
    return newList
print (lengthValue(6,2))
    