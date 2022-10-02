
import random
import string
from time import *
from tkinter import ROUND
def errorCalculater(comp,user):
  error=0
  for i in range(len(comp)):
    try:
        if (comp[i]!=user[i]):
            error=error+1
    except :
            error=error+1
  return error     

def timeCalculater(timeStart,timeEnd,userInput):
  totalTime=timeEnd-timeStart
  totalTime=round(totalTime,2)
  speed=len(userInput)/totalTime
  speed=round(speed)
  return  speed
# comp = string.ascii_letters
# print ( ''.join(random.choice(comp) for i in range(101)) )

comp=['hello how are you i hope you are good ','what you wnat for us ']

timeStart=time()
rComp=random.choice(comp)
print ( rComp )
userInput=input("enter your string")
timeEnd=time()

print("Error value percentage ",errorCalculater(rComp,userInput))

speed=timeCalculater(timeStart,timeEnd,userInput)
print('speedIsThis ', speed)
