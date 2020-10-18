from collections import deque
def valid(state, col):
    for i in range(len(state)):
        if state[i] == col or state[i] == col - len(state) + i or state[i] == col + len(state) - i:
            return False
    return True

size = 5
queue = deque((col,) for col in range(size))
while queue:
    board_state = queue.popleft()
    if len(board_state) == size:
        print('solution:', board_state)
        break
    for col in range(size):
        if not valid(board_state, col):
            continue
        next_pos = board_state + (col,)
        queue.append(next_pos)