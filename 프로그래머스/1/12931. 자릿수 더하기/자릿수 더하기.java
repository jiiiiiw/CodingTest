public class Solution {
    public int solution(int N) {
        int sum = 0;
        
        while (N > 0) {
            sum += N % 10; 
            N /= 10;        
        }
        
        return sum;
    }
}