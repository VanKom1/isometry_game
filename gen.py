import pygame
pygame.init()

window = pygame.display.set_mode((500,500))
window.fill((50,150,50))

class Block():
    def __init__(self,x,y,w,h):
        self.image = pygame.image.load("2.png")
        self.rect = pygame.Rect(x, y, w, h)
        self.srart_x = x
        self.srart_y = y
    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)



game_map = [
    [0,2,1,1,0,0,0,0],
    [0,0,1,1,0,0,0,0],
    [0,0,1,1,1,2,3,0],
    [0,0,0,1,1,2,3,0],
    [0,0,0,1,1,2,3,0],
    [1,1,1,1,1,1,1,1]
]



def gen(game_map):
    
    global pole
    pole = []
    start_x = 10
    start_y = 10
    for i in range(len(game_map)):
        for j in game_map[i]:
            start_y_2 = start_y
            for k in range(j):
                block = Block(start_x, start_y, 26, 26)
                pole.append(block)
                start_y -= 16
            start_x += 32
            start_y = start_y_2
        start_y += 8
        start_x = 10 + ((i % 2) * 16) + 16
gen(game_map)
while True:
    window.fill((50,150,50))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x,y = pygame.mouse.get_pos()
            for i in pole:
                if i.collidepoint(x,y):
                    i.rect.y = i.srart_y - 8
                else:
                    i.rect.x = i.srart_x
                    i.rect.y = i.srart_y
                        
    for i in pole:
        i.draw()

    pygame.display.update()
    pygame.time.delay(50)