import pygame

size = (1792, 896)
screen = pygame.display.set_mode(size)
image = pygame.image.load('супер пупер заставка тыщу лет фотожопила поставьте полный балл за такое умоляю.png').convert_alpha()
image_question = pygame.image.load('нифига умный вопрос.png').convert_alpha()
image_gears = pygame.image.load('ну а это че.png').convert_alpha()
image_gears_tap = pygame.image.load('ну а это че нажали.png').convert_alpha()
image_question_tap = pygame.image.load('нифига умный вопрос нажали.png').convert_alpha()
screen.blit(image, (0, 0))
screen.blit(image_question, (1574, 22))
screen.blit(image_gears, (1690, 22))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and 1574 <= event.pos[0] <= 1574 + 73 and\
               22 <= event.pos[1] <= 22 + 73:
            screen.blit(image_question_tap, (1574, 22))
            clock.tick(10)
            screen.blit(image_question, (1574, 22))
            #print('question')
            #screen.blit()
        if event.type == pygame.MOUSEBUTTONDOWN and 1574 <= event.pos[0] <= 1574 + 73 and \
                22 <= event.pos[1] <= 22 + 73:
            screen.blit(image_question_tap, (1574, 22))
        if event.type == pygame.MOUSEBUTTONUP and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73:
            screen.blit(image_gears, (1690, 22))
        if event.type == pygame.MOUSEBUTTONDOWN and 1690 <= event.pos[0] <= 1690 + 73 and \
                22 <= event.pos[1] <= 22 + 73:
            screen.blit(image_gears_tap, (1690, 22))
    pygame.display.flip()
pygame.quit()
