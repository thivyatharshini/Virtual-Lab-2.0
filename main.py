import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Arrange the Dielectric")
font1 = pygame.font.Font("fonts/Inconsolata.ttf", 80)
font2 = pygame.font.Font("fonts/Inconsolata.ttf", 40)
font3 = pygame.font.Font("fonts/Inconsolata.ttf", 20)

running = True
current_screen = "screen1"
capacitance=0
target_value=[28.32,79.65,1026.6,41.78,55.12,147.83,13.98,38.38,89.21]
iter=0
highscore=0



class Image:
    def __init__(self, x, y, image_path, x1, y1):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (x1, y1))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class ImageButton:
    def __init__(self, x, y, image_path, x1, y1):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (x1, y1))
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


class DraggableElement:
    def __init__(self, x, y, image_path, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            x,
            y,
        )  # Pygame rectangle defining the element's position and size
        self.permittivity = 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.image == d1.image:
                    self.permittivity = 1.6  # Paper
                elif self.image == d2.image:
                    self.permittivity = 4.5  # Quartz
                elif self.image == d3.image:
                    self.permittivity = 58  # Mica

                duplicate = DraggableDuplicate(
                    self.rect.x + 10,  # Offset the duplicate's position
                    self.rect.y + 10,  # Offset the duplicate's position
                    self.image,
                    self.permittivity,
                )
                duplicate_dlist.append(duplicate)
                value.append(self.permittivity)


class DraggableDuplicate:
    def __init__(self, x, y, image, permittivity):
        self.permittivity = permittivity
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y,)  # Pygame rectangle defining the element's position and size
        self.dragging = False  # Flag to track if the element is being dragged

    def update(self, mouse_pos):
        # Update the element's position if it's being dragged
        if self.dragging:
            self.rect.center = mouse_pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            any_dragging = any(element.dragging for element in duplicate_dlist)
            if not any_dragging and self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if self.rect.collidepoint(event.pos):
                duplicate_dlist.remove(self)
                value.remove(self.permittivity)
                del self

    def fix_position_and_size(self, fixed_x, fixed_y, new_width, new_height):
        if self.rect.colliderect(pygame.Rect(fixed_x, fixed_y, new_width, new_height)):
            self.rect.topleft = (fixed_x, fixed_y)
            self.image = pygame.transform.scale(self.image, (new_width, new_height))


menu = ImageButton(340, 260, "assets/menu-button.png", 90, 60)
exit1 = ImageButton(450, 260, "assets/exit-button.png", 90, 70)
play = ImageButton(200, 250, "assets/play-button.png", 100, 90)
exit2 = ImageButton(700, 20, "assets/exit-button.png", 90, 70)
dielectric = ImageButton(20, 100, "assets/dielectric-button.png", 100, 70)
run = ImageButton(20, 170, "assets/run-button.png", 100, 60)
battery = Image(290, 330, "assets/battery.png", 200, 150)
capacitorL = Image(240, 130, "assets/capacitorleft.png", 100, 170)
capacitorR = Image(400, 130, "assets/capacitorright.png", 100, 170)
d1 = DraggableElement(50, 20, "assets/dielectric1.png", 70, 70)
d2 = DraggableElement(150, 20, "assets/dielectric2.png", 70, 70)
d3 = DraggableElement(250, 14, "assets/dielectric3.png", 82, 82)
result= Image(600, 80, "assets/resultplate.png", 250, 200)
score= Image(575, 230, "assets/scoreplate.png", 260, 200)
instruction= Image(20, 10, "assets/instruction.png", 690, 480)


def draw_screen1():
    bgnd = pygame.image.load("assets/background.png")
    bgnd = pygame.transform.scale(bgnd, (800, 500))
    screen.blit(bgnd, (0, 0))
    menu.draw(screen)
    play.draw(screen)
    exit1.draw(screen)
    text = font1.render("Virtual Lab", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (400 - 10, 250 - 70)
    screen.blit(text, text_rect)

def draw_screen3():
    bgnd = pygame.image.load("assets/background2.png")
    bgnd = pygame.transform.scale(bgnd, (800, 500))
    screen.blit(bgnd, (0, 0))
    exit2.draw(screen)
    instruction.draw(screen)
    
    

def draw_screen2():
    
    bgnd = pygame.image.load("assets/background2.png")
    bgnd = pygame.transform.scale((bgnd), (800, 500))
    screen.blit(bgnd, (0, 0))
    battery.draw(screen)
    capacitorL.draw(screen)
    capacitorR.draw(screen)
    dielectric.draw(screen)
    run.draw(screen)
    exit2.draw(screen)
    result.draw(screen)
    score.draw(screen)
    for start, end in wire:
        pygame.draw.line(
            screen, (255, 0, 0), start, end, 5
        )  # Use the color (255, 0, 0) for red
    text = font2.render("Arrange The Dielectric", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (390, 60)
    screen.blit(text, text_rect)
    text = font2.render("Level "+str((iter//3)+1), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (390, 100)
    screen.blit(text, text_rect)
    printresult()
    printscore()
    
    

    if open_smallscreen:
        bgnd = pygame.image.load("assets/dielectric-bgnd.png")
        bgnd = pygame.transform.scale(bgnd, (300, 100))
        screen.blit(bgnd, (40, 10))
        text = font3.render("Paper       Quartz        Mica", True, (255, 0,0))
        text_rect = text.get_rect()
        text_rect.topleft = (65, 85)
        screen.blit(text, text_rect)
        for element in dlist:
            element.draw(screen)
    for element in duplicate_dlist:
        element.draw(screen)
def printresult():
    global iter
    text = font3.render(str(capacitance)+" pF", True, (255, 0,0))
    text_rect = text.get_rect()
    text_rect.center = (715, 210)
    screen.blit(text, text_rect)
    if target_value[iter]==capacitance:
        time.sleep(1)
        iter+=1
        
    text = font3.render(str(target_value[iter])+" pF", True, (255, 0,0))
    text_rect = text.get_rect()
    text_rect.center = (715, 165)
    screen.blit(text, text_rect)

def printscore():
    text = font3.render(str(highscore), True, (255, 0,0))
    text_rect = text.get_rect()
    text_rect.center = (715, 350)
    screen.blit(text, text_rect)
    text = font3.render(str(iter), True, (255, 0,0))
    text_rect = text.get_rect()
    text_rect.center = (715, 305)
    screen.blit(text, text_rect)
    

def calculate_capacitance(val):
    length = len(val)
    re_permittivity = 1
    if length == 1:
        re_permittivity = val[0]
    elif length == 2:
        re_permittivity = (2 * val[0] * val[1]) / (val[0] + val[1])
    elif length == 3:
        re_permittivity = (val[0] * (val[1] + val[2])) / (
            val[0] + 2 * (val[1] + val[2])
        )
    elif length == 4:
        re_permittivity = ((val[0] * val[1]) / (val[0] + val[1])) + (
            (val[2] * val[3]) / (val[2] + val[3])
        )
    capacitance = (8.85 * 100 * re_permittivity) / (10 * 5)
    return capacitance


dlist = [d1, d2, d3]
duplicate_dlist = []
value = []
wire = [
    ((240, 218), (160, 218)),
    ((160, 218), (160, 346)),
    ((160, 346), (326, 346)),
    ((500, 218), (570, 218)),
    ((570, 218), (570, 346)),
    ((570, 346), (430, 346)),
]
open_smallscreen = False


while running:
    for event in pygame.event.get():
        exit1.handle_event(event)
        menu.handle_event(event)
        play.handle_event(event)
        exit2.handle_event(event)
        dielectric.handle_event(event)
        run.handle_event(event)
        for element in dlist:
            element.handle_event(event)
        for element in duplicate_dlist:
            element.handle_event(event)

        if event.type == pygame.QUIT or (exit1.clicked and current_screen == "screen1"):
            running = False
        elif play.clicked:
            current_screen = "screen2"
        elif menu.clicked:
            current_screen = "screen3"
        elif exit2.clicked:
            current_screen = "screen1"
            duplicate_dlist.clear()
            value.clear()
            capacitance=0
            open_smallscreen = False
            if iter>highscore:
                highscore=iter
            iter=0

        if dielectric.clicked:
            open_smallscreen = not open_smallscreen
        if run.clicked :
            open_smallscreen = False
            capacitance = round(calculate_capacitance(value),2)
            print(capacitance, "pF")
            
                
            

    if current_screen == "screen1":
        draw_screen1()
    elif current_screen == "screen2":
        draw_screen2()
    elif current_screen == "screen3":
        draw_screen3()
        
    for index, element in enumerate(duplicate_dlist):
        element.update(pygame.mouse.get_pos())
        xc = [320, 370, 370, 320]
        yc = [154, 154, 214, 214]
        w = 100 if len(duplicate_dlist) == 1 else 50
        h = 120 if (len(duplicate_dlist) + index) <= 3 else 60
        element.fix_position_and_size(xc[index], yc[index], w, h)

    pygame.display.update()
