def problem3(input):
    N = len(input)
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    
    forest = [row[:] for row in input]
    
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0

    def can_move(x, y):
        return 0 <= x < N and 0 <= y < N and forest[x][y] <= bear_size

    def bfs(start_x, start_y):
        nonlocal honeycomb_count, time, bear_size, bear_x, bear_y
        from collections import deque

        queue = deque([(start_x, start_y, 0)])
        visited = [[False] * N for _ in range(N)]
        visited[start_x][start_y] = True

        while queue:
            x, y, dist = queue.popleft()

            if 1 <= forest[x][y] < bear_size:
                honeycomb_count += 1
                time += dist
                forest[x][y] = 0  
                
                if honeycomb_count == bear_size:
                    bear_size += 1
                    honeycomb_count = 0
                    bear_x, bear_y = x, y  

                
                queue = deque([(bear_x, bear_y, 0)])  
                visited = [[False] * N for _ in range(N)]
                visited[bear_x][bear_y] = True
                continue

            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if can_move(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    
    
    bfs(bear_x, bear_y)

    return time


input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
result = problem3(input)


assert result == 14
print("정답입니다.")
