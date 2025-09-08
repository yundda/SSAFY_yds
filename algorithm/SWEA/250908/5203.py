import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    p1 = [0] * 10
    p2 = [0] * 10




    def triple(card, n):
        player = p1 if n == 1 else p2
        if player[card] == 2:
            return True
        else:
            player[card] += 1
            return False

    def check_run(card,n):
        player = p1 if n == 1 else p2

        if card > 1 and player[card-2] * player[card - 1] != 0:
            return True
        if 0 < card < 9 and player[card-1] * player[card + 1] != 0:
            return True
        if card < 8 and player[card+1] * player[card + 2] != 0:
            return True
        return False
        


    for i in range(6):
        card1 = cards[i*2]
        if triple(card1,1) or check_run(card1,1):
            ans = 1
            break

        card2 = cards[i*2 + 1]
        if triple(card2,2) or check_run(card2,2):
            ans = 2
            break   
    else:
        ans = 0


    print(f'#{tc} {ans}')