# ---------------------------------- WINDOW ---------------------------------- #
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
WINDOW_TITLE = "Poker"
WINDOW_ICON = "assets\\icon.ico"

# Applies to the entire code
FONT = "Arial"
MOUSE_BIND = "<Button-1>"
SAVE_FILE_PATH = "assets\\color_save.txt"
CARDS_CHARACTERS = (("♠", "black"), ("♥", "red"), ("♣", "black"), ("♦", "red"))
CARDS_NUM = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
COLOR_PALETTE = (
    ("white", "red", "cyan"),
    ("lightgray", "orange", "lightblue"),
    ("silver", "gold", "blue"),
    ("darkgray", "yellow", "darkblue"),
    ("gray", "lightgreen", "purple"),
    ("black", "green", "magenta"),
    ("brown", "darkgreen", "pink"),
)


# ----------------------------------- MENU ----------------------------------- #
MENU_BG = "gold"

# Menu title
MENU_TITLE_POS = (WINDOW_WIDTH / 2 - 450, 100)
MENU_TITLE_FONT = (FONT, 192)
MENU_TITLE_TEXT = "POKER"


# Menu buttons
MENU_BUTTONS_TEXT = ("START GAME", "GAME SETTINGS")
MENU_BUTTONS_COLOR = ("silver", "gray")
MENU_BUTTONS_FONT = (FONT, 20)
MENU_BUTTONS_SIZE = (20, 1)
MENU_BUTTONS_POS = (
    (WINDOW_WIDTH / 2 - 165, WINDOW_HEIGHT - 250),
    (WINDOW_WIDTH / 2 - 165, WINDOW_HEIGHT - 150),
)


# --------------------------------- SETTINGS --------------------------------- #
SETTINGS_BG = "lightblue"

# Settings buttons
SETTINGS_BUTTONS_TEXT = ("SAVE COLOR", "BACK TO MENU")
SETTINGS_BUTTONS_COLOR = ("silver", "gray")
SETTINGS_BUTTONS_FONT = (FONT, 20)
SETTINGS_BUTTONS_SIZE = (15, 1)
SETTINGS_BUTTONS_POS = (
    (WINDOW_WIDTH * 3 / 4 - 222.5, WINDOW_HEIGHT - 75),
    (WINDOW_WIDTH - 270, WINDOW_HEIGHT - 75),
)

# Settings entry
SETTINGS_ENTRY_POS = (WINDOW_WIDTH / 5 - 225, WINDOW_HEIGHT - 65)
SETTINGS_ENTRY_FONT = (FONT, 20)
SETTINGS_ENTRY_BG = "white"

# Settings text
SETTINGS_TEXT_POS = ((WINDOW_WIDTH / 2 - 255, 10), (WINDOW_WIDTH - 460, 175))
SETTINGS_TEXT_FONT = ((FONT, 75), (FONT, 30))
SETTINGS_TEXT = (
    "SETTINGS",
    """Choose the color of 
the back of the cards.
Click on circle or 
manually type color 
from the options.
Feel free to also use 
HEX color palette.
But don't forget 
the hashtag (#).""",
)


# ----------------------------------- GAME ----------------------------------- #
GAME_BG = "green"

# Game buttons
GAME_BUTTONS_COLOR = ("silver", "gray")
GAME_BUTTONS_FONT = (FONT, 10)
GAME_BUTTONS_SIZE = (15, 1)
GAME_BUTTONS_TEXT = (
    "DEAL CARDS",
    "FIRST TURN",
    "SECOND TURN",
    "FINAL TURN",
    "SHOWDOWN",
    "RESTART",
    "BACK TO MENU",
)
GAME_BUTTONS_POS = (
    (WINDOW_WIDTH / 7 - 155, 680),
    (WINDOW_WIDTH * 2 / 7 - 155, 680),
    (WINDOW_WIDTH * 3 / 7 - 155, 680),
    (WINDOW_WIDTH * 4 / 7 - 155, 680),
    (WINDOW_WIDTH * 5 / 7 - 155, 680),
    (WINDOW_WIDTH * 6 / 7 - 155, 680),
    (WINDOW_WIDTH - 155, 680),
)
