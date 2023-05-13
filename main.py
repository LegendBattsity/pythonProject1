from pygame import *
from random import random, randrange, randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(30,45))
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
        if keys_pressed[K_w]:
            self.rect.x += 10
        if keys_pressed[K_s]:
            self.rect.x -= 10
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o]:
            self.rect.x += 10
        if keys_pressed[K_l]:
            self.rect.x -= 10

FPS = 60
clock = time.Clock()
win_height = 0


window = display.set_mode((700,500))
display.set_caption('Фон')
background = transform.scale(image.load('фон.jpg'), (900,900))
rocket1 = transform.scale(image.load('images.jpg'),(50,200))
rocket2 = transform.scale(image.load('Без названия.jpg'),(50,200))
ball = transform.scale(image.load('мяч.png'),(100,100))

p1 = Player('images.jpg',440,50,60)
p2 = Player('Без названия.jpg', -444,50,60)
p3 = Player('мяч.png', 200,40,60)

speed_x = 3
speed_y = 3

game = True
finish = False
while game:
    window.blit(background, (0, 0))
    p1.reset()
    p1.update()
    clock.tick(FPS)
    p2.draw(window)
    p2.update()
    p3.update()
    p3.draw(window)

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1






