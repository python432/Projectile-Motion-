from tkinter import *
import math


root = Tk()
root.title("Projectile Motion Calculator")




def voGrab():
    global currentVo
    currentVo = vo.get()
    currentVo = float(currentVo)

def thetaGrab():
    global currentTheta 
    currentTheta = theta.get()
    currentTheta = float(currentTheta)
    currentTheta = math.radians(currentTheta)
    


#   When hit sumbit button
def runCalc():
    voGrab()
    thetaGrab()
    heightCalc()
    timeCalc()
    rangeCalc()
    


#   Calculations
def heightCalc():
    calcHeight = (((currentVo ** 2) * ((math.sin(currentTheta)) ** 2)) / (2*9.8))
    calcHeight = str(calcHeight)
    heightValue.insert(0, calcHeight)

def timeCalc():
    calcTime = ((currentVo * 2) * (math.sin(currentTheta)) / 9.8 )
    calcTime = str(calcTime)
    timeValue.insert(0, calcTime)

def rangeCalc():
    calcRange = ((currentVo ** 2) * (math.sin(2 * currentTheta)) / 9.8)
    calcRange = str(calcRange)
    distanceValue.insert(0, calcRange)





#                   Display

#           Right Side

#   Initial Velocity 
voLabel = Label(root, text="Input the initial velocity (m/s): ")
voLabel.grid(row= 0, column= 0)

vo = Entry(root, width= 20, borderwidth= 5)
vo.grid(row= 1, column= 0)


#   Initial Degree
thetaLabel = Label(root, text = "Input the initial degree: ")
thetaLabel.grid(row=2, column = 0)

theta = Entry(root, width = 20, borderwidth = 5)
theta.grid(row = 3, column = 0)

#   Gravity Value (Earth) 
gravLabel = Label(root, text="Gravity on Earth")
gravLabel.grid(row = 4, column = 0)

gravValue = Label(root, text="-9.8 m/s^2")
gravValue.grid(row=5, column=0)

#   Submit Button
submit = Button(root, text="Submit", command = runCalc)
submit.grid(row = 6, column = 0)




#           Middle Spaces 
spaceLabel = Label(root, text="                        ")
spaceLabel.grid(row=0, column = 1)




#           Left Side Display

#   Maximum Height
heightLabel = Label(root, text="Maximum Height (m)")
heightLabel.grid(row=0, column = 2)

heightValue = Entry(root)
heightValue.grid(row=1, column = 2)


#   Distance
distanceLabel = Label(root, text = "Distance (m)")
distanceLabel.grid(row = 2, column = 2)

distanceValue = Entry(root)
distanceValue.grid(row = 3, column = 2)


#   Time
timeLabel = Label(root, text="Time (s)")
timeLabel.grid(row=4, column = 2)

timeValue = Entry(root)
timeValue.grid(row=5, column=2)



#Finish
root.mainloop()