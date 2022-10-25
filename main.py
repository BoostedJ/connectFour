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
                for i in range(44, 3, -8):
                    if self.board[i][column] == ' ':
                        self.board[i][column] = piece
                        self.display_board()
                        self.curr_round += 1
                        return
                print(f"Column {column} is full!")
            else:
                print(f"Column {column} is out of range!")

        else:
            print("Entered a non \"X\" or \"O\" character.")

    def play(self):
        valid_pieces = ['X', 'O']
        starting = valid_pieces[0]
        column = int(input(f"\nWelcome to Connect Four! You will be {starting}. Please enter the column you'd like to begin with\n"))
        while int(column) > self.grid_width:
            print(f"Column {column} is out of range!")
            column = input(f"Please enter a value between 1 and {self.grid_width}\n")
        self.board_place(starting, int(column))

        while self.curr_round < (self.grid_width * self.grid_height):
            column = input(f"Please enter a value between 1 and {self.grid_width}\n")
            self.board_place(valid_pieces[self.curr_round % 2], int(column))


def main():
    game = ConnectFour()
    game.play()


if __name__ == "__main__":
    main()
