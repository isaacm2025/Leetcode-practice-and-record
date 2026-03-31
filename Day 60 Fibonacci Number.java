import java.util.HashMap;
import java.util.Map;

public class Day 60 Fibonacci Number() {
    public int fib(int n) {
        /**
         * The Fibonacci sequence is defined as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. 
         * In other words, the first two numbers in the sequence are 0 and 1, and each subsequent number is the sum of the previous two.
         * n >= 2 to utilize the Fibonacci equation, otherwise we can return n itself as the result.
         * n < 2 -> base case, return n
         * n >= 2 -> recursive case, return fib(n-1) + fib(n-2)
         * Time complexity: O(2^n) - exponential time complexity due to the repeated calculations of the same Fibonacci numbers.
         * Space complexity: O(n) - due to the call stack used for recursion, which can go up to n levels deep in the worst case.
         * n = 2 : 1
         * 
         * Not off by 1:
         * n = 1 and n = 2 -> fib(1) = 1 and fib(2) -> return 1;
         * 
         * off by 1:
         * n = 0 and n = 1 -> fib(0) = 0 and fib(1) = 1 -> fib(n) = n -> return n;
         * 
         * Recursive approach:
         * fib(n - 1) + fib(n - 2)
         * 
         * 
         * 
         *                                          fib(n)
         *                                /                     \    
         *                            fib(n-1)                               fib(n-2)
         * *                          /       \                              /       \
         * *                      fib(n-2)  fib(n-3)                     fib(n-3)  fib(n-4)
         * *                      /   \      /   \                        /   \      /   \
         * *                  fib(n-3) fib(n-4) fib(n-4) fib(n-5)     fib(n-4) fib(n-5) fib(n-5) fib(n-6)
         * 
         * time complexity: O(2^n) - exponential time complexity due to the repeated calculations of the same Fibonacci numbers.
         * space complexity: O(n) - due to the call stack used for recursion, which can go up to n levels deep in the worst case.
         */

        //recursive approach
        //if (n <= 1) {
         //   return n;
        //}
        //return fib(n-1) + fib(n-2);

        /**
         * How to optimize?
         * non-necessary computation or duplicate computation can be avoided by storing the previously computed Fibonacci numbers in a data structure such as an array or a hash map. 
         * This technique is known as memoization.
         * 
         * 
         * Question: if we call a recursive function twice with the same input, will it return the same result?
         * Yes, if the function is deterministic (i.e., it always produces the same output for the same input), then calling it twice with the same input will return the same result.
         * 
         * 
         * Question2: can we avoid doing this duplicate work? Can we calculate the same value only once and use the result later?
         * Yes, we can avoid doing duplicate work by using memoization. 
         * We can store the results of previously computed Fibonacci numbers in a data structure (like an array or a hash map) and check if the value has already been computed before performing the recursive calls.
         * 
         * 
         * A map: a collection of key-value pairs where each key is unique and maps to a specific value.
         * look up value by its key in O(1) time complexity.
         * finding an element in an array requires O(n) time complexity, while looking up a value in a map can be done in O(1) time complexity on average.
         * 
         * Map<Integer, Integer> memo = new HashMap<>();
         *      i,       fib(i)
         *
         */

        //memoization approach
        if (n <= 1) {
            return n;
        }
        Map<Integer, Integer> memo = new HashMap<>();
        return fibMemo(n, memo);
    }

    private int fibMemo(int n, Map<Integer, Integer> memo) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        if (n <= 1) {
            return n;
        }
        int result = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
        memo.put(n, result);
        return result;
    }
    /**
     * why faster?
     * The memoization approach is faster than the naive recursive approach because it avoids redundant calculations by storing previously computed results. 
     * In the naive recursive approach, the same Fibonacci numbers are calculated multiple times, leading to an exponential time complexity of O(2^n). 
     * In contrast, the memoization approach has a linear time complexity of O(n) because each Fibonacci number is computed only once and stored in the map for future reference. 
     * This significantly reduces the number of function calls and improves the overall efficiency of the algorithm.
     * 
     * can use dynamic programming approach as well, which is an iterative approach that builds up the solution from the base cases.
     * space complexity: O(1)
     * 
     * using matrix:
     * time O(n) -> O(log n) using fast exponentiation
     */
}
