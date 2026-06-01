
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

class NumberOfStudentsUnableToEatLunch {
    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> studentQueue = new LinkedList<>();
        Stack<Integer> sandwichStack = new Stack<>();

        for (int i = 0; i < students.length; i++) {
            studentQueue.offer(students[i]);
        }
        for (int i = sandwiches.length - 1; i >= 0; i--) {
            sandwichStack.push(sandwiches[i]);

        }
        int count = 0;
        while (studentQueue.size() > 0 && count < studentQueue.size()) {
            if (studentQueue.peek() == sandwichStack.peek()) {
                studentQueue.poll();
                sandwichStack.pop();
                count = 0;
            } else {
                studentQueue.offer(studentQueue.poll());
                count++;
            }

        }
        return studentQueue.size();
    }
    
}
