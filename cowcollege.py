n_cows = int(input())
t_cows = list(map(int, input().split()))
t_cows.sort()

max_rev = 0
opt_t = 0

for i in range(n_cows):
    temp_t = t_cows[i]
    temp_rev = temp_t * (n_cows - i)
    if max_rev < temp_rev:
        max_rev = temp_rev
        opt_t = temp_t
    elif max_rev == temp_rev:
        if opt_t != 0 and temp_t < opt_t:
            opt_t = temp_t


print(str(max_rev) + " " + str(opt_t))
