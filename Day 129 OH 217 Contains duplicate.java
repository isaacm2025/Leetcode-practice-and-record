
import java.util.HashSet;
import java.util.Set;


/**
 * hashset
 * time complexity: O(n) because we need to iterate through the array once
 * space complexity: O(n) because in the worst case, we might have to store all the elements in the hashset if there are no duplicates
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> integerSet = new HashSet<>(); // create a hashset to store the unique elements

        for (int i = 0; i < nums.length; i++) { // iterate through the array
            if (integerSet.contains(nums[i])) { // if the current element is already in the hashset, it means we have found a duplicate, so we return true
                return true;
            }
            integerSet.add(nums[i]); // if the current element is not in the hashset, we add it to the hashset for future reference
        }
        return false;
    }
}
