import tkinter as tk


class GameCanvas(tk.Canvas):
	def __init__(self, root: tk.Tk):
		super().__init__()
		
		self.master = root
		self.pack(fill=tk.BOTH, expand=1)
		self.bind("<Button-1>", self.click)

		self.board = [['' for _ in range(3)] for _ in range(3)]
		self.current_player = 'X'
		self.drawUi()

	def drawUi(self):
		self.create_line(100, 0, 100, 300, width=2)
		self.create_line(200, 0, 200, 300, width=2)
		self.create_line(0, 100, 300, 100, width=2)
		self.create_line(0, 200, 300, 200, width=2)

	def draw_mark(self, x, y):
		if self.current_player == 'X':
			self.create_line(x * 100 + 10, y * 100 + 10, x * 100 + 90, y * 100 + 90, width=2, fill="blue")
			self.create_line(x * 100 + 10, y * 100 + 90, x * 100 + 90, y * 100 + 10, width=2, fill="blue")
		else:
			self.create_oval(x * 100 + 10, y * 100 + 10, x * 100 + 90, y * 100 + 90, width=2, outline="green")


	def check_winner(self) -> bool:
		for row in self.board:
			if row[0] == row[1] == row[2] != '':
				return True
		
		for col in range(3):
			if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
				return True
		
		if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
				return True
		if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
				return True
		return False
		
	def click(self, event: tk.Event):
		x, y = event.x // 100, event.y // 100
		
		if self.board[y][x] == '':
			self.board[y][x] = self.current_player
			self.draw_mark(x, y)

			if self.check_winner():
				self.create_text(150, 150, text=f"{self.current_player} wins!", font=('Arial', 24), fill="red")
				self.unbind("<Button-1>")
			elif all(cell != '' for row in self.board for cell in row):
				self.create_text(150, 150, text="Draw!", font=('Arial', 24), fill="red")
				self.unbind("<Button-1>")
			else:
				self.current_player = 'O' if self.current_player == 'X' else 'X'

class Window(tk.Tk):
	def __init__(self) -> None:
		super().__init__()
		self.window_setting()
		
		GameCanvas(self)

	def window_setting(self) -> None:
		self.title("Крестики нолики")
		self.geometry("300x300")
		self.resizable(False, False)
		self.config(
			bg="#d1d5db"
		)
	
if __name__ == "__main__":
	window = Window()
	window.mainloop()
