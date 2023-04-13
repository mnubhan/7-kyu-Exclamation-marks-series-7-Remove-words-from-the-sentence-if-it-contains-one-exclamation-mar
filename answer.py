def remove(s):
    return ' '.join(w for w in s.split(' ') if w.count('!') != 1)
    
def remove(string):
    result = []
    for i in string.split(' '):
        if i.count('!') != 1:
            result.append(i)
    return ' '.join(result)
