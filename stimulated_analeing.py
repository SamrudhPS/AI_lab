
import random
import math

def cost(board):
    conflicts = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def simulated_annealing():
    board = [random.randint(0, 7) for _ in range(8)]
    T = 100
    cooling = 0.99

    while T > 0.01:
        current = cost(board)

        if current == 0:
            return board

        new_board = board.copy()
        col = random.randint(0, 7)
        row = random.randint(0, 7)
        new_board[col] = row

        new_cost = cost(new_board)
        diff = new_cost - current

        if diff < 0 or random.random() < math.exp(-diff / T):
            board = new_board

        T *= cooling

    return None

def main():
    solution = simulated_annealing()

    if solution is None:
        print("No solution found")
        return

    print("Solution Found:")
    for row in range(8):
        for col in range(8):
            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("Total Conflicts:", cost(solution))

main()