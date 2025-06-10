class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String str1 = String.valueOf(a);
        String str2 = String.valueOf(b);
        
        int str3 = Integer.valueOf(str1 + str2);
        int str4 = Integer.valueOf(str2 + str1);
        
        if(str3 >= str4){
            answer = str3;
        }else{
            answer = str4;
        }
        
        return answer;
    }
}