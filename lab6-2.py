import sys
import pygame as pg
pg.init()


class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r
        self.g = g
        self.b = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x  >= self.x and  mouse_x <= self.x+self.w and mouse_y >= self.y and  mouse_y <= self.y+self.h:
            return True
        else: return False


pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20, 20, 100, 100)  # สร้าง Object จากคลาส Button ขึ้นมา

while (run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.r = 160
        btn.g = 160
        btn.b = 160
    else:
        btn.r = 255
        btn.g = 0
        btn.b = 0
    btn.draw(screen)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D down")
            btn.x += 10

        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key A down")
            btn.x -= 10

        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key W down")
            btn.y -= 10

        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key S down")
            btn.y += 10

