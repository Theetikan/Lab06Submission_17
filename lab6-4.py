import sys
import pygame as pg

pg.init()

win_x = 800
win_y = 400
screen = pg.display.set_mode((win_x, win_y))

#First Name
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('First Name', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (170, 67)

#Last Name
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text2 = font.render('Last Name', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect2 = text.get_rect() # text size
textRect2.center = (170, 167)

#Age
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text3 = font.render('Age', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect3 = text.get_rect() # text size
textRect3.center = (170, 267)

#Submit
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text4 = font.render('Submit', True, (0,0,0)) # (text,is smooth?,letter color,background color)
textRect4 = text.get_rect() # text size
textRect4.center = (700, 350)


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
        pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    #def isMouseClick(self):
    #    mouse_x, mouse_y = pg.mouse.get_pos()
    #   if mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h and pg.mouse.get_pressed()[0]:
    #        return True
    #    else: return False

    def isMouseClick(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0] and mouse_x  >= self.x and  mouse_x <= self.x+self.w and mouse_y >= self.y and  mouse_y <= self.y+self.h:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
                return True
        else: return False

btn = Button(600, 325, 150, 50)  # สร้าง Object จากคลาส Button ขึ้นมา


class InputBox:

    def __init__(self, x, y, w, h, text='',pp=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.pp = pp
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos):  # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.pp = self.text
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def printpp(self):
        return self.pp

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class InputBoxforAge:

    def __init__(self, x, y, w, h, text='',pp='',er = 'error'):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.pp = pp
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.error = er

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos):  # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.pp = self.text
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def printpp(self):
        try :
            float(self.pp)
            return self.pp
        except ValueError: return self.error

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

COLOR_INACTIVE = pg.Color('lightskyblue3')  # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')  # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32)  # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32)  # สร้าง InputBox2
input_boxAge = InputBoxforAge(100, 300, 140, 32)  # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_boxAge]  # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True


switch = 0
while run:
    screen.fill((255, 255, 255))
    # Print Text
    font = pg.font.Font('freesansbold.ttf', 22)  # font and fontsize
    text5 = font.render(
        "Hello " + input_box1.printpp() + ' ' + input_box2.printpp() + ". You are " + input_boxAge.printpp() + " years old.",
        True, (255, 0, 0))  # (text,is smooth?,letter color,background color)
    textRect5 = text.get_rect()  # text size
    textRect5.center = (400, 100)

    if btn.isMouseClick():
        switch = 1

    if switch == 1:
        screen.blit(text5, textRect5)

    for box in input_boxes:  # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update()  # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen)  # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen


    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)

        #if event.type == pg.mouse.get_pressed()[0]:  # ปุ่มถูกกดลงและเป็นปุ่มleft click
            #print("Hello " + input_boxes[0] + ' ' + input_boxes[1] + "You are " + input_boxes[2] + " years old.")

        if event.type == pg.QUIT:
            pg.quit()
            run = False



    btn.draw(screen)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)



    pg.time.delay(1)
    pg.display.update()

