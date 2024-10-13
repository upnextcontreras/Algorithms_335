#CPSC 335 Project 1
#Marcus Martin

#I commented some of the print fuinctions for testing, left them in if you want to see the algorithim working as it progresses through the loops
#alter input here.
#NOTE: this algorithim works only if exactly the correct distances, gas station, and mpg are entered together
#array size of City_distances MUST equal array size of Gas_station AND sum of City_distances MUST equal sum of Gas_station multiplied by Mpg
#I could very easily have added it in but it was not a requirement of the project
City_distances = [5,25,15,10,15]
Gas_station = [1,2,1,0,3]
Mpg = 10
Num_cities = 0
Starting_position = 0

print("Distance to the next city: ", City_distances, "miles")
print("Amount of Gallons availabe at each city: ", Gas_station, "gallons")
print("Miles per Gallon: ", Mpg)

#loop to find the number of cities/gas stations
for i in City_distances:
    Num_cities += 1

#outside loop for altering the starting position of the algorithim
for x in City_distances:
    Fuel = 0
    Current_fuel = 0
    Cities_travelled = 0
    Current_position = Starting_position
    #print("Testing from city index#: ", (Starting_position))

#inside loop to testing how many cities you can visit given that you tank up, then travel
    for y in City_distances:
        Fuel = Fuel + (Gas_station[Current_position] * Mpg)
        #print("Before Driving ", Fuel)
        Fuel = Fuel - (City_distances[Current_position])
        #print("After Driving ", Fuel)
        Current_position += 1
        #check if Current_position needs to reset to 0 after travelling the length of the array
        if Current_position > (Num_cities-1):
            Current_position = 0
        #check if you ran out of fuel between cities and failed to fully travel the distance
        if Fuel >= 0:
            Cities_travelled += 1
        #check if you travelled the whole loop, declare it the city you must start at, and break
        if Cities_travelled == Num_cities:  
            #print("total # of cities travelled = ", Cities_travelled)
            print("This is the best possible starting city index: ", (Starting_position))
            break
        #check if you ran out of fuel and report the number of cities travelled
        if Fuel < 0:
            #print("total # of cities travelled = ", Cities_travelled) 
            break
    #back to the outside loop, need to increase starting position before re-entering the inside loop
    Starting_position += 1
        
