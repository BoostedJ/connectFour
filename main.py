import sys
import operator

# x increment = 4
# y increment = 8
# board[y][x]
# reminder board[4][2] is first
# reminder board[44][26] is last


class ConnectFour:

    def __init__(self, grid_width=7, grid_height=6):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.curr_round = 0

        self.board = []
        self.icons = ['┼', '─', '│', ' ']
        self.pieces = ['X', 'O']
        self.board_create()

    def board_create(self):
        for y in range(self.grid_height * 4 + 1):
            col = []
            if y % 4 == 0:
                for x in range(self.grid_width * 4 + 1):
                    if x % 4 == 0:
                        col.append(self.icons[0])
                    else:
                        col.append(self.icons[1])
            else:
                for x in range(self.grid_width * 4 + 1):
                    if x % 4 == 0:
                        col.append(self.icons[2])
                    else:
                        col.append(self.icons[3])
            self.board.append(col)
            self.board.append("\n")
        self.display_board()

    def display_board(self):
        for i in range(self.grid_width):
            print(f"  {i + 1} ", end='')
        print()

        for row in self.board:
            for item in row:
                print(item, end='')

    def board_place(self, piece, column):
        if piece != "X" or piece != "O":
            if column-1 < self.grid_width:
                column = 2 + (4 * (column-1))
                for row in range(44, 3, -8):
                    if self.board[row][column] == ' ':
                        self.board[row][column] = piece
                        self.display_board()
                        self.curr_round += 1
                        if self.curr_round > 6:
                            if self.check_win(row, column, piece):
                                break
                        return
                print(f"Column {column} is full!")
            else:
                print(f"Column {column} is out of range!")

        else:
            print("Entered a non \"X\" or \"O\" character.")

    def play(self):
        starting = self.pieces[0]
        column = int(input(f"\nWelcome to Connect Four! You will be {starting}. Please enter the column you'd like to begin with\n"))
        while int(column) > self.grid_width:
            print(f"Column {column} is out of range!")
            column = input(f"Please enter a value between 1 and {self.grid_width}\n")
        self.board_place(starting, int(column))

        while self.curr_round < (self.grid_width * self.grid_height):
            column = int(input(f'Please enter a value between 1 and {self.grid_width}\n'))
            if column > self.grid_width:
                print(f"Column {column} is out of range!")
                continue
            else:
                self.board_place(self.pieces[self.curr_round % 2], column)

    # range(44, 3, -8) for rows, columns at range(2, 27, 4)
    def check_win(self, row, column, piece):
        operations = [operator.add, operator.sub]

        def counter(iterations, mode, n=0, m=0):
            count = 1
            j = k = 0
            for i in range(1, iterations):
                if mode == 'row':
                    count = 1
                    j = i
                elif mode == 'column':
                    k = i
                elif mode == 'diagonal':
                    j = i
                    k = i
                if 2 <= operations[n](row, 8 * j) <= 44 and 2 <= operations[m](column, 4 * k) <= 26:
                    if self.board[operations[n](row, 8*j)][operations[m](column, 4*k)] != piece:
                        break
                    else:
                        count += 1
                else:
                    break
            return count

        def check(count):
            if count >= 4:
                print(f'\n     {piece} has won the game!')
                sys.exit()
            else:
                return 1

        top_iter = int((44 - row)/8 + 1)
        bottom_iter = int((row - 4)/8 + 1)
        if top_iter >= 4:
            check(counter(top_iter, 'row'))

        left_iter = int((column-2)/4 + 1)
        right_iter = int((26-column)/4 + 1)
        check(counter(right_iter, 'column') + counter(left_iter, 'column', m=1) - 1)

        check(counter(top_iter, "diagonal", 0, 0) + counter(bottom_iter, "diagonal", 1, 1) - 1)
        check(counter(top_iter, "diagonal", 0, 1) + counter(bottom_iter, "diagonal", 1, 0) - 1)


def main():
    game = ConnectFour()
    game.play()


if __name__ == "__main__":
    main()
