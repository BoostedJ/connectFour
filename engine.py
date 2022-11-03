import connectfour as cf
import random
random.seed(random.randint(0, 1000))


def play_against_ai():
    game = cf.ConnectFour()


def move_is_valid(board, move):
    if move < 1 or move > (len(board.grid_width)):
        return False

    if board[move-1][0] != ' ':
        return False

    return True


def available_move(board):
    moves = []
    for i in range(1, board.grid_width):
        if move_is_valid(board, i):
            moves.append(i)
    return moves


if __name__ == '__main__':
    play_against_ai()
