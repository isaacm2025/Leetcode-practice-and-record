'''Asteroid Collision
Medium
Topics
Company Tags
You are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [2,4,-4,-1]

Output: [2]
Example 2:

Input: asteroids = [5,5]

Output: [5,5]
Example 3:

Input: asteroids = [7,-3,9]

Output: [7,9]
Constraints:

2 <= asteroids.length <= 10,000.
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0'''

from typing import List
#stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] #we want to use a stack to keep track of the asteroids that are still in space after we have processed all the collisions, since we want to be able to easily access the last asteroid that we have processed and compare it with the current asteroid to see if they collide or not
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0: #we want to check if the current asteroid is moving left (negative) and the last asteroid in the stack is moving right (positive), since if they are moving in opposite directions, they will collide with each other
                diff = stack[-1] + a #we want to calculate the difference between the last asteroid in the stack and the current asteroid to see which one is bigger, since the smaller one will explode and the bigger one will continue moving in space
                if diff < 0: #if the difference is negative, it means that the current asteroid is bigger than the last asteroid in the stack, so we want to pop the last asteroid from the stack because it will explode and we want to continue checking if the current asteroid will collide with the next asteroid in the stack,since the current asteroid will continue moving in space after the collision
                    stack.pop() #we want to pop the last asteroid from the stack because it will explode and we want to continue checking if the current asteroid will collide with the next asteroid in the stack, since the current asteroid will continue moving in space after the collision
                elif diff > 0: #if the difference is positive, it means that the last asteroid in the stack is bigger than the current asteroid, so we want to set a to 0 because the current asteroid will explode and we want to stop checking for collisions with the next asteroids in the stack, since the current asteroid will not continue moving in space after the collision
                    a = 0
                else:
                    a = 0 #if the difference is 0, it means that both asteroids are the same size, so we want to set a to 0 because the current asteroid will explode and we want to pop the last asteroid from the stack because it will also explode, since both asteroids will explode after the collision
                    stack.pop() #we want to pop the last asteroid from the stack because it will also explode, since both asteroids will explode after the collision
            if a:
                stack.append(a) #we want to append the current asteroid to the stack if it is not 0, since if it is 0, it means that it has exploded and we do not want to add it to the stack, since we only want to keep track of the asteroids that are still in space after we have processed all the collisions
        return stack
    #time complexity: O(n) because we are iterating through the asteroids list once and performing operations on the stack, which takes O(1) time
    #space complexity: O(n) because in the worst case, we could have all the asteroids in the stack if they are all moving in the same direction and do not collide with each other

    