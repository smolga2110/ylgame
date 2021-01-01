import pygame

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
                pygame.draw.rect(screen, pygame.color.Color("white"),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)



size = (500, 500)
screen = pygame.display.set_mode(size)

board = Board(3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
pygame.quit()
