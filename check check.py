import pygame

size = (1792, 896)
screen = pygame.display.set_mode(size)
image = pygame.image.load(
    'супер пупер заставка тыщу лет фотожопила поставьте полный балл за такое умоляю.png').convert_alpha()
image_question = pygame.image.load('нифига умный вопрос.png').convert_alpha()
image_gears = pygame.image.load('ну а это че.png').convert_alpha()
image_gears_tap = pygame.image.load('ну а это че нажали.png').convert_alpha()
image_question_tap = pygame.image.load('нифига умный вопрос нажали.png').convert_alpha()
image_button_game = pygame.image.load('кнопка игры.png').convert_alpha()
screen.blit(image, (0, 0))
screen.blit(image_question, (1574, 22))
screen.blit(image_gears, (1690, 22))
screen.blit(image_button_game, ((1070, 635)))
clock = pygame.time.Clock()

first_page = True
second_page = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_question, (1574, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_question_tap, (1574, 22))

        if event.type == pygame.MOUSEBUTTONUP and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_gears, (1690, 22))
        elif event.type == pygame.MOUSEBUTTONDOWN and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73 and first_page:
            screen.blit(image_gears_tap, (1690, 22))

        if event.type == pygame.MOUSEBUTTONUP and 1070 <= event.pos[0] <= 1070 + 699 and \
                635 <= event.pos[1] <= 635 + 162 and first_page:
            screen.blit(image_button_game, ((1070, 635)))
            image_level_spisok = pygame.image.load('заставка фона для уровней.png').convert_alpha()
            screen.blit(image_level_spisok, (0, 0))
            first_page = False
            second_page = True
        elif event.type == pygame.MOUSEBUTTONDOWN and 1070 <= event.pos[0] <= 1690 + 73 and \
                635 <= event.pos[1] <= 635 + 162 and first_page:
            image_button_game_tap = pygame.image.load('кнопка игры нажата.png').convert_alpha()
            screen.blit(image_button_game_tap, ((1070, 635)))

        if event.type == pygame.MOUSEBUTTONUP and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and second_page:
            image_go_back = pygame.image.load('назад.png').convert_alpha()
            screen.blit(image_go_back, (15, 15))
            first_page = True
            second_page = False
            screen.blit(image, (0, 0))
            screen.blit(image_question, (1574, 22))
            screen.blit(image_gears, (1690, 22))
            screen.blit(image_button_game, ((1070, 635)))
        elif event.type == pygame.MOUSEBUTTONDOWN and 15 <= event.pos[0] <= 15 + 73 and \
                15 <= event.pos[1] <= 15 + 73 and second_page:
            image_go_back_tap = pygame.image.load('назад нажали.png').convert_alpha()
            screen.blit(image_go_back_tap, (15, 15))

        elif second_page:
            #print(event.pos)
            image_go_back = pygame.image.load('назад.png').convert_alpha()
            screen.blit(image_go_back, ((15, 15)))
    pygame.display.flip()
pygame.quit()
