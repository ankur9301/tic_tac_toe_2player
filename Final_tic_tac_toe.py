import os

class Game:
    def __init__(self):
        self.board = {str(num): ' ' for num in range(1, 10)}
        self.player1 = None
        self.player2 = None
        self.active_player = None
        self.player1_moves = set()
        self.player2_moves = set()
        self.winning_combinations = [
            {'7', '8', '9'}, {'4', '5', '6'}, {'1', '2', '3'},
            {'7', '4', '1'}, {'8', '5', '2'}, {'9', '6', '3'},
            {'7', '5', '3'}, {'9', '5', '1'}
        ]
        self.all_moves = {}

    def initiate(self):
        print("Welcome to Tic Tac Toe")
        while True:
            player1 = input("Player 1: Do you want to be X or O? ").upper()
            if player1 in ["X", "O"]:
                break
            print("Invalid input. Please enter either X or O")
        self.player1 = player1
        self.player2 = 'O' if player1 == 'X' else 'X'
        print("Player 1 will go first.")
        self.play_game()

    def display_board(self):
        print(f" {self.board['7']} | {self.board['8']} | {self.board['9']} ")
        print("-----------")
        print(f" {self.board['4']} | {self.board['5']} | {self.board['6']} ")
        print("-----------")
        print(f" {self.board['1']} | {self.board['2']} | {self.board['3']} ")

    def check_winners(self, player_moves):
        return any(combination.issubset(player_moves) for combination in self.winning_combinations)

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_game(self):
        for turn in range(1, 10):
            self.clear_console()
            self.display_board()
            self.active_player = self.player1 if turn % 2 != 0 else self.player2
            player_moves = self.player1_moves if self.active_player == self.player1 else self.player2_moves
            move = input(f"Player {1 if self.active_player == self.player1 else 2} ({self.active_player}), choose a position (1-9): ")
            while move not in self.board or move in self.all_moves:
                move = input("Invalid move. Choose a different position: ")
            
            self.board[move] = self.active_player
            self.all_moves[move] = 1
            player_moves.add(move)

            if self.check_winners(player_moves):
                self.clear_console()
                self.display_board()
                print(f"Congratulations! Player {1 if self.active_player == self.player1 else 2} wins!")
                break
            elif turn == 9:
                self.clear_console()
                self.display_board()
                print("It's a draw!")

        retry = input("Do you want to restart the Game? Say yes or no: ").lower()
        if retry == "yes":
            self.__init__()
            self.initiate()

game = Game()
game.initiate()
