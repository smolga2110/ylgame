import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Test')
    background = pygame.image.load('background.jpg')
    screen.blit(background, (0,0))
    face = pygame.image.load('text.gif')
    b = screen.blit(face, (300, 300))



    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if b.collidepoint(x, y):
                    face = pygame.image.load('background.jpg')
                    b = screen.blit(face, (300, 300))
                else:
                    face = face = pygame.image.load('text.gif')
                    b = screen.blit(face, (300, 300))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if b.collidepoint(x, y):
                    print("button has been clicked")



        pygame.display.update()
class HelloWorld:
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Hello Привет', True,
                      (180, 0, 0))




if __name__ == "__main__":
    def _creator():
        screen2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
        hello = HelloWorld(screen2)
        hello.run()
    MENU_ITEMS = ("Welcome", "Exit")
    SCREEN = pygame.display.set_mode((800, 600), 0, 32)
    FUNCS = {"Welcome": _creator, "Exit": sys.exit}
    GM = Main(SCREEN, FUNCS.keys(), FUNCS)
    GM.run()