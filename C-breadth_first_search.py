maze_height, maze_width = map(int, input().rstrip().split())
start_y, start_x = map(int, input().rstrip().split())
goal_y, goal_x = map(int, input().rstrip().split())

maze = [list(input().rstrip()) for i in range(maze_height)]
maze[start_y-1][start_x-1] = 's'

pos = [[start_y-1, start_x-1, 0]]

while len(pos) > 0:
    y, x, depth = pos.pop(0)

    # ゴールに着くと終了
    if (goal_y-1 == y) and (goal_x-1 == x):
        print(depth)
        break

    # 上下左右を探索
    if (maze[y-1][x] == '.') or (maze[y-1][x] == 'g'):
        # 探索済みとしてセット
        maze[y-1][x] = '*'
        pos.append([y-1, x, depth+1]) # 上に移動
    if (maze[y+1][x] == '.') or (maze[y+1][x] == 'g'):
        maze[y+1][x] = '*'
        pos.append([y+1, x, depth+1]) # 下に移動
    if (maze[y][x-1] == '.') or (maze[y][x-1] == 'g'):
        maze[y][x-1] = '*'
        pos.append([y, x-1, depth+1]) # 左に移動
    if (maze[y][x+1] == '.') or (maze[y][x+1] == 'g'):
        maze[y][x+1] = '*'
        pos.append([y, x+1, depth+1]) # 右に移動