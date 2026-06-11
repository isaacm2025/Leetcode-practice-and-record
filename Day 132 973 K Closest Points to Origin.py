'''You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:



Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).
Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:

1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100'''

#sorting
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0] ** 2 + x[1] ** 2) #sort the points based on their distance from the origin, which is calculated as x^2 + y^2, since we only need to compare the distances, we can ignore the square root and just compare the squares of the distances. 
        #Use lambda becuase we need to sort the points based on their distance from the origin, which is calculated as x^2 + y^2, and we can use a lambda function to specify the sorting key as the distance from the origin
        return points[: k]
#time complexity: O(nlogn) for sorting the array, where n is the number of points
#space complexity: O(1) for sorting the array in place