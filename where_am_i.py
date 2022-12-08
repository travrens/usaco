#slicing doesnt include last one
# split doesnt work on a string
# need to use list for a string

fin = open("whereami.in", "r")
fout = open("whereami.out", "w")

n_mailboxes = int(fin.readline())
mailboxes = list(fin.readline()[:-1])
types_m = set(mailboxes)

found = False
for seg in range(1, n_mailboxes+1):
    sets = set()
    for i in range(n_mailboxes - seg + 1):
        if "".join(mailboxes[i:i+seg]) in sets:
            break
        else:
            if int(n_mailboxes - seg) == i:
                found = True
                break
            sets.add("".join(mailboxes[i:i+seg]))
    if found:
        break

fout.write(str(seg))
