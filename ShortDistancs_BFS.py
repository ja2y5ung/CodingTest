from collections import deque
def solution(maps):
    answer = -1
    row = len(maps)
    col = len(maps[0])

    last_x = 0
    last_y = 0

    visited = [[False]*col for _ in range(row)]
    direction = [(0,-1),(0,1),(-1,0),(1,0)]

    q = deque()
    q.append((0, 0, 1))

    while q:
        cur_x, cur_y, cur_length = q.popleft()
        if cur_x == row-1 and cur_y == col-1:
            return cur_length
        for dx, dy in direction:
            next_x = cur_x + dx
            next_y = cur_y + dy
            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                if maps[next_x][next_y] != 0 and not visited[next_x][next_y]:
                    q.append((next_x, next_y, cur_length + 1))
                    visited[next_x][next_y] = True
    if not visited[-1][-1]:
        return answer
    answer = cur_length

    return answer
