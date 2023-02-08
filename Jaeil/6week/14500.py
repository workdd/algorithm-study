def solve(board, N, M):
    def check(x, y, dir):
        if x + dir[0] >= 0 and x + dir[0] < N and y + dir[1] >= 0 and y + dir[1] < M:
            return True
        return False
    
    def dfs(x, y, dir, cnt, total):
        nonlocal max_sum
        if cnt == 4:
            max_sum = max(max_sum, total)
            return
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if check(nx, ny, (dx, dy)) and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, (dx, dy), cnt + 1, total + board[nx][ny])
                visited[nx][ny] = False
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_sum = 0
    for i in range(N):
        for j in range(M):
            visited = [[False] * M for _ in range(N)]
            visited[i][j] = True
            dfs(i, j, (0, 0), 1, board[i][j])
    
    return max_sum

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solve(board, N, M))
