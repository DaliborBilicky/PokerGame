import tkinter


class WindowHandler:
    def __init__(self, w_destination, w_width, w_height, w_bg):
        self.w_dest = w_destination
        self.w_width = w_width
        self.w_height = w_height
        self.w_bg = w_bg

    def display(self):
        self.canvas = tkinter.Canvas(
            self.w_dest, width=self.w_width, height=self.w_height, bg=self.w_bg
        )
        self.canvas.pack()

    def kill(self):
        self.canvas.destroy()

    def buttons(self, b_pos, b_size, b_font, b_text, b_color, b_command):
        button = tkinter.Button(
            self.w_dest,
            width=b_size[0],
            height=b_size[1],
            bg=b_color[0],
            activebackground=b_color[1],
            font=b_font,
            text=b_text,
            command=b_command,
        )
        button.place(x=b_pos[0], y=b_pos[1])

    def labels(self, l_pos, l_text, l_font, l_fg="black", l_bg=None):
        if not l_bg:
            l_bg = self.w_bg
        label = tkinter.Label(
            self.w_dest,
            bg=l_bg,
            fg=l_fg,
            text=l_text,
            font=l_font,
        )
        label.place(x=l_pos[0], y=l_pos[1])

    def entries(self, e_pos, e_bg, e_font):
        self.entry = tkinter.Entry(self.w_dest, width=45, bg=e_bg, font=e_font)
        self.entry.place(x=e_pos[0], y=e_pos[1])
