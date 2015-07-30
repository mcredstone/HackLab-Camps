#Bouncing Sprite (BOING, BOING, EARPHONE SPLAT! (OW!) )
from livewires import games

games.init(screen_width = 800, screen_height = 500, fps = 50)

hacklab_BG = games.load_image("HackLabBG.png")
games.screen.background = hacklab_BG

class HackLab(games.Sprite):

    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
            
hacklab_img = games.load_image("HackLab.png")
hacklab = HackLab(image = hacklab_img, x = 400, y = 250, dx = 1, dy = 1)
games.screen.add(hacklab)

games.screen.mainloop()
