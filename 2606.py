# #1. DFS로 풀기
# #
# n = int(input()) #컴퓨터 수
# idx = int(input()) # 네트워크 상 연결되어 있는 컴퓨터 쌍의 개수
# computer = [[] for _ in range(n+1)] #컴퓨터 연결 정보 저장하는 리스트
# virus = [0 for _ in range(n+1)] #바이러스 감염된 컴퓨터 세기 위한 리스트
# #
# for i in range(idx): # 직접 연결된 번호 쌍 저장하기 위한 반복문
#     a,b = map(int, input().split())
#     computer[a].append(b) #a와 연결되어 있는 b 삽입
#     computer[b].append(a)
# #
# # def recur(node):
# #     virus[node] = 1
# #     for nxt in computer[node]:
# #         if virus[nxt]==1:
# #             continue
# #         recur(nxt)
# #
# # recur(1)
# # print(sum(virus)-1)
#
# #2. BFS
# from collections import deque
# q = deque() #appendleft, popleft 사용하기 위해 deque사용
#
# q.append(1) #1에서 출발
#
# while len(q) > 0:
#     node = q.popleft() #큐의 첫 번쨰 것 가져감
#     print("node: ", node)
#     virus[node] = 1
#
#     # print("node: ", node)
#     for nxt in computer[node]:
#         print("nxt: ", nxt)
#         # print("node: ", node)
#         if virus[nxt] == 1:
#             continue #방문 전적있으면 그냥 넘어가기
#         q.append(nxt)
#
# print(virus)
n = int(input()) #컴퓨터 수
graph = [[] for _ in range(n+1)] #1부터 세기 때문
visited = [0 for _ in range(n+1)] #방문한 수
idx = int(input())

for _ in range(idx):
    a,b = map(int,input().split())
    #인접 컴퓨터 쓰기
    graph[a].append(b)
    graph[b].append(a)

def rec(node):
    visited[node] = 1
    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        rec(nxt)

rec(1)
# print(visited)
print(sum(visited) - 1)