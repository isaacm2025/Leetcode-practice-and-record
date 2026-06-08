
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * backtracking
 * time complexity: O(4^n) because in the worst case, each digit can correspond to 4 letters (for digits 7 and 9), and we need to explore all possible combinations of letters for the given digits
 * space complexity: O(n) because the maximum depth of the recursion is equal to the length of the input digits string, and we are using a StringBuilder to build the current combination of letters, 
 * which can take up to O(n) space in the worst case when we have a combination of letters that is as long as the input digits string
 */
class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> results = new ArrayList<>();
        results = new ArrayList<>();

        Map<Character, String> numMap = Map.of(
                '2', "abc",
                '3', "def",
                '4', "ghi",
                '5', "jkl",
                '6', "mno",
                '7', "pqrs",
                '8', "tuv",
                '9', "wxyz"
    
        );
        StringBuilder currentString = new StringBuilder();

        recursiveHelper(numMap, digits, results, 0, currentString); // call the helper function to start the recursive process with the initial index set to 0 and an empty currentString
        return results; // return the list of results after the recursive process is complete

    }

    private void recursiveHelper(Map<Character, String> numMap, String digits, List<String> results, int index, StringBuilder currentString) {
        // base case: if the index is greater than the length of the digits string, it means we have formed a complete combination, so we add it to the results list and return
        if (index > digits.length() - 1) {
            results.add(currentString.toString());
            return;
        }
        String letters = numMap.get(digits.charAt(index)); // get the corresponding letters for the current digit from the numMap
        for (int i = 0; i < letters.length(); i++) { // iterate through the letters corresponding to the current digit
            currentString.append(letters.charAt(i)); // append the current letter to the currentString
            recursiveHelper(numMap, digits, results, index + 1, currentString); // recursively call the helper function with the next index to process the next digit
            currentString.deleteCharAt(currentString.length() - 1); // backtrack by removing the last character added to currentString to explore other combinations with different letters for the current digit
        }
    }

}