#Background Image (HackLab!)
from livewires import games

games.init(screen_width = 800, screen_height = 500, fps = 50)

hacklab_img = games.load_image("HackLabBG.png")
games.screen.background = hacklab_img

games.screen.mainloop()
