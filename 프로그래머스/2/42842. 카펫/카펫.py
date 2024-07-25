def solution(brown, yellow):
    # bh, bw = yh + 2, yw + 2
    # yellow + brown = bh * bw
    
    for bh in range(1, brown//2 + 1): # 길어봤자지 ~
        bw = (brown - 2*bh + 4)//2
        yh, yw = bh - 2, bw - 2
        if yellow == yh * yw and yellow + brown == bh * bw:
            return [bw, bh]