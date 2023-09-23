import pygame
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Arrange the Dielectric")
running=True
bgnd=pygame.image.load('background.png')
bgnd=pygame.transform.scale(bgnd,(800,500))



class ImageButton:
    def __init__(self, x, y, image_path,x1,y1):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(x1,y1))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False

menu=ImageButton(340, 260, 'menu-button.png',90,60)
exit=ImageButton(450, 260,'exit-button.png',90,70)
play=ImageButton(200, 250,'play-button.png',100,90)

while running:
    screen.fill((0,0,0))
    screen.blit(bgnd,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        menu.handle_event(event)
        exit.handle_event(event)
        play.handle_event(event)
    
    menu.draw(screen)
    play.draw(screen)
    exit.draw(screen)
    pygame.display.update()
