#Moving Sprite (RUN RUN RUN!)
from livewires import games

games.init(screen_width = 800, screen_height = 500, fps = 50)

hacklabBG = games.load_image("HackLabBG.png")
games.screen.background = hacklabBG

mrhacker_img = games.load_image("HackLab.png")
mrhacker = games.Sprite(image = mrhacker_img, x = 400, y = 250, dx = 1, dy = 1)
games.screen.add(mrhacker)

games.screen.mainloop()
