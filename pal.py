def pal(s):
    for k, v in enumerate(s):
        print k, v, -1 * (k + 1), s[-1 * (k + 1)]
        if not v == s[-1 * (k + 1)]:
            return False
        continue
    return True

if __name__ == '__main__':
    print pal('maam')