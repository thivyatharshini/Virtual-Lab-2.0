import pygame
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Arrange the Dielectric")
font1 = pygame.font.Font('fonts/Inconsolata.ttf', 80)
font2 = pygame.font.Font('fonts/Inconsolata.ttf', 40)

running=True
current_screen = "screen1"


class Image:
    def __init__(self, x, y, image_path,x1,y1):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(x1,y1))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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
            
class DraggableElement:
    def __init__(self, x, y, image_path,width,height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)    # Pygame rectangle defining the element's position and size

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                duplicate = DraggableDuplicate(
                        self.rect.x + 10,  # Offset the duplicate's position
                        self.rect.y + 10,  # Offset the duplicate's position
                        self.image)
                duplicate_dlist.append(duplicate)
class DraggableDuplicate:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)    # Pygame rectangle defining the element's position and size
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
            if  self.rect.collidepoint(event.pos):
                duplicate_dlist.remove(self)
                del self
    def fix_position_and_size(self, fixed_x, fixed_y, new_width, new_height):
            if self.rect.colliderect(pygame.Rect(fixed_x, fixed_y, new_width, new_height)):
                self.rect.topleft = (fixed_x, fixed_y)
                self.image = pygame.transform.scale(self.image, (new_width, new_height))    
        

menu=ImageButton(340, 260, 'assets/menu-button.png',90,60)
exit1=ImageButton(450, 260,'assets/exit-button.png',90,70)
play=ImageButton(200, 250,'assets/play-button.png',100,90)
exit2=ImageButton(700, 20,'assets/exit-button.png',90,70)
dielectric=ImageButton(20, 100,'assets/dielectric-button.png',100,70)
run=ImageButton(20, 170,'assets/run-button.png',100,60)
edit=ImageButton(20, 230,'assets/edit-button.png',100,60)
battery=Image(290, 330, 'assets/battery.png',200,150)
capacitorL=Image(240, 130, 'assets/capacitorleft.png',100,170)
capacitorR=Image(400, 130, 'assets/capacitorright.png',100,170)
d1=DraggableElement(50, 30, 'assets/dielectric1.png',70,70)
d2=DraggableElement(120, 30, 'assets/dielectric2.png',70,70)
d3=DraggableElement(190, 24, 'assets/dielectric3.png',82,82)



def draw_screen1():
   
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
    
    bgnd=pygame.image.load('assets/background2.png')
    bgnd=pygame.transform.scale((bgnd),(800,500))
    screen.blit(bgnd,(0,0))
    battery.draw(screen)
    capacitorL.draw(screen)
    capacitorR.draw(screen)
    dielectric.draw(screen)
    run.draw(screen)
    edit.draw(screen)
    exit2.draw(screen)
    for element in duplicate_dlist:
        element.draw(screen)
    
    text = font2.render("Arrange the Dielectric", True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = (390, 60)
    screen.blit(text, text_rect)

def dielectric_screen():
    bgnd=pygame.image.load('assets/dielectric-bgnd.png')
    bgnd=pygame.transform.scale(bgnd,(300,100))
    screen.blit(bgnd,(40,10))
    for element in dlist:
        element.draw(screen)
    
    
    
dlist=[d1,d2,d3]  
duplicate_dlist=[]  
open_smallscreen = False

    
    
while running:
    for event in pygame.event.get():
        
        exit1.handle_event(event)
        menu.handle_event(event)
        play.handle_event(event)
        exit2.handle_event(event)
        dielectric.handle_event(event)
        for element in dlist:
            element.handle_event(event)
        for element in duplicate_dlist:
            element.handle_event(event)
            
        if event.type==pygame.QUIT or (exit1.clicked and current_screen == "screen1"):
            running=False
        elif play.clicked:
            current_screen = "screen2"
        elif exit2.clicked:
            current_screen = "screen1" 
        if dielectric.clicked :
            open_smallscreen = not open_smallscreen
    if current_screen == "screen1":
        draw_screen1()
    elif current_screen == "screen2":
        draw_screen2()
    if open_smallscreen and current_screen == "screen2":
        dielectric_screen()
    for index,element in enumerate(duplicate_dlist):
        element.update(pygame.mouse.get_pos())
        xc=[320,370,370,320]
        yc=[154,154,214,214]
        w=100 if len(duplicate_dlist)==1 else 50
        h=120 if (len(duplicate_dlist)+index) <=3 else 60
        print(index)
        element.fix_position_and_size(xc[index], yc[index],w, h)   
        
    
    pygame.display.update()
