import java.util.*;

public class Solution {
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) return cities.length * 5;

        int time = 0;
        LinkedHashMap<String, Boolean> cache = new LinkedHashMap<>(cacheSize, 0.75f, true);

        for (String city : cities) {
            city = city.toLowerCase();

            if (cache.containsKey(city)) {
                time += 1;
                cache.get(city);
            } else {
                time += 5;
                if (cache.size() >= cacheSize) {
                    String lru = cache.keySet().iterator().next();
                    cache.remove(lru);
                }
                cache.put(city, true);
            }
        }

        return time;
    }
}