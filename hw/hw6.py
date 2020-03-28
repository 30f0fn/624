# def mtf(L, x):
#     found = L.index(x)
#     L[found], L[0] = L[0], L[found]

def mtf(L, S):
    print(f"\nstep\tL\t\t\tsought\tcost")
    cost = 0
    for i, x in enumerate(S):
        # print(f"seeking {x} in {L}...")
        loc = L.index(x)
        cost += loc + 1
        while loc != 0:
            L[loc], L[loc-1] = L[loc-1], L[loc]
            loc -= 1
            cost += 1
        print(f"{i+1}\t{L}\t{x}\t{cost}")
    return L, cost

L = ['A', 'B', 'C', 'D']
S = ['B', 'C', 'A', 'C', 'C', 'A', 'D', 'D', 'A', 'B', 'A', 'C', 'B', 'C']

S = ['B', 'A'] * 7

mtf(L,S)


# step	L			sought	cost
# 1	['B', 'A', 'C', 'D']	B	3
# 2	['C', 'B', 'A', 'D']	C	8
# 3	['A', 'C', 'B', 'D']	A	13
# 4	['C', 'A', 'B', 'D']	C	16
# 5	['C', 'A', 'B', 'D']	C	17
# 6	['A', 'C', 'B', 'D']	A	20
# 7	['D', 'A', 'C', 'B']	D	27
# 8	['D', 'A', 'C', 'B']	D	28
# 9	['A', 'D', 'C', 'B']	A	31
# 10	['B', 'A', 'D', 'C']	B	38
# 11	['A', 'B', 'D', 'C']	A	41
# 12	['C', 'A', 'B', 'D']	C	48
# 13	['B', 'C', 'A', 'D']	B	53
# 14	['C', 'B', 'A', 'D']	C	56
