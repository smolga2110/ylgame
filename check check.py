import pygame
import sqlite3


drawings = {1: [[0, 1, 1, 0, ],
                [0, 1, 1, 0],
                [1, 1, 1, 1],
                [0, 1, 1, 0],
                [1, 0, 0, 1]],
            2: [[1, 0, 1, 0, 1],
                [0, 1, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [1, 0, 1, 0, 1]],
            3: [[0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1]],
            4: [[0, 0, 1, 1, 0, 0, ],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0]],
            5: [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]],
            6: [[1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 0]],
            7: [[0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0]],
            8: [[0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0]],
            9: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}
cosrs = [12, 16, 17, 9, 13, 34, 19, 38, 35]
pygame.init()


class Board:
    def __init__(self, level):
        if len(level[0]) > 6:
            cell_size = 50
        else:
            cell_size = 80
        height = len(level)
        width = len(level[0])
        for i in range(1, 10):
            if level == drawings[i]:
                left = (size[0] / 2) - (width * cell_size / 2)
                top = (size[1] / 2) - (width * cell_size / 2 - 190)
            else:
                left = (size[0] / 2) - (width * cell_size / 2)
                top = (size[1] / 2) - (width * cell_size / 2)
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

    def render1(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen, pygame.color.Color("#070031"),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size,
                                      self.cell_size))
                pygame.draw.rect(screen, pygame.color.Color("black"),
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
        global flag
        global ab
        global nameExists
        cell_x = int(cell_coords[0])
        cell_y = int(cell_coords[1])
        if not (cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height):
            if self.board[cell_y][cell_x] != 1 and drawings[level][cell_y][cell_x] == 1:
                self.board[cell_y][cell_x] = (self.board[cell_y][cell_x] + 1) % 2
                ab += 1
                print('+1')
                cur = con.cursor()
            #  cur.execute("""SELECT coords FROM level_coords""")
            #  for row in cur:
            #      result = row[0]
            #      if result:
            #          nameExists = True
            #      else:
            #         nameExists = False
            # if not nameExists:
            #     cur.execute("""INSERT INTO level_coords(coords, level) VALUES (%r), (%s)""",
            #                 (tuple(self.board), id))

            # else:
            #     cur.execute("""SELECT level FROM level_coords WHERE coords = %r""", self.board)
            #     for row in cur:
            #         actualId = row[0]
            #     actualId = actualId + 1
            #     cur.execute("""UPDATE level_coords SET level = %s WHERE coords = %r;""", actualId,
            #                (tuple(self.board)))

            else:
                flag -= 1
                if flag == 2:
                    screen.blit(image_kill_heart, (760, 700))
                elif flag == 1:
                    screen.blit(image_kill_heart, (860, 700))
                elif flag == 0:
                    screen.blit(image_kill_heart, (960, 700))


def level_info(event_pos):
    # event_pos = f'{event_pos[0]} {event_pos[1]}'
    for i in range(1, 10):
        con = sqlite3.connect('nonagramm.db')
        cur = con.cursor()
        result = cur.execute('''SELECT coords
                              FROM level_coords
                              WHERE level = ?''', (i,)).fetchall()
        if len(result) != 0:
            x, y = list(map(lambda x: int(x), result[0][0].split()))
            if x <= event_pos[0] <= x + 163 and \
                    y <= event_pos[1] <= y + 163:
                return [True, i]
    return [False, None]


size = (1792, 896)
screen = pygame.display.set_mode(size)
image = pygame.image.load(
    'sprites/супер пупер заставка тыщу лет фотожопила поставьте полный балл за такое умоляю.png').convert_alpha()
image_question = pygame.image.load('sprites/нифига умный вопрос.png').convert_alpha()
image_gears = pygame.image.load('sprites/ну а это че.png').convert_alpha()
image_gears_tap = pygame.image.load('sprites/ну а это че нажали.png').convert_alpha()
image_question_tap = pygame.image.load('sprites/нифига умный вопрос нажали.png').convert_alpha()
image_button_game = pygame.image.load('sprites/кнопка игры.png').convert_alpha()
image_level_but = pygame.image.load('sprites/проверка.png').convert_alpha()
image_check_but = pygame.image.load('sprites/проверка нажали.png').convert_alpha()
screen.blit(image, (0, 0))
screen.blit(image_question, (1574, 22))
screen.blit(image_gears, (1690, 22))
screen.blit(image_button_game, ((1070, 635)))
clock = pygame.time.Clock()

first_page = True
info_page = False
second_page = False
level_page = False
flag = 0
ab = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_question, (1574, 22))
            image_helpa = pygame.image.load('sprites/катянебей это хелп.png').convert_alpha()
            screen.blit(image_helpa, (0, 0))
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = False
            info_page = True
            second_page = False
            level_page = False
            screen.blit(image_gears, (1690, 22))

        elif event.type == pygame.MOUSEBUTTONDOWN and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_question_tap, (1574, 22))

        if event.type == pygame.MOUSEBUTTONUP and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and info_page:
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and info_page:
            screen.blit(image_gears_tap, (1690, 22))

        if event.type == pygame.MOUSEBUTTONUP and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and info_page:
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = True
            info_page = False
            second_page = False
            level_page = False
            screen.blit(image, (0, 0))
            screen.blit(image_question, (1574, 22))
            screen.blit(image_gears, (1690, 22))
            screen.blit(image_button_game, ((1070, 635)))
        elif event.type == pygame.MOUSEBUTTONDOWN and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and info_page:
            image_go_back_tap = pygame.image.load('sprites/назад нажали.png').convert_alpha()
            screen.blit(image_go_back_tap, (15, 15))

        if event.type == pygame.MOUSEBUTTONUP and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_gears_tap, (1690, 22))

        if event.type == pygame.MOUSEBUTTONUP and 1070 <= event.pos[0] <= 1070 + 699 and \
                635 <= event.pos[1] <= 635 + 162 and first_page:
            image_level_spisok = pygame.image.load('sprites/заставка фона для уровней.png').convert_alpha()
            screen.blit(image_level_spisok, (0, 0))
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = False
            info_page = False
            second_page = True
            level_page = False
            screen.blit(image_question, (1574, 22))
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1070 <= event.pos[0] <= 1690 + 73 and \
                635 <= event.pos[1] <= 635 + 162 and first_page:
            image_button_game_tap = pygame.image.load('sprites/кнопка игры нажата.png').convert_alpha()
            screen.blit(image_button_game_tap, ((1070, 635)))

        if event.type == pygame.MOUSEBUTTONUP and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and second_page:
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = True
            info_page = False
            second_page = False
            level_page = False
            screen.blit(image, (0, 0))
            screen.blit(image_question, (1574, 22))
            screen.blit(image_gears, (1690, 22))
            screen.blit(image_button_game, ((1070, 635)))
        elif event.type == pygame.MOUSEBUTTONDOWN and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and second_page:
            image_go_back_tap = pygame.image.load('sprites/назад нажали.png').convert_alpha()
            screen.blit(image_go_back_tap, (15, 15))

        if event.type == pygame.MOUSEBUTTONUP and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and second_page:
            screen.blit(image_question, (1574, 22))
            screen.blit(image_question, (1574, 22))
            image_helpa = pygame.image.load('sprites/катянебей это хелп.png').convert_alpha()
            screen.blit(image_helpa, (0, 0))
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = False
            info_page = True
            second_page = False
            level_page = False
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and second_page:
            screen.blit(image_question_tap, (1574, 22))

        if event.type == pygame.MOUSEBUTTONUP and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and second_page:
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and second_page:
            screen.blit(image_gears_tap, (1690, 22))

        if event.type == pygame.MOUSEBUTTONDOWN and level_info(event.pos)[0] and second_page:
            level = level_info(event.pos)[1]
            image_level_button = pygame.image.load(f'sprites/уровень {level} нажали.png').convert_alpha()
            con = sqlite3.connect('nonagramm.db')
            cur = con.cursor()
            result = cur.execute('''SELECT coords
                                      FROM level_coords
                                      WHERE level = ?''', (level,)).fetchall()
            x, y = list(map(lambda x: int(x), result[0][0].split()))
            screen.blit(image_level_button, (x, y))
        elif event.type == pygame.MOUSEBUTTONUP and level_info(event.pos)[0] and second_page:
            level = level_info(event.pos)[1]
            image_level_button = pygame.image.load(f'sprites/уровень {level}.png').convert_alpha()
            con = sqlite3.connect('nonagramm.db')
            cur = con.cursor()
            result = cur.execute('''SELECT coords
                                                  FROM level_coords
                                                  WHERE level = ?''', (level,)).fetchall()
            x, y = list(map(lambda x: int(x), result[0][0].split()))
            screen.blit(image_level_button, (x, y))
            first_page = False
            second_page = False
            level_page = True
            board = Board(drawings[level])
            image_game_background = pygame.image.load(f'sprites\уровень {level} фон.png').convert_alpha()
            screen.blit(image_game_background, (0, 0))
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            image_kill_heart = pygame.image.load('sprites/сердце пустое.png').convert_alpha()
            image_heart = pygame.image.load('sprites/сердце полное.png').convert_alpha()
            myfont = pygame.font.SysFont('ofont.ru_President.ttf', 24)
            textsurface = myfont.render('С ПОБЕДОЙ', True, (0, 0, 0))
            print(level)
            image_level_strok = pygame.image.load(f'sprites/уровень {level} надпись.png').convert_alpha()
            image_level_but = pygame.image.load('sprites/проверка.png').convert_alpha()
            image_check_but = pygame.image.load('sprites/проверка нажали.png').convert_alpha()
            screen.blit(image_level_but, (1100, 400))
            if level == 4 or 8:
                screen.blit(image_level_strok, (690, 75))
            else:
                screen.blit(image_level_strok, (690, 130))
            a = screen.blit(image_heart, (760, 700))
            b = screen.blit(image_heart, (860, 700))
            c = screen.blit(image_heart, (960, 700))
            screen.blit(image_go_back, (15, 15))
            ab = 0
            flag = 3
            screen.blit(image_question, (1574, 22))
            screen.blit(image_gears, (1690, 22))
            board.render1()

        if event.type == pygame.MOUSEBUTTONUP and 1100 <= event.pos[0] <= 1100 + 600 and \
                400 <= event.pos[1] <= 400 + 140 and level_page:
            screen.blit(image_level_but, (1100, 400))
            if ab == cosrs[level - 1]:
                myfont = pygame.font.SysFont('ofont.ru_President.ttf', 100)
                textsurface = myfont.render('УРОВЕНЬ ПРОЙДЕН', True, (0, 0, 0))
                print('YOU WIN')
                screen.blit(textsurface, (550, 800))
                pygame.display.update()
                pygame.time.wait(4000)
                image_level_spisok = pygame.image.load('sprites/заставка фона для уровней.png').convert_alpha()
                screen.blit(image_level_spisok, (0, 0))
                image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
                screen.blit(image_go_back, (15, 15))
                first_page = False
                second_page = True
                level_page = False
                screen.blit(image_question, (1574, 22))
                screen.blit(image_gears, (1690, 22))
            else:
                print('NOPE')
        elif event.type == pygame.MOUSEBUTTONDOWN and 1100 <= event.pos[0] <= 1100 + 600 and \
                400 <= event.pos[1] <= 400 + 140 and level_page:
            screen.blit(image_check_but, (1100, 400))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and level_page and flag != 0:
            board.get_click(event.pos)
            board.render1()
        if flag == 0 and level_page:
            f2 = pygame.font.SysFont('ofont.ru_President.ttf', 100)
            image_you_lose = pygame.image.load('sprites/проиграли.png').convert_alpha()
            screen.blit(image_you_lose, (600, 760))

        if event.type == pygame.MOUSEBUTTONUP and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and level_page:
            image_level_spisok = pygame.image.load('sprites/заставка фона для уровней.png').convert_alpha()
            screen.blit(image_level_spisok, (0, 0))
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = False
            second_page = True
            level_page = False
            screen.blit(image_question, (1574, 22))
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and level_page:
            image_go_back_tap = pygame.image.load('sprites/назад нажали.png').convert_alpha()
            screen.blit(image_go_back_tap, (15, 15))

        if event.type == pygame.MOUSEBUTTONUP and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and level_page:
            screen.blit(image_question, (1574, 22))
            screen.blit(image_question, (1574, 22))
            screen.blit(image_question, (1574, 22))
            image_helpa = pygame.image.load('sprites/катянебей это хелп.png').convert_alpha()
            screen.blit(image_helpa, (0, 0))
            image_go_back = pygame.image.load('sprites/назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = False
            info_page = True
            second_page = False
            level_page = False
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and level_page:
            screen.blit(image_question_tap, (1574, 22))

        if event.type == pygame.MOUSEBUTTONUP and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and level_page:
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and level_page:
            screen.blit(image_gears_tap, (1690, 22))

    pygame.display.flip()
pygame.quit()
