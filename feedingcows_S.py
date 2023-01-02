t = int(input())

def solve():
    n, k = (int(x) for x in input().split())
    cows = input()
    patches = ['.'] *n
    h_LastSeen = -1
    g_LastSeen = -1
    for i, cow in enumerate(cows):
        if cow == "G" and g_LastSeen < i:
            if i + k >= len(patches):
                if patches[i] != '.':
                    patches[i-1] = "G"
                else:
                    patches[i] = "G"
                g_LastSeen = n
            else:
                patches[i+k] = 'G'
                g_LastSeen = i + 2*k
        elif cow == 'H' and h_LastSeen < i:
            if i + k >= len(patches):
                if patches[i] != '.':
                    patches[i-1] = "H"
                else:
                    patches[i] = "H"
                h_LastSeen = n
            else:
                patches[i+k] = 'H'
                h_LastSeen = i + 2*k
    print(n - patches.count('.'))
    print("".join(patches))

for _ in range (t): solve()