from tkinter import *

CANVAS_SIZE = 600
FIGURE_SIZE = 200
ROTIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

X = 'player 1'
O = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        # self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    def build_grid(self, grid_color):
        for i in range(1, ROTIO):

            self.canvas.create_line(i * FIGURE_SIZE, 0, i * FIGURE_SIZE, CANVAS_SIZE, fill=grid_color, width=2)
            self.canvas.create_line(0, i * FIGURE_SIZE, CANVAS_SIZE, i * FIGURE_SIZE,fill=grid_color, width=2)

    
    def render_cross(self, posX, posY):
        pass
    def render_circle(self, posX, poxY):
        pass

    def winner(self, player=None):
        pass

    def render_cross(self,posX,posY):
        f_size = self.figure_size
        self.canvas.create_line(posX, posY, posX + f_size, posY + f_size, fill='white' , width=5)
        self.canvas.create_line(posX + f_size, posY, posX, posY + f_size, fill='white' , width=5)

    def render_circle(self, posX, posY):
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX+5, posY+5, posX + f_size, posY + f_size, outline='white', width=5)

game_v1 = Board(start_player=FIRST_PLAYER)

game_v1.build_grid('white')


game_v1.mainloop()


