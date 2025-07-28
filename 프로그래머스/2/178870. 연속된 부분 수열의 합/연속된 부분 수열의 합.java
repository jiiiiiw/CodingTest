class Solution {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;
        int start = 0, end = 0, sum = sequence[0];

        int minLength = Integer.MAX_VALUE;
        int[] answer = new int[2];

        while (start < n && end < n) {
            if (sum < k) {
                end++;
                if (end < n) sum += sequence[end];
            } else if (sum > k) {
                sum -= sequence[start];
                start++;
            } else { 
                if ((end - start) < minLength) {
                    minLength = end - start;
                    answer[0] = start;
                    answer[1] = end;
                }
                sum -= sequence[start];
                start++;
            }
        }

        return answer;
    }
}