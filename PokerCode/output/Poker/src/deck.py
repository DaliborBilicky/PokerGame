import config as cf


class Deck:
    def __init__(self, canvas, saved_color_path):
        with open(saved_color_path, "r") as file:
            self.back_color = file.readline()
        if self.back_color == "black":
            self.lines_color = "white"
        else:
            self.lines_color = "black"
        self.face_color = "lightgray"
        self.canvas = canvas

    def cart_template(self, pos_x, pos_y, back=True):
        if back:
            color = self.back_color
        else:
            color = self.face_color

        # Drawing corners
        for col in range(2):
            for row in range(2):
                self.canvas.create_oval(
                    pos_x - 75 + col * 150,
                    pos_y - 100 + row * 200,
                    pos_x - 55 + col * 110,
                    pos_y - 80 + row * 160,
                    fill=color,
                )

        # Drawing card
        for rec in range(2):
            rec_append = ((65, 75), (100, 90))
            self.canvas.create_rectangle(
                pos_x - rec_append[0][rec],
                pos_y - rec_append[1][rec],
                pos_x + rec_append[0][rec],
                pos_y + rec_append[1][rec],
                fill=color,
                outline=color,
            )

        # Draw cart outline
        for outline in range(2):
            self.canvas.create_line(
                pos_x - 75.5 + outline * 151,
                pos_y - 90.5,
                pos_x - 75.5 + outline * 151,
                pos_y + 90.5,
            )
            self.canvas.create_line(
                pos_x - 65.5,
                pos_y - 100.5 + outline * 201,
                pos_x + 65.5,
                pos_y - 100.5 + outline * 201,
            )

    def draw_cart_back(self, pos_x, pos_y):
        self.cart_template(pos_x, pos_y)

        # Draw grid for detail
        for row in range(19):
            self.canvas.create_line(
                pos_x - 75,
                pos_y - 90 + row * 10,
                pos_x + 75,
                pos_y - 90 + row * 10,
                fill=self.lines_color,
            )
        for col in range(14):
            self.canvas.create_line(
                pos_x - 65 + col * 10,
                pos_y - 100,
                pos_x - 65 + col * 10,
                pos_y + 100,
                fill=self.lines_color,
            )

    def draw_cart_face(self, pos_x, pos_y, card_value):
        number = card_value[0]
        char = card_value[1]
        self.cart_template(pos_x, pos_y, back=False)

        # Drawing cards values (numbers, characters)
        for c_value in range(2):
            self.canvas.create_text(
                pos_x - 50 + c_value * 100,
                pos_y - 80 + c_value * 160,
                text=f"{number}{char[0]}",
                fill=char[1],
                font=(cf.FONT, 20),
            )
        self.canvas.create_text(
            pos_x, pos_y, text=char[0], fill=char[1], font=(cf.FONT, 50)
        )
