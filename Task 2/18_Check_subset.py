

def checker():
    x = int(input())
    s1 = set(map(int, input().split()))
    y = int(input())
    s2 = set(map(int, input().split()))
    l = []
    for i in s1:
        if i in s2:
            l.append(i)
    l = set(l)
    if l == s1:
        print(True)
    else:
        print(False)

T = int(input())
for i in range(T):
    checker()