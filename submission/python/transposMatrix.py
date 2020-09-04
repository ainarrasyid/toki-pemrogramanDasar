n = 9
L = []

for i in range(3):
    M = list(map(int, input().split()))
    L.append(M)
rez = [[L[j][i] for j in range(len(L))] for i in range(len(L[0]))] 
for row in rez: 
    print(*row) 