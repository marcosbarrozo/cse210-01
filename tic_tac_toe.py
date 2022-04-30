'''
Tic-Tac-Toe
Author: Marcos Barrozo
'''

class TicTacToe:
    board = [" " for x in range(9) ]

    def drawn_board(self):
        copy_board = self.board[:]
        for i in range(len(copy_board)):
            if copy_board[i] == " ":
                copy_board[i] = i+1
        print()
        print(' {} | {} | {}'.format(copy_board[0],copy_board[1],copy_board[2]))
        print('-----------')
        print(' {} | {} | {}'.format(copy_board[3],copy_board[4],copy_board[5]))
        print('-----------')
        print(' {} | {} | {}'.format(copy_board[6],copy_board[7],copy_board[8]))
        print()

    def is_winner(self,le):     
        return (self.board[0] == le and self.board[1] == le and self.board[2] == le
    	or self.board[3] == le and self.board[4] == le and self.board[5] == le
    	or self.board[6] == le and self.board[7] == le and self.board[8] == le
    	or self.board[0] == le and self.board[3] == le and self.board[6] == le
    	or self.board[1] == le and self.board[4] == le and self.board[7] == le
    	or self.board[2] == le and self.board[5] == le and self.board[8] == le
    	or self.board[0] == le and self.board[4] == le and self.board[8] == le
    	or self.board[2] == le and self.board[4] == le and self.board[6] == le)

    def player(self):
        count_x = 0
        count_o = 0
    
        for i in self.board:
            if i == "X":
                count_x += 1
            if i == "O":
                count_o += 1
        if count_x == count_o:
            return "X"
        elif count_x > count_o:
            return "O"
    
    def move(self,position):
        position -= 1
        self.board[position] = self.player();

    def winner_or_draw(self):
        count = 0
        for i in self.board:
            if i == " ":
                count += 1   
        return count == 0 or self.is_winner("X") or self.is_winner("O")

    def validate_move(self,move):
        move -= 1
        if self.board[move] == " ":
            return True
        else:
            return False

def main():
    game = TicTacToe()
    while(not game.winner_or_draw()):
        game.drawn_board()
        try:
            if game.player() == "X":
                move = int(input("X's turn to choose a square (1-9): "))
            elif game.player() == "O":
                move = int(input("O's turn to choose a square (1-9): "))

            if move < 1 or move > 9:
                print("\nNumber out of range, please enter a valid digit! (1-9)")
                print()
                continue
            if not game.validate_move(move):
                print("\nSorry, this square is not avalible!")
                print()
                continue
        except ValueError:
            print('\nPlease enter a valid digit (1 - 9)')
            print()
            continue

        game.move(move)

        if game.winner_or_draw():
            if game.is_winner("X"):
                print("X Won!")
            elif game.is_winner("O"):
                print("O Won!")
            else:
                print("Draw!")

    print("Good game. Thanks for playing!")

if __name__ == "__main__":
    main()