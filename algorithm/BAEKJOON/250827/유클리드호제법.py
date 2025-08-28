N, M = map(int,input().split())

def euc(big,small):
    if big % small == 0:
        print(small)
        return
    euc(small, big % small)
    

euc(max(N,M),min(N,M))