class Solution {
    public String solution(String s) {
        String[] tokens = s.split(" ");
        
        int min = Integer.parseInt(tokens[0]);
        int max = min;
        
        for (int i = 1; i < tokens.length; i++) {
            int num = Integer.parseInt(tokens[i]);
            if (num < min) min = num;
            if (num > max) max = num;
        }

        return min + " " + max;
    }
}