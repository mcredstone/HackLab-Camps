#Sprite (THE HACKLAB!)
from livewires import games

games.init(screen_width = 800, screen_height = 500, fps = 50)

hacklab_img = games.load_image("HackLab.png")
hacklab = games.Sprite(image = hacklab_img, x = 400, y = 250)
games.screen.add(hacklab)

hacklab_BG = games.load_image("HackLabBG.png")
games.screen.background = hacklab_BG

games.screen.mainloop()
