#Big Score (You did well!)

from livewires import games, color

games.init(screen_width = 800, screen_height = 500, fps = 50)

hacklabBG = games.load_image("HackLabBG.png")
games.screen.background = hacklabBG

score = games.Text(value = 9876543210,
                   size = 45,
                   color = color.white,
                   x = 650,
                   y = 30)
games.screen.add(score)

games.screen.mainloop()

