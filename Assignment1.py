from collections import deque
# ----------------------------- DFS -----------------------------

def printResult(result):
    global N
    for i in range(N):
        print('* '*result[i] + '^ ' + '* '*(N-result[i]-1))

def isSafe(row, col):
    global isCompleted, N, result
    for i in range(row):
        if result[i] == col or result[i] == col - row + i or result[i] == col + row - i:
            return False
    return True

def findResultDFS(row):
    global isCompleted, N, result
    if row == N:
        print('DFS:')
        printResult(result)
        isCompleted = True
        return
    for i in range(N):
        if isSafe(row, i):
            result[row] = i
            findResultDFS(row + 1)
        if isCompleted:
            return
# ----------------------------- BFS -----------------------------

def valid(state, col):
    for i in range(len(state)):
        if state[i] == col or state[i] == col - len(state) + i or state[i] == col + len(state) - i:
            return False
    return True

def findResultBFS(size):
    queue = deque((col,) for col in range(size))
    while queue:
        board_state = queue.popleft()
        if len(board_state) == size:
            print('BFS:')
            printResult(board_state)
            break
        for col in range(size):
            if not valid(board_state, col):
                continue
            next_pos = board_state + (col,)
            queue.append(next_pos)
# ----------------------------- Main -----------------------------

isCompleted = False
print("Nhập N")
N = int(input())
result = [-1]*N
findResultDFS(0)
findResultBFS(N)