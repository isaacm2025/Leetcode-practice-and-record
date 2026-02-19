'''There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 1000
0 < target <= 1000
0 < speed[i] <= 100
0 <= position[i] < target
All the values of position are unique.
'''
#stack
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)] #create a list of tuples where each tuple contains the position and speed of a car
        pair.sort(reverse = True)#sort the list of tuples in reverse order based on the position of the cars, so that we can process the cars from the one closest to the destination to the one farthest from the destination
        stack = [] #initialize an empty stack to keep track of the time it takes for each car or fleet to reach the destination
        for p, s in pair: #iterate through the sorted list of tuples
            stack.append((target - p) / s) #calculate the time it takes for the current car to reach the destination and push it onto the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if there are at least two times on the stack and the time for the current car is less than or equal to the time for the previous car, it means that the current car will catch up to the previous car before reaching the destination, so we pop the previous time from the stack
                stack.pop() #pop the previous time from the stack because the current car will catch up to the previous car and they will form a fleet, so we only need to keep track of the time for the fleet
        return len(stack)
#time complexity: O(n log n) due to sorting
#space complexity: O(n) for the stack and the pair list

#iteration
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)] #create a list of tuples where each tuple contains the position and speed of a car
        pair.sort(reverse = True) #sort the list of tuples in reverse order based on the position of the cars, so that we can process the cars from the one closest to the destination to the one farthest from the destination

        fleets = 1 #initialize the number of fleets to 1, because there is at least one fleet (the first car or the first fleet)
        prev_time = (target - pair[0][0]) / pair[0][1] #calculate the time it takes for the first car to reach the destination and store it as the previous time, which will be used to compare with the times of the subsequent cars
        for i in range(1, len(pair)): #iterate through the sorted list of tuples starting from the second car
            currCar = pair[i] #get the current car's position and speed
            curr_time = (target - currCar[0]) / currCar[1] #calculate the time it takes for the current car to reach the destination
            if curr_time > prev_time:
                fleets += 1 #if the time for the current car is greater than the previous time, it means that the current car will not catch up to the previous fleet and will form a new fleet, so we increment the number of fleets
                prev_time = curr_time #update the previous time to the current time for the next iteration, so that we can compare the times of the subsequent cars with the time of the current fleet
        return fleets 
#time complexity: O(n log n) due to sorting
#space complexity: O(n) for the pair list
