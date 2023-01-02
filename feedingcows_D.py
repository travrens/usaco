n = int(input())

for _ in range(n):
    n_cows, step = input().split()
    n_cows = int(n_cows)
    step = int(step)
    cows = input()
    # print(f"#cows: {n_cows}, step: {step}, cows: {cows}")
    res = ["."] * n_cows
    pos = {'H': -1, 'G': -1}
    cnt = 0
    for i in range(n_cows):
        last = pos[cows[i]]
        if last == -1 or i - last > step:
            if i + step < n_cows - 1 or (res[i] not in ['.', cows[i]]):
                last = i + step
            else:
                last = i
            pos[cows[i]] = last
            res[last] = cows[i]
            cnt += 1
    print(str(cnt))
    print(''.join(res))


# 7
# 5 0
# GHHGG
# 5 1
# GHHGG
# 5 2
# GHHGG
# 5 3
# GHHGG
# 5 4
# GHHGG
# 2 1
# GH
# 3 1
# HGH

#