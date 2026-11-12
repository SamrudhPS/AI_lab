
import heapq

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal = state[i] - 1
            distance += abs(i // 3 - goal // 3) + abs(i % 3 - goal % 3)
    return distance

def is_solvable(state):
    nums = [x for x in state if x != 0]
    inversions = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inversions += 1
    return inversions % 2 == 0

def astar(start):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    if not is_solvable(start):
        print("Puzzle is not solvable")
        return

    pq = [(heuristic(start), 0, start)]
    visited = {start: 0}
    parent = {}

    while pq:
        f, g, current = heapq.heappop(pq)

        if g != visited[current]:
            continue

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()

            print("\nSolution found!")
            print("Number of moves:", len(path) - 1)

            for board in path:
                for i in range(0, 9, 3):
                    print(*board[i:i+3])
                print()
            return

        pos = current.index(0)
        x, y = divmod(pos, 3)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos = nx * 3 + ny
                new_state = list(current)
                new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
                new_state = tuple(new_state)

                new_g = g + 1

                if new_state not in visited or new_g < visited[new_state]:
                    visited[new_state] = new_g
                    parent[new_state] = current
                    new_f = new_g + heuristic(new_state)
                    heapq.heappush(pq, (new_f, new_g, new_state))

    print("No solution found")

# Main program
print("Enter 9 numbers (use 0 for blank):")
try:
    start = tuple(map(int, input().split()))

    if len(start) != 9 or sorted(start) != list(range(9)):
        print("Invalid input! Enter numbers from 0 to 8 exactly once.")
    else:
        astar(start)

except ValueError:
    print("Please enter only numbers.")