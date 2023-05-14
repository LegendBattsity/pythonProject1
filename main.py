from pygame import *
from random import random, randrange, randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self,player_image,player_x, player_y, player_speed):
        super().__init__(player_image,player_x, player_y, player_speed)
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.x += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_l] and self.rect.y < win_height - 80:
            self.rect.x += self.speed
finish = False
FPS = 60
clock = time.Clock()
win_height = 0


window = display.set_mode((700,500))
display.set_caption('Фон')
background = transform.scale(image.load('фон.jpg'), (900,900))
rocket1 = transform.scale(image.load('images.jpg'),(50,200))
rocket2 = transform.scale(image.load('Без названия.jpg'),(50,200))
ball = transform.scale(image.load('мяч.png'),(100,100))

p1 = Player('images.jpg',300,200,4,50,150)
p2 = Player('Без названия.jpg', 520,200,4,50,150)
ball = GameSprite('мяч.png', 200,200,4,50,50)

speed_x = 3
speed_y = 3

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background)
        p1.update1()
        p2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y




    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    p1.reset()
    p2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)






