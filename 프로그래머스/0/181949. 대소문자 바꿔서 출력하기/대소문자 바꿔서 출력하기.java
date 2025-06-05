import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        String a = sc.next();
        
        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            
            if(Character.isUpperCase(c)){
                sb.append(Character.toLowerCase(c));
            }else if(Character.isLowerCase(c)){
                sb.append(Character.toUpperCase(c));
            }else{
                sb.append(c);
            }
        }
        
        System.out.println(sb.toString());
        
    }
}