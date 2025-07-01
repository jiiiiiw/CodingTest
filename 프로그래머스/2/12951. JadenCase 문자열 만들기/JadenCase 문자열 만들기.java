class Solution {
    public String solution(String s) {
        s = s.toLowerCase();
        StringBuilder r = new StringBuilder();
        boolean f = true;

        for (char c : s.toCharArray()) {
            if (f && Character.isLetter(c)) {
                r.append(Character.toUpperCase(c));
            } else {
                r.append(c);
            }
            f = (c == ' ');
        }

        return r.toString();
    }
}