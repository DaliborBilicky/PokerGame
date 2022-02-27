import config as cf


class GameMenu(cf.WindowHandler):
    def __init__(self, w_destination, w_width, w_height, w_bg):
        super().__init__(w_destination, w_width, w_height, w_bg)
        self.char = cf.CARDS_CHARACTERS

    def display(self):
        super().display()
        char_pos = (
            (75, 75),
            (75, self.w_height - 75),
            (self.w_width - 75, 75),
            (self.w_width - 75, self.w_height - 75),
        )

        # Some details for menu
        for i in range(4):
            self.canvas.create_text(
                char_pos[i][0],
                char_pos[i][1],
                text=self.char[i][0],
                fill=self.char[i][1],
                font=(cf.FONT, 100),
            )
