import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String string = sc.next();
        
        for (char s : string.toCharArray()){
            System.out.println(s);
        }
    }
}