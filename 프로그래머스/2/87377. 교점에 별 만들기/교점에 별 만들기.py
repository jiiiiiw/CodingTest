def solution(line):
    def find_intersection(l1, l2):
        a, b, e = l1
        c, d, f = l2
        if a*d - b*c == 0:  # 평행 또는 일치
            return None
        x = (b*f - e*d) / (a*d - b*c)
        y = (e*c - a*f) / (a*d - b*c)
        if x.is_integer() and y.is_integer():
            return (int(x), int(y))
        return None

    intersections = set()
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            point = find_intersection(line[i], line[j])
            if point:
                intersections.add(point)

    if not intersections:
        return ["*"]

    min_x = min(p[0] for p in intersections)
    max_x = max(p[0] for p in intersections)
    min_y = min(p[1] for p in intersections)
    max_y = max(p[1] for p in intersections)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [['.'] * width for _ in range(height)]

    for x, y in intersections:
        grid[max_y - y][x - min_x] = '*'

    return [''.join(row) for row in grid]