
import random

def cost(board):
    conflicts = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing():
    board = [random.randint(0, 3) for _ in range(4)]

    while True:
        current = cost(board)
        if current == 0:
            return board

        best = board
        best_cost = current

        for col in range(4):
            for row in range(4):
                new_board = board.copy()
                new_board[col] = row
                c = cost(new_board)

                if c < best_cost:
                    best = new_board
                    best_cost = c

        if best_cost >= current:
            break

        board = best

    return hill_climbing()

def main():
    solution = hill_climbing()

    print("Solution:")
    for row in range(4):
        for col in range(4):
            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print("Conflicts:", cost(solution))

main()