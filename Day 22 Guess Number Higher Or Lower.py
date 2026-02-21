'''We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

0: your guess is equal to the number I picked (i.e. num == pick).
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
Return the number that I picked.

Example 1:

Input: n = 5, pick = 3

Output: 3
Example 2:

Input: n = 15, pick = 10

Output: 10
Example 3:

Input: n = 1, pick = 1

Output: 1
Constraints:

1 <= pick <= n <= ((2^31)-1)
'''

#linear search
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        for num in range(1, n + 1): #iterate through the numbers from 1 to n
            if guess(num) == 0: #if the guess is correct, return the number
                return num
#time complexity: O(n)
#space complexity: O(1)

#binary search
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n #initialize the left and right pointers
        while True:
            mid = (left + right) // 2 #calculate the middle index
            res = guess(mid) #call the guess API with the middle index
            if res > 0:
                left = mid + 1 #move the left pointer to the right of the middle index
            elif res < 0:
                right = mid - 1 #move the right pointer to the left of the middle index
            else:
                return mid
#time complexity: O(log n)
#space complexity: O(1)