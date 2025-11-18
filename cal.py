L1, r1,  L2, r2 = map(int, input().split())
start = max(L1, L2)
end = min(r1, r2)
if start > end:
    print(-1)
else:
    print(start,end)     