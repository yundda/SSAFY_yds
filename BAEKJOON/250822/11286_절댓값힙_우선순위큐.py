import sys
import heapq

input = sys.stdin.readline

N = int(input())
H = []


for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(H, (abs(x), x))

    else:
        if H:
            abs_x, x = heapq.heappop(H)
            print(x)
        else:
            print(0)


# import heapq 사용
# heapq.heappush(pq, x) : 삽입
# heapq.heappop(pq) : 삭제
# pq[0] : 최소값 확인
# (우선순위1, 우선순위2, ... , 값) 튜플 형태로 우선순위 전달 -> 우선순위 작은 게 먼저 나옴


# JAVA
# JAVA의 PriorityQueue는 생성자에 Comparator를 넘겨서 우선순위를 정함
# PriorityQueue<Integer> myQueue = new PriorityQueue<>((x1,x2)->{ ~~~ return 양수, 음수, 0 })
# return (-) : x1 우선 순위
# return (+) : x2 우선 순위
# return 0  : x1, x2 우선 순위 동일
