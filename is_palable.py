def is_palable(s):
    d = {}
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    print d

    c = 0
    for i in d.values():
        if i % 2 == 1:
            c += 1

    if c > 1:
        return False
    return True

if __name__ == '__main__':
    print is_palable('maam')