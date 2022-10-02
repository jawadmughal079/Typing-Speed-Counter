import random
from time import *
import string


def errorCalculater(comp, userInput):
    # crete the vaiable to stor the count of error
    error = 0
    for item in range(len(comp)):
        try:
            if comp[item] != userInput[item]:
                error = error+1
        except:
            error = error+1
    return error


def timeCalculater(starTime, EndTime, userInput):
    totalTime = EndTime-starTime
    # now we need is to round the time
    # 2 SHOW HOW MANY DECIMAL WE NEED TO AFTER DECIMAL
    totalTime = round(totalTime, 2)
    # how calculate the speed
    # we also need to calculate the length 
    speed = len(userInput)/totalTime
    # after division it will give you  decimal it is require to round of
    return round(speed)


print("how to crete the speed calculater in python ")


# first import time module for calcuolate the time


# second module is RANDOM because how need to generate the random String


# let create the list to store the strings into

strings = ["how are you i hope you are well ",
           "this is testing area for coader ", "i am good programer "]


# create the vaiable to store the random string

# choice work is it select the random strings from list and array and tuples
comp = random.choice(strings)

# PRINT THE string for user
print(comp)

# let take the input form user

# first we need the count the time to start the tying 

startTime=time()

userInput = input("Enter a string for check the Typing Speed : \t")

# second after end the input we also need to count the time 
EndTime=time()

# let compare both the strings Make the function


print("THE ERROR OF WORD IS : ", errorCalculater(comp, userInput))


# let make a function for how much time to write this string
# we need to pass the start time or end time or user Input

print(" TOTAL SPEED OF USER ",timeCalculater(startTime,EndTime,userInput),"WPS")




