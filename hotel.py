T=int(input())

for i in range(T):
    x=list(map(int,input().split()))
    M=x[0]
    N=x[1]
    K=x[2]
    on=[]
    off=[]
    for j in range(M):
        x=int(input())
        on.append(x)
        off.append(N-x)
    on.sort()
    off.sort()
    off=off[::-1]
    on=on[::-1]
    print(on)
    print(off)
    if M==K:
        if sum(off)>sum(on):
            maxi=sum(off)
        else:
            maxi=sum(on)
    else:
        maxi=sum(off[:K])+sum(on[:M-K])
        print(off[:K])
        print(on[:M-K])
    print(maxi)
"""
2
2 2 1
2
0
2 4 2
0
3
"""