import pygame

drawings = {1: [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]],
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None}

pygame.init()


class Board:
    # создание поля
    def __init__(self, width):
        height = width
        cell_size = 50
        left = (size[0] / 2) - (width * cell_size / 2)
        top = (size[0] / 2) - (width * cell_size / 2)
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        self.left = 0
        self.top = 0
        self.cell_size = 0
        self.set_view(left, top, cell_size)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen, pygame.color.Color("pink"),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size,
                                      self.cell_size))
                pygame.draw.rect(screen, pygame.color.Color("white"),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell_coords):
        cell_x = int(cell_coords[0])
        cell_y = int(cell_coords[1])
        if not(cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height):
            self.board[cell_y][cell_x] = (self.board[cell_y][cell_x] + 1) % 2


size = (500, 500)
screen = pygame.display.set_mode(size)

board = Board(len(drawings[1]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
