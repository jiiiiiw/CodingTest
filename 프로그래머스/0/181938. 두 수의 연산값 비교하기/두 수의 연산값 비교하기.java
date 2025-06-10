class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int var1 = Integer.parseInt(""+a+b);
        int var2 = 2*a*b;
        
        if(var1 >= var2){
            answer = var1;
        }else{
            answer = var2;
        }
        return answer;
    }
}