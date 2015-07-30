#Platformer
from livewires import games
import time

games.init(screen_width = 800, screen_height = 500, fps = 50)

patternImg = games.load_image("HackLabBG.png")
games.screen.background = patternImg

class Player(games.Sprite):
    def update(self):
        self.dy += 1
        if games.keyboard.is_pressed(games.K_d):
            pass
        if self.bottom > 499:
            self.y = 499 - 52.5
        if games.keyboard.is_pressed(games.K_SPACE) and self.y == 499 - 52.5:
            self.dy = -17.5
player = Player(image = games.load_image("HackLab.png"), x = 150, y = 250, dx = 0, dy = 3)
games.screen.add(player)

games.screen.mainloop()
