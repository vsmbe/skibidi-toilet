from pygame import *
from random import *

lost = 0
kil = 0

mixer.init()
vis = mixer.Sound("fire.ogg")
mixer.music.load("space.ogg")
mixer.music.play()
font.init()
font = font.SysFont("Times New Roman", 70)
won = font.render("выиграл", True, (0, 255, 110))
wyn = font.render("проиграл", True, (255, 0, 0))

fps = 120
clock = time.Clock()
win = display.set_mode((700, 500))
display.set_caption("shooter")

back = transform.scale(image.load("galaxy.jpg"), (700, 500))

class gs (sprite.Sprite):
    def __init__(self, img, x, y, spd, wid, hei):
        super().__init__()
        self.image = transform.scale(image.load(img), (wid, hei))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.spd = spd
        self.dir = "right"
    def res (self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class player(gs):
    def upd(self):
        keypress = key.get_pressed()
        if keypress[K_d] and self.rect.x < 600:
            self.rect.x += self.spd
        if keypress[K_a] and self.rect.x > 5:
            self.rect.x -= self.spd
    def fire(self):
        spr5 = bulet("qwe.png", self.rect.centerx - 15, self.rect.top, 2, 30, 30)
        pulki.add(spr5)
        vis.play()

class bulet(gs):
    def update(self):
        self.rect.y -= self.spd
        if self.rect.y <= -40:
            self.kill()

class enemy(gs):
    def update(self):
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = (randint(50,650))
            global lost
            lost = lost + 1
        else:
            self.rect.y += self.spd

spr = player("Без.png",300,400,5,60,100)
spr0 = enemy("ufo.png", randint(50,650), 1, randint(1, 2),65, 65)
spr1 = enemy("ufo.png",randint(50,650),1,randint(1, 2), 65, 65)
spr2 = enemy("ufo.png",randint(50,650),1,randint(1, 2),65, 65)
spr3 = enemy("ufo.png",randint(50,650),1,randint(1, 2),65, 65)
spr4 = enemy("ufo.png",randint(50,650),1,randint(1, 2), 65, 65)
sprs = sprite.Group()
pulki = sprite.Group()
sprs.add(spr0)
sprs.add(spr1)
sprs.add(spr2)
sprs.add(spr3)
sprs.add(spr4)

game = True
finish = False
while game:
    kol0 = sprite.spritecollide(spr, sprs, True)
    if finish != True:
        win.blit(back, (0, 0))
        spr.res()
        spr.upd()
        pulki.draw(win)
        pulki.update()
        sprs.draw(win)
        sprs.update()
        text0 = font.render("Убито: " + str(kil) + " из 20", 1,(200, 230, 130))
        text = font.render("Пропущено: " + str(lost) + " из 1", 1, (200, 230, 130))
        win.blit(text, (0, 0))
        win.blit(text0, (0,50))
        if lost >= 1 or len(kol0) > 0:
            finish = True
            win.blit(wyn, (250, 250))
        elif kil >= 20:
            finish = True
            win.blit(won, (250,250))

    for q in event.get():
        if q.type == QUIT:
            game=False
        elif q.type == KEYDOWN:
            if q.key == K_SPACE:
                spr.fire()

    kol = sprite.groupcollide(sprs, pulki, True, True)

    for i in kol:
        kil +=1
        spr6 = enemy("ufo.png", randint(50, 650), 1, randint(1, 2), 65, 65)
        sprs.add(spr6)

    clock.tick(fps)

    display.update()