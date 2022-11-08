
"""
CS664 Lab1 Tic Tac Toe
Luke Arpino larpino@bu.edu
Sai Sathvic Reddy kjssr@bu.edu
Ivan Ramadhan ivan2301@bu.edu

"""


import random

class lab1TicTacToe:

    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        print(type(player))
        print(player)
        print(f"swapping from {player}")
        if player == "0":
            print("swapping to X")
            return 'X'
        else:
            print(f"0 does not equal {player}")
        if player == 'X':
            print("swapping to 0")
            return '0'

    def show_board(self):
        print("  0 1 2")
        count = 0
        for row in self.board:
            print(count, end=" ")
            count += 1
            for item in row:
                print(item, end=" ")
            print()

    def checkfor2(self, playerx):
        # this function checks the board for any rows cols or diags where there is a blank space and 2 of the same character
        # ie a win or a block scenario
        # returns a row, col tuple at the blank space if there is a 2 in a row, or returns false if not

        n = len(self.board)

        symCount = 0  # count of player symbols in rows
        bCount = 0  # count of blank spaces

        # check rows
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == playerx:
                    symCount += 1

                elif self.board[i][j] == "-":
                    bCount += 1
                    blank = i, j


            if (symCount == 2) & (bCount == 1):
                return blank

            symCount = 0  # count of player symbols in rows
            bCount = 0  # count of blank spaces

        symCount = 0  # count of player symbols in rows
        bCount = 0  # count of blank spaces


        # check columns
        for i in range(n):
            for j in range(n):
                if self.board[j][i] == playerx:
                    symCount += 1

                elif self.board[j][i] == "-":
                    bCount += 1
                    blank = j, i


            if (symCount == 2) & (bCount == 1):
                return blank

            symCount = 0  # count of player symbols in rows
            bCount = 0  # count of blank spaces

        symCount = 0  # count of player symbols in rows
        bCount = 0  # count of blank spaces


        # check diagonal1
        for i in range(n):
            if self.board[i][i] == playerx:
                symCount += 1
            elif self.board[i][i] == "-":
                bCount += 1
                blank = i, i

        if (symCount == 2) & (bCount == 1):
            return blank

        symCount = 0  # count of player symbols in rows
        bCount = 0  # count of blank spaces

        # check diagonal2
        for i in range(n):
            if self.board[i][n - 1 - i] == playerx:
                symCount += 1
            elif self.board[i][n - 1 - i] == "-":
                bCount += 1
                blank = i, n - 1 - i


        if (symCount == 2) & (bCount == 1):
            return blank

        symCount = 0  # count of player symbols in rows
        bCount = 0  # count of blank spaces

        return False

    def agent(self, player1):
        # this function takes a player symbol,
        # and returns a position tuple representing where that player should place their piece

        player2 = '0'
        if player1 == '0':
            player2 = 'X'

        # check for win
        if self.checkfor2(player1):
            return self.checkfor2(player1)

        # check for block
        if self.checkfor2(player2):
            return self.checkfor2(player2)

        # take center
        if self.board[1][1] == '-':
            return 1, 1

        # take corner
        corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
        for corner in corners:
            row = corner[0]
            col = corner[1]
            if self.board[row][col] == '-':
                return row, col

        while True:
            result = random.randint(0, 2), random.randint(0, 2)
            if self.board[result[0]][result[1]] == "-":
                break

        return result

    def start(self):

        print("Human is X. Flipping coin.")

        if self.get_random_first_player() == 1:
            player = 'X'
        else:
            player = '0'


        while True:

            self.show_board()
            print(f"Player {player} turn")

            if player == 'X':
                #taking user input
                row, col = list(
                    map(int, input("Enter row and column numbers to fix spot [format: row space col] : ").split()))
                print()
                self.fix_spot(row, col, player)
            else:
                row, col = self.agent('0')
                self.fix_spot(row, col, player)


            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            print("swapping the turn")
            if player == 'X':
                player = '0'
            elif player == '0':
                player = 'X'


        # showing the final view of board
        print()
        self.show_board()


# starting the game
lab1 = lab1TicTacToe()
lab1.start()
