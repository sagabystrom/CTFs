import json

N = 8

K = ...   # paste from info
ct = ...  # paste from info

ans = []

for block in ct:
    x = []
    for j in range(N):
        xj = max(block[i] - K[i][j] for i in range(N))
        x.append(xj)
    ans.extend(x)

print(json.dumps(ans))
