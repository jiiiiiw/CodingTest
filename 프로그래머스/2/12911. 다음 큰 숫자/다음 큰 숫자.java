class Solution {
    public int solution(int n) {
        int a = Integer.bitCount(n);
        int b = n + 1;
        while (Integer.bitCount(b) != a) {
            b++;
        }
        return b;
    }
}