# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 04:57:49 2016

@author: julien
"""

import turtle
# Tess becomes a traffic light.
import numpy as np

import time


turtle.setup(1000,1000)
wn = turtle.Screen()
wn.title("Automated Parking Space Detection, AI-Perspective Concept")
wn.bgcolor("white")

parking_engineer = turtle.Turtle()
parking_engineer.speed(9)



##########Declaration of state of parking spots
spot_1 = turtle.Turtle()
spot_2 = turtle.Turtle()
spot_3 = turtle.Turtle()
spot_4 = turtle.Turtle()
spot_5 = turtle.Turtle()
spot_6 = turtle.Turtle()
##########Declaration of state of parking spots

##########Declaration of driver
fortunate_driver = turtle.Turtle()
##########Declaration of driver

fortunate_driver.speed(1)

state_spot1 = 1
state_spot2 = 1
state_spot3 = 1
state_spot4 = 1
state_spot5 = 1
state_spot6 = 1



#0 <-- free spot 
#1 <-- busy/occupied spot 

def draw_parking_boundaries():
    tess = turtle.Turtle()
    tess.penup()
    tess.setpos((-300,-300))
    print tess.pos()
    tess.pensize(3)
    tess.pendown()
    tess.goto((450,-300))
    print tess.pos()
    tess.goto((450,325))
    print tess.pos()
    tess.goto((-300,325))
    print tess.pos()
    tess.goto((-300,-300))
    print tess.pos()
    print "parking boudaries created"
    

def draw_parking_spots():
    #tess = turtle.Turtle()
    parking_engineer.penup()
    parking_engineer.goto((225,250))
    print parking_engineer.pos()
    parking_engineer.pensize(3)
    parking_engineer.pendown()
    parking_engineer.goto((225,-250))
    print parking_engineer.pos()
    
    parking_engineer.left(90)    
    parking_engineer.forward(125)
    parking_engineer.left(90)
    
    go_and_make_a_spot()

    print "first spot"   

    parking_engineer.forward(150)
    
    go_and_make_a_spot()
  
    print "second spot"
    
    return_to_track()
    
    go_and_make_a_spot()

    print "third spot"
    
    parking_engineer.forward(150)

    go_and_make_a_spot()
    print "end fourth"
    
    return_to_track()
    
    go_and_make_a_spot()
    print "fifth spot"
    
    parking_engineer.forward(150)
        
    go_and_make_a_spot()
    print "sixth spot"
    
    parking_engineer.penup()
    
    print "Done with parking!!!!"


def go_and_make_a_spot():    
    #tess = turtle.Turtle()    
    parking_engineer.forward(150)    
    parking_engineer.right(90)
    parking_engineer.forward(25)
    parking_engineer.left(90)
    parking_engineer.forward(25)
    parking_engineer.left(90)    
    parking_engineer.forward(50)
    parking_engineer.left(90)
    parking_engineer.forward(25)
    parking_engineer.left(90)
    parking_engineer.forward(25)
    parking_engineer.right(90)
    
def return_to_track():
    parking_engineer.forward(150)
    parking_engineer.right(90)
    parking_engineer.forward(125)
    parking_engineer.left(90)
    

draw_parking_boundaries()
draw_parking_spots()
parking_engineer.hideturtle() #hide engineer 

spot_1.penup() #do not write while moving
spot_2.penup()
spot_3.penup()
spot_4.penup()
spot_5.penup()
spot_6.penup()
fortunate_driver.penup()

spot_1.setpos((62.5,-125))
spot_1.shape("square")
spot_1.fillcolor("red")

spot_2.setpos((387.5,-125))
spot_2.shape("square")
spot_2.fillcolor("red")

spot_3.setpos((62.5,0))
spot_3.shape("square")
spot_3.fillcolor("red")

spot_4.setpos((387.5,0))
spot_4.shape("square")
spot_4.fillcolor("red")

spot_5.setpos((62.5,125))
spot_5.shape("square")
spot_5.fillcolor("red")

spot_6.setpos((387.5,125))
spot_6.shape("square")
spot_6.fillcolor("red")

def h4():
    wn.bye()

def handler_for_spot_1(x,y):
    global state_spot1
    if state_spot1 == 0:
        spot_1.fillcolor("red")
        state_spot1 = 1
    else:
        spot_1.fillcolor("green")
        state_spot1 = 0
        
def handler_for_spot_2(x,y):
    global state_spot2
    if state_spot2 == 0:
        spot_2.fillcolor("red")
        state_spot2 = 1
    else:
        spot_2.fillcolor("green")
        state_spot2 = 0

def handler_for_spot_3(x,y):
    global state_spot3
    if state_spot3 == 0:
        spot_3.fillcolor("red")
        state_spot3 = 1
    else:
        spot_3.fillcolor("green")
        state_spot3 = 0

def handler_for_spot_4(x,y):
    global state_spot4
    if state_spot4 == 0:
        spot_4.fillcolor("red")
        state_spot4 = 1
    else:
        spot_4.fillcolor("green")
        state_spot4 = 0

def handler_for_spot_5(x,y):
    global state_spot5
    if state_spot5 == 0:
        spot_5.fillcolor("red")
        state_spot5 = 1
    else:
        spot_5.fillcolor("green")
        state_spot5 = 0


def handler_for_spot_6(x,y):
    global state_spot6
    if state_spot6 == 0:
        spot_6.fillcolor("red")
        state_spot6 = 1
    else:
        spot_6.fillcolor("green")
        state_spot6 = 0

fortunate_driver.setpos((-250,-290))
fortunate_driver.shape("square")
fortunate_driver.color("blue")
fortunate_driver.left(90)



spot_1.onclick(handler_for_spot_1)
spot_2.onclick(handler_for_spot_2)
spot_3.onclick(handler_for_spot_3)
spot_4.onclick(handler_for_spot_4)
spot_5.onclick(handler_for_spot_5)
spot_6.onclick(handler_for_spot_6)


spots = [spot_1,spot_2,spot_3,spot_4,spot_5,spot_6]
#states = [state_spot1,state_spot2,state_spot3,state_spot4,state_spot5,state_spot6]
least_cost = 0

distance_y = 0 # the distance on x from the agent to the the x position of the goal

closest_agent = [] #the index of coordinates of the position of the goal

timeout = time.time() + 60*0.5   # 1 minutes from now

while True:
    
    test = 0
    if test == 5 or time.time() > timeout:
        break
    test = test - 1    
    
    distance = []
    states = [state_spot1,state_spot2,state_spot3,state_spot4,state_spot5,state_spot6]

    spot_1.onclick(handler_for_spot_1)
    spot_2.onclick(handler_for_spot_2)
    spot_3.onclick(handler_for_spot_3)
    spot_4.onclick(handler_for_spot_4)
    spot_5.onclick(handler_for_spot_5)
    spot_6.onclick(handler_for_spot_6)    
    
    for i in spots:        
        distance.append(fortunate_driver.distance(i))
    
    #Searches in the list of states the index that returns 0 for free    
    available_spots = [i for i,x in enumerate(states) if x == 0]
    
    print "Available spots"
    print available_spots
    
    #returns the set of distances where the parking spots are available from available distance
    free_spots_distances = [distance[i] for i in available_spots]
    
    print "Distance to free available spots"
    print free_spots_distances
    
    least_cost = 0    
    
    #returns the minimun distance from all the available spots to the driver
    if not free_spots_distances:
        min_distance_index = 0
    else:
        min_distance_index = np.argmin(free_spots_distances)
#        print "Smallest distance"
        least_cost = free_spots_distances[min_distance_index]
        
    print "Smallest distance"
    print least_cost
    #for j in distance:
    
    #queries the main list of spots, to get the current distance
    closest_agent = [i for i,x in enumerate(spots) if (fortunate_driver.distance(x)-least_cost) == 0]
    print closest_agent
    if not closest_agent:
        closest_agent = []
    else:
        print spots[closest_agent[0]].pos()
        
        
            
            #pythagorean distance
    #        if i.fillcolor() == 'green':
    #            #distance.append(fortunate_driver.distance(i))
    #            print np.sqrt((fortunate_driver.pos()[0]-i.pos()[0])**2+(fortunate_driver.pos()[1]-i.pos()[1])**2)
    #            min_distance_index = np.argmin(distance)
    #            #x_min,y_min = spots[].pos()
    #            #print (x_min,y_min)
    #            print min_distance_index
        #    else:
        #        print "all Busy"
        print "State of each spot"
        print states
        print "Distance form driver to all spots"
        print distance
        
        print #####
    
print "off loop"

if not closest_agent:
    print "no chance my man"
    fortunate_driver.forward(-200)
else:
    print "Should head to that spot"
    print spots[closest_agent[0]].pos()
    
    distance_y = np.abs(spots[closest_agent[0]].pos()[1] - fortunate_driver.pos()[1])
    
    print "distance from agent"
    print distance_y
    
    print "distance y to the goal"
    print spots[closest_agent[0]].pos()[1] 
    
    print "distance to travel from the agent"
    print fortunate_driver.pos()[1]
    
    print "distance to travel from the goal"
    print fortunate_driver.pos()[1] + distance_y
    
    fortunate_driver.forward(distance_y)
    
    print fortunate_driver.pos()
    
    fortunate_driver.goto(spots[closest_agent[0]].pos())

#y_fortunate_driver_extra = np.array([1,2])
#
#y_fortunate_driver_extra = fortunate_driver.pos()
#
#y_fortunate_driver_extra[1] = fortunate_driver.pos()[1] + 1
#
#x_spot_extra = np.array([1,2])
#
#x_spot_extra = spots[closest_agent[0]].pos()
#
#x_spot_extra[0] = spots[closest_agent[0]].pos()[0] + 1
#
## now lets find angle between the agent and the spot, if theta > 0 => pi/2, -pi/2 otherwise
#
##vector of agent 
#vector_fortunate_driver = y_fortunate_driver_extra - fortunate_driver.pos()
#vector_spot = x_spot_extra - spots[closest_agent[0]].pos()







wn.onkey(h4, "q")
# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
turtle.mainloop()
