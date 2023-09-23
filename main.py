import pygame
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Arrange the Dielectric")
font1 = pygame.font.Font('fonts\Inconsolata.ttf', 80)
font2 = pygame.font.Font('fonts\Inconsolata.ttf', 40)

running=True
current_screen = "screen1"


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
            


menu=ImageButton(340, 260, 'assets/menu-button.png',90,60)
exit1=ImageButton(450, 260,'assets/exit-button.png',90,70)
play=ImageButton(200, 250,'assets/play-button.png',100,90)
exit2=ImageButton(700, 20,'assets/exit-button.png',90,70)

def draw_screen1():
    screen.fill((0,0,0))
    bgnd=pygame.image.load("assets/background.png")
    bgnd=pygame.transform.scale(bgnd,(800,500))
    screen.blit(bgnd,(0,0))
    menu.draw(screen)
    play.draw(screen)
    exit1.draw(screen)
    text = font1.render("Virtual Lab", True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = (400-10, 250-70)
    screen.blit(text, text_rect)
def draw_screen2():
    screen.fill((0,0,0))
    screen.fill((0,0,0))
    bgnd=pygame.image.load('assets/background2.png')
    bgnd=pygame.transform.scale(bgnd,(800,500))
    screen.blit(bgnd,(0,0))
    exit2.draw(screen)
    text = font2.render("Arrange the Dielectric", True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = (400-10, 250-190)
    screen.blit(text, text_rect)
    
while running:
    for event in pygame.event.get():
        exit1.handle_event(event)
        menu.handle_event(event)
        play.handle_event(event)
        exit2.handle_event(event)
        if event.type==pygame.QUIT or (exit1.clicked and current_screen == "screen1"):
            running=False
        elif play.clicked:
            current_screen = "screen2"
        elif exit2.clicked:
            current_screen = "screen1" 
    if current_screen == "screen1":
        draw_screen1()
    elif current_screen == "screen2":
        draw_screen2()
    
    pygame.display.update()
