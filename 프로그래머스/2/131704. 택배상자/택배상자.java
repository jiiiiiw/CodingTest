import java.util.*;

class Solution {
    public int solution(int[] o) {
        Stack<Integer> s = new Stack<>();
        int a = 1; 
        int i = 0; 

        while (a <= o.length) {
            if (a == o[i]) {
                i++;
                a++;
            } else if (!s.isEmpty() && s.peek() == o[i]) {
                s.pop();
                i++;
            } else {
                s.push(a++);
            }
        }

        while (!s.isEmpty() && s.peek() == o[i]) {
            s.pop();
            i++;
        }

        return i;
    }
}
