import datetime


def trans_bits():
    a = int(input())
    begin_time = datetime.datetime.now()
    c = 0
    while a:
        b = a % 2
        if b:
            c += 1
        a = int(a / 2)
    end_time = datetime.datetime.now()
    d_time = end_time - begin_time
    print("运行时间:%f" % d_time.total_seconds())
    return c


def get_sum(n, m):
    s = 0
    while (n > 0) and (m > 0):
        s += n + m
        n -= 1
        m -= 1
    return s


def f(n, m):
    if (n == 0) or (m == 0):
        return 1
    else:
        return f(n-1,m)+f(n,m-1)


def level():
    s = input()
    l = len(s)
    p = 0
    d = 0
    lw = 0
    up = 0
    f = 0
    t = ['0', '0', '0', '0']
    if l < 5:
        p += 5
    elif l < 8:
        p += 10
    else:
        p += 25
    for i in range(0, l):
        if s[i].isdigit():
            t[0] = '1'
            if d < 20:
                d += 10
        elif s[i].isupper():
            t[1] = '1'
            if lw < 10:
                lw += 10
        elif s[i].islower():
            t[2] = '1'
            if up < 10:
                up += 10
        else:
            t[3] = '1'
            if f == 10:
                f = 25
            elif f == 0:
                f = 10
    p += d + lw + up + f
    t_s = ''.join(t)
    if t_s == '1111':
        p += 5
    elif t_s == '1011' or t_s == '1101':
        p += 3
    elif t[0] and t_s[1:2] != '00':
        p += 2
    if p >= 90:
        print('VERY_SECURE')
    elif p >= 80:
        print('SECURE')
    elif p >= 70:
        print('VERY_STRONG')
    elif p >= 60:
        print('STRONG')
    elif p >= 50:
        print('AVERAGE')
    elif p >= 25:
        print('WEAK')
    else:
        print('VERY_WEAK')


def s_one():
    n = int(input())
    c = 0
    m = 0
    while n:
        if (n % 2):
            c += 1
            if c > m:
                m = c
        else:
            c = 0
        n = int(n / 2)
    print(m)


def m_len():
    while True:
        try:
            n = input()
            c_m = 0
            for i in range(0, len(n) - 1):
                c = 0
                j = i - 1
                m = i + 1
                if n[i] == n[m]:
                    j = i
                elif n[i] == n[j]:
                    m = i
                else:
                    c = 1
                while (j > 0) and (m < len(n)):
                    if n[j] == n[m]:
                        c += 2
                    else:
                        break
                    j -= 1
                    m += 1
                if c > c_m:
                    c_m = c
            print(c_m)
        except:
            break


def get_one(arr):
    if len(arr) == 1:
        return arr[0]


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


def t1():
    n = input().split()
    s = []
    f = get_list(s, n)


def get_list(n1, n2):
    # while len(n2):
    if len(n1) == 0:
        for e in n2:
            n1.append([e])
    else:
        for e1 in n1:
            for e2 in n2:
                x = e1[:]
                x.append(e2)
                e1.append(x)
    return n1


def get_upper_count():
    # try:
    n = input()
    c = 0
    for i in n:
        if i.isalpha():
            if i.isupper():
                c += 1
    print(c)
    # except:
    #     break



def point24():
    p = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    n = input().split()
    if ('joker' in n) or ('JOKER' in n):
        print('ERROR')
    else:
        for i in range(n):
            if n[i] in p.keys():
                n[i] = p[n[i]]
    a, b, c, d = map(int, n)

    s = [0, 0, 0, 0]
    for i in range(4):
        for e in n:
            s[i] = e


if __name__ == '__main__':
    get_upper_count()
    # t()
#     # print(trans_bits())
#     # while True:
#     #     for n in range(1, 100):
#     #         for m in range(1, 100):
#     #             # n, m = map(int, input().split())
#     #             s1 = f(n, m)
#     #             s2 = get_sum(n, m)
#     #             if s1 != s2:
#     #                 print(n, m, s1, s2)
#     # level()
#     s_one()
