import config as cf


class GameSettings(cf.WindowHandler):
    def __init__(self, w_destination, w_width, w_height, w_bg):
        super().__init__(w_destination, w_width, w_height, w_bg)
        self.palette = cf.COLOR_PALETTE

    def save_settings(self, file_path, value_to_save):
        with open(file_path, "w") as file:
            file.write(value_to_save)

    def return_color(self):
        self.color = self.entry.get()
        return self.color

    def set_color(self, text):
        self.entry.delete(0, "end")
        self.entry.insert(0, text)

    def get_color_after_click(self, event):
        x = event.x
        y = event.y
        for col in range(3):
            for row in range(7):
                if (
                    50 + col * 215 < x < 100 + col * 215
                    and 175 + row * 60 < y < 225 + row * 60
                ):
                    return self.set_color(self.palette[row][col])

    def color_options(self):
        for col in range(3):
            for row in range(7):
                self.canvas.create_oval(
                    50 + col * 215,
                    175 + row * 60,
                    100 + col * 215,
                    225 + row * 60,
                    fill=self.palette[row][col],
                )
                self.canvas.create_text(
                    150 + col * 215,
                    205 + row * 60,
                    text=self.palette[row][col],
                    font=(cf.FONT, 15),
                )
