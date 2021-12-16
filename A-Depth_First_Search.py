import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().rstrip().split())
maze = [list(input().rstrip()) for i in range(H)]
reached = [[False]*W for i in range(H)]
 
def search(y, x):
    if y<0 or H<=y or x<0 or W<=x or maze[y][x] == '#':
        return
    if reached[y][x] == True:
        return
    reached[y][x] = True
    search(y+1, x)
    search(y-1, x)
    search(y, x+1)
    search(y, x-1)

for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            start_i, start_j = i,j
        if maze[i][j] == 'g':
            goal_i, goal_j = i,j

search(start_i,start_j)
print("Yes" if reached[goal_i][goal_j] else "No")

# import sys
# sys.setrecursionlimit(10**6)
 
# H,W=map(int,input().split())
# c=[input() for i in range(H)]
 
# flag=[[False]*W for i in range(H)]
# moves=[[0,1],[1,0],[0,-1],[-1,0]]
 
# def dfs(i,j):
#     if not(0<=i<H) or not(0<=j<W) or c[i][j]=="#" or flag[i][j]:
#         return
#     flag[i][j]=True
#     for move in moves:
#         dfs(i+move[0],j+move[1])
 
# for i in range(H):
#     for j in range(W):
#         if c[i][j]=="s":
#             start_i,start_j=i,j
#         if c[i][j]=="g":
#             goal_i,goal_j=i,j
 
# dfs(start_i,start_j)
# print("Yes" if flag[goal_i][goal_j] else "No")
