import java.util.*;

public class Solution {
    public int solution(int[] topping) {
        int answer = 0;

        Map<Integer, Integer> rightMap = new HashMap<>();
        Set<Integer> leftSet = new HashSet<>();

        for (int t : topping) {
            rightMap.put(t, rightMap.getOrDefault(t, 0) + 1);
        }

        for (int i = 0; i < topping.length; i++) {
            int t = topping[i];
            
            leftSet.add(t);

            rightMap.put(t, rightMap.get(t) - 1);
            if (rightMap.get(t) == 0) {
                rightMap.remove(t);
            }

            if (leftSet.size() == rightMap.size()) {
                answer++;
            }
        }

        return answer;
    }
}