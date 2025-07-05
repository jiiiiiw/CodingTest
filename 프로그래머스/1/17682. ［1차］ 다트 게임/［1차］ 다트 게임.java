import java.util.regex.*;

class Solution {
    public int solution(String s) {
        int[] a = new int[3];  
        int i = 0;             

        Pattern p = Pattern.compile("(10|[0-9])([SDT])([*#]?)");
        Matcher m = p.matcher(s);

        while (m.find()) {
            int x = Integer.parseInt(m.group(1));  
            String b = m.group(2);                 
            String o = m.group(3);                 

            if (b.equals("S")) x = (int)Math.pow(x, 1);
            else if (b.equals("D")) x = (int)Math.pow(x, 2);
            else if (b.equals("T")) x = (int)Math.pow(x, 3);

            if (o.equals("*")) {
                x *= 2;
                if (i > 0) a[i - 1] *= 2;
            } else if (o.equals("#")) {
                x *= -1;
            }

            a[i++] = x;
        }

        return a[0] + a[1] + a[2];
    }
}
