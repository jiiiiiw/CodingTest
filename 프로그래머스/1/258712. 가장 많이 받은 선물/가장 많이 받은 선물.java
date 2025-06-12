import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int n = friends.length;

        Map<String, Integer> idxMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            idxMap.put(friends[i], i);
        }

        int[][] giftMap = new int[n][n];
        int[] given = new int[n];   
        int[] received = new int[n]; 

        for (String g : gifts) {
            String[] parts = g.split(" ");
            int from = idxMap.get(parts[0]);
            int to = idxMap.get(parts[1]);
            giftMap[from][to]++;
            given[from]++;
            received[to]++;
        }

        int[] nextMonthGifts = new int[n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;

                int giToj = giftMap[i][j];
                int gjToi = giftMap[j][i];

                if (giToj > gjToi) {
                    nextMonthGifts[i]++;
                } else if (giToj == gjToi) {
                    int giScore = given[i] - received[i];
                    int gjScore = given[j] - received[j];
                    if (giScore > gjScore) {
                        nextMonthGifts[i]++;
                    }
                }
            }
        }

        int max = 0;
        for (int x : nextMonthGifts) {
            max = Math.max(max, x);
        }
        return max;
    }
}