def t():
    n = input().split()
    for e in n:
        s = []
        s.append(e)
        m = n[:]
        m.remove(e)
        for f in m:
            s.append(f)
            k = m[:]
            k.remove(f)
            for g in k:
                s.append(g)
                q = k[:]
                q.remove(g)
                for h in q:
                    s.append(h)
                    print(s)
                    s.remove(h)
                s.remove(g)
            s.remove(f)
        s.remove(e)


def fun(tt, s, n):
    for e in n:
        s.append(e)
        tt. append(s)
        m = n[:].remove(e)
        if len(m) == 1:
            return m[0]
        else:
            return fun(tt, s, m)
    tt.append(s)

# s = []
# n = [1,2,3,4,5]
# tt = []
# fun(tt, s, n)
# print(tt)


def al():
    # try:
        n = int(input())
        k = int(input())
        s = []
        t = []
        i = 1
        while i <= n:
            s.append(str(i))
            i += 1
        t.append(''.join(s))
        for i in range(len(s)):
            for j in range(len(s)):
                for e in t:
                    n_l = [a for a in e]
                    m = n_l[i]
                    n_l[i] = n_l[j]
                    n_l[j] = m
                    x = ''.join(n_l)
                    if x not in t:
                        t.append(x)
        for i in range(len(t)):
            for j in range(len(t)):
                if i == j:
                    continue
                if int(t[i]) < int(t[j]):
                    m = t[i]
                    t[i] = t[j]
                    t[j] = m
        print(t)
        print(t[k-1])
    # except:
    #     break


def merge(roomTimes):
    mark = roomTimes[:]
    for each in roomTimes:
        if each not in mark:
            continue
        for n_each in mark:
            if each != n_each:
                if each[0] <= n_each[0] and each[1] >= n_each[0]:
                    min_t = each[0]
                    if each[1] >= n_each[1]:
                        max_t = each[1]
                    else:
                        max_t = n_each[1]
                elif each[0] >= n_each[0] and each[0] <= n_each[1]:
                    min_t = n_each[0]
                    if each[1] >= n_each[1]:
                        max_t = each[1]
                    else:
                        max_t = n_each[1]
                else:
                    continue
                if each in mark:
                    mark.remove(each)
                if n_each in mark:
                    mark.remove(n_each)
                mark.append([min_t, max_t])
    return mark


if __name__ == '__main__':
    times = [[1,4],[4,5]]
    print(merge(times))
