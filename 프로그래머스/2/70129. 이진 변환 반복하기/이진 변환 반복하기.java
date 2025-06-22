public class Solution {
    public int[] solution(String s) {
        int a = 0; 
        int b = 0; 

        while (!s.equals("1")) {
            int l = s.length();      
            s = s.replace("0", "");  
            b += (l - s.length());  
            l = s.length();         
            s = Integer.toBinaryString(l); 
            a++; 
        }

        return new int[]{a, b};
    }
}
