#Platformer
from livewires import games
import time
import random

games.init(screen_width = 800, screen_height = 500, fps = 50)

patternImg = games.load_image("HackLabBG.png")
games.screen.background = patternImg

class Player(games.Sprite):
    def update(self):
        self.dy += 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 2.5
        if self.bottom > 499:
            self.y = 499 - 52.5
        if games.keyboard.is_pressed(games.K_SPACE) and self.y == 499 - 52.5:
            self.dy = -17.5
player = Player(image = games.load_image("HackLab.png"), x = 150, y = 100, dx = 0, dy = 3)
games.screen.add(player)

platform1Img = games.load_image("platform1.png")
platform2Img = games.load_image("platform2.png")
platform3Img = games.load_image("platform3.png")
count = 0
class Platform(games.Sprite):
    def update(self):
        fall = False
        playeronTop = False
        if self.top < player.bottom:
            if fall != True:
                player.bottom = self.top
                playeronTop = True
        if self.image == platform2Img:
            fall = True
            if playeronTop == True:
                count += 1
                if count >= 3:
                    fall = True
                    count = 0
            
        
platformt1 = Platform(image = random.choice([games.load_image("platform1.png"), games.load_image("platform2.png"), games.load_image("platform3.png")]), x = 200, y = 150)
platformt2 = Platform(image = random.choice([games.load_image("platform1.png"), games.load_image("platform2.png"), games.load_image("platform3.png")]), x = 400, y = 150)
games.screen.add(platformt1)
games.screen.add(platformt2)

games.screen.mainloop()
