class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow;

        for (int h = 3; h <= total / 3; h++) {
            int w = total / h;

            if (total % h == 0 && w >= h) {
                int y = (w - 2) * (h - 2);
                if (y == yellow) {
                    return new int[]{w, h};
                }
            }
        }

        return new int[]{0, 0};
    }
}