t = int(input())


def pour(t1, t2, t3, moves, n_moves):
    # end
    if len(set(t1)) == 1 and len(set(t2)) == 1 and len(t3) == 0:
        global final
        final = min(n_moves, final)
        global q
        if q != 1:
            final_list = moves
        return

    if len(t1) > 0:
    if len(t2) > 0:
    if len(t3) > 0:
        type = t3[-1]
        iterations = 0
        for i in range(len(t3)-1, -1, -1):
            if t3.pop() == type:
                iterations += 1
            else:
                if type == "1":
                    t3.append("2")
                else:
                    t3.append("1")
                break
        for i in range(iterations):
            moves.append("3 1")
            t1.append(type)
        if q != 1:
            moves.append("3 2")
        pour(t1, t2, t3, moves, n_moves)

        for i in range(iterations):
            t2.append(type)
        if q != 1:
            moves.append("3 1")
        pour(t1, t2, t3, moves, n_moves)

for _ in range(t):
    p, q = list(int(x) for x in input().split())
    final = 0
    final_list = []
    t1 = list(input())
    t2 = list(input())

    pour(t1, t2, [0], [], 0)

    print(final)
    if q != 1:
        for move in final_list:
            print(move)
        print("\n")





