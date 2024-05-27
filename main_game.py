import tkinter as tk
from tkinter import messagebox
import user_data

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("3 en Raya")
        self.board = [' '] * 9
        self.player = 'X'
        self.username1 = user_data.get_username(1)
        self.username2 = user_data.get_username(2)
        self.scores = user_data.load_scores()
        self.score1 = user_data.get_score(self.username1, self.scores)
        self.score2 = user_data.get_score(self.username2, self.scores)
        self.game_over = False
        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text=' ', font=('normal', 20), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.status_label = tk.Label(self.root, text="", font=('normal', 20))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def on_button_click(self, index):
        if not self.game_over and self.board[index] == ' ':
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_win():
                self.end_game(f"¡Felicidades, {self.get_current_username()}! ¡Has ganado!")
                if self.player == 'X':
                    self.score1 += 1
                    user_data.update_score(self.username1, self.score1, self.scores)
                else:
                    self.score2 += 1
                    user_data.update_score(self.username2, self.score2, self.scores)
                self.update_status()
            elif self.is_board_full():
                self.end_game("¡Es un empate!")
            else:
                self.switch_player()
                self.update_status()

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                self.game_over = True
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def switch_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def get_current_username(self):
        return self.username1 if self.player == 'X' else self.username2

    def update_status(self):
        if not self.game_over:
            self.status_label.config(text=f"{self.username1} (X): {self.score1} - {self.username2} (O): {self.score2}")

    def end_game(self, message):
        messagebox.showinfo("Fin del juego", message)
        self.game_over = True

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
