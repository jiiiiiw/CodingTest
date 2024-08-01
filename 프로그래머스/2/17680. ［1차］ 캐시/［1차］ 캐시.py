def solution(cacheSize, cities):
    # 캐시구성 => 오래된것 --- 새로운 것 순 
    Cache = []
    Time = 0
    for city in cities:
        city = city.lower() # 공백 특수 없고, 대소문자가 없으니
        if city in Cache:
            Cache.remove(city)
            Cache.append(city)
            Time += 1
        else: #miss
            Cache.append(city)
            if cacheSize < len(Cache):
                Cache.pop(0)
            Time += 5
    return Time