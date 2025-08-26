# fast io & 상수
import sys, heapq
input = sys.stdin.readline
INF = 10**18; MOD = 1_000_000_007

# BFS
from collections import deque
def bfs(start, g, n):
    dist = [-1]*n; dist[start]=0
    q=deque([start])
    while q:
        u=q.popleft()
        for v in g[u]:
            if dist[v]==-1:
                dist[v]=dist[u]+1; q.append(v)
    return dist

# Dijkstra
def dijkstra(s, g, n):
    dist=[INF]*n; dist[s]=0
    pq=[(0,s)]
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]: continue
        for v,w in g[u]:
            nd=d+w
            if nd<dist[v]:
                dist[v]=nd; heapq.heappush(pq,(nd,v))
    return dist

# Bellman-Ford (neg. cycle -> None)
def bellman_ford(s, edges, n):
    dist=[INF]*n; dist[s]=0
    for _ in range(n-1):
        updated=False
        for u,v,w in edges:
            if dist[u]!=INF and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w; updated=True
        if not updated: break
    for u,v,w in edges:
        if dist[u]!=INF and dist[u]+w<dist[v]: return None
    return dist