class Solution {
    public int solution(int n) {
        int a = 0;
        int b = 1;
        while (b * (b - 1) / 2 < n) {
            if ((n - b * (b - 1) / 2) % b == 0) {
                a++;
            }
            b++;
        }
        return a;
    }
}