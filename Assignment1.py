from collections import deque
import random
import math
import time
from copy import deepcopy
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

# ----------------- Heuristic - Simulated Annealing --------------

def initState(n):
    lst = list(range(n))
    random.shuffle(lst)
    return lst

def nextState(state):
    lst = deepcopy(state)
    i, j = random.sample(range(len(lst)), 2)
    lst[i], lst[j] = lst[j], lst[i]
    return lst

def constFunc(state):
    heuristic_result = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(state[i] - state[j]) in [abs(i - j), 0]:
                heuristic_result += 1

    return heuristic_result

def simulatedAnnealing(N):
    global isCompleted
    temperature = 4000*N
    
    alpha = 0.99
    current_state = initState(N)
    current_cost = constFunc(current_state)

    while temperature > 0:
        temperature *= alpha
        next_state = nextState(current_state)
        next_cost = constFunc(next_state)
        delta_E = next_cost - current_cost

        if delta_E < 0 or random.uniform(0, 1) < math.exp(-delta_E / temperature):
            current_state = next_state
            current_cost = constFunc(current_state)

        if current_cost == 0:
            isCompleted = True
            printBoard(current_state)
            break

    if isCompleted is False:
        print("Failed")

def printBoard(lst):
    print("Heuristic:")
    print(lst)

# ---------------------- >> Queens ---------------
lst = []
def nQueenHundredTh(N):
    r = N%12
    for i in range(2, N+1, 2):
        lst.append(i)

    if r == 3 or r == 9:
        lst.remove(2)
        lst.append(2)

    _count = len(lst)

    for i in range(1, N+1,2):
            lst.append(i)

    if r == 8:
        for i in range(_count, len(lst), 2):
           
            lst[i], lst[i+1] = lst[i+1], lst[i]
    
    elif r == 2:
        lst[_count], lst[_count + 1] = lst[_count + 1], lst[_count]
        lst.remove(5)
        lst.append(5)
    
    elif r == 3 or r == 9:
        lst.remove(1)
        lst.remove(3)
        lst.append(1)
        lst.append(3)
        
# ------------------------ Main ----------------------

start = time.time()
print("Nhập N")
N = int(input())
isCompleted = False

if N < 10:
    result = [-1]*N
    findResultDFS(0)
    findResultBFS(N)
    simulatedAnnealing(N)

elif N > 9 and N < 100:
    simulatedAnnealing(N)
    
else:
    nQueenHundredTh(N)
    print(lst)

print("Runtime in second:", time.time() - start)
