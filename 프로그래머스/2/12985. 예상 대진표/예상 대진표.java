public class Solution {
    public int solution(int n, int a, int b) {
        int r = 0;
        while (a != b) {
            a = (a + 1) / 2;
            b = (b + 1) / 2;
            r++;
        }
        return r;
    }
}