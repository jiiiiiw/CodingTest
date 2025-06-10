import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_count = dict()

    for op in operations:
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_count[num] = entry_count.get(num, 0) + 1

        elif op == 'D 1':
            while max_heap:
                num = -heapq.heappop(max_heap)
                if entry_count.get(num, 0) > 0:
                    entry_count[num] -= 1
                    break

        elif op == 'D -1':
            while min_heap:
                num = heapq.heappop(min_heap)
                if entry_count.get(num, 0) > 0:
                    entry_count[num] -= 1
                    break

    min_val, max_val = None, None
    for num in entry_count:
        if entry_count[num] > 0:
            if min_val is None or num < min_val:
                min_val = num
            if max_val is None or num > max_val:
                max_val = num

    if min_val is None:
        return [0, 0]
    else:
        return [max_val, min_val]