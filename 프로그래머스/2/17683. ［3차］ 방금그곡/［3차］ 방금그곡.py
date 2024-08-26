sharp = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a', 'B#':'b'}

def sharp2lower(m):
    for s in sharp.keys():
        m = m.replace(s, sharp[s])
    return m

def time2min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def musicfull(mel, dur):
    mel = sharp2lower(mel)
    mel = mel * (dur // len(mel) + 1) # 전체의 악보 구성
    
    return mel[:dur]
    
def solution(m, musicinfos):
    m = sharp2lower(m)
    print(m)
    play_title = ['(None)']
    play_dur = [0]
    # 재생시간
    for music in musicinfos:
        start, end, title, mel = music.split(',')
        dur = time2min(end) - time2min(start)
    # 음이 내부, 음악이 중간에 끝
        mel = musicfull(mel, dur)
        if m in mel:
            play_title.append(title)
            play_dur.append(dur)
    
    # none
    return play_title[play_dur.index(max(play_dur))]