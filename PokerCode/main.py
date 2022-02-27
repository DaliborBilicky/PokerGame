import src
import tkinter
import config as cf


def main():
    # Set window (Tk)
    window = tkinter.Tk()
    window.title(cf.WINDOW_TITLE)
    window.iconbitmap(cf.WINDOW_ICON)
    window.resizable(False, False)

    # Set my classes
    menu = src.GameMenu(window, cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT, cf.MENU_BG)
    game = src.Game(window, cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT, cf.GAME_BG)
    sett = src.GameSettings(
        window, cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT, cf.SETTINGS_BG
    )

    def start_menu():
        menu.display()
        menu.labels(cf.MENU_TITLE_POS, cf.MENU_TITLE_TEXT, cf.MENU_TITLE_FONT)
        for i in range(2):
            buttons_commands = (start_game, start_settings)
            menu.buttons(
                cf.MENU_BUTTONS_POS[i],
                cf.MENU_BUTTONS_SIZE,
                cf.MENU_BUTTONS_FONT,
                cf.MENU_BUTTONS_TEXT[i],
                cf.MENU_BUTTONS_COLOR,
                buttons_commands[i],
            )

    def start_settings():
        def back_to_menu_from_settings():
            sett.kill()
            start_menu()

        def save_settings():
            sett.save_settings(cf.SAVE_FILE_PATH, sett.return_color())
            # Restarts window
            window.destroy()
            main()

        menu.kill()
        sett.display()
        sett.color_options()
        window.bind(cf.MOUSE_BIND, sett.get_color_after_click)
        sett.entries(
            cf.SETTINGS_ENTRY_POS, cf.SETTINGS_ENTRY_BG, cf.SETTINGS_ENTRY_FONT
        )
        for i in range(2):
            buttons_commands = (save_settings, back_to_menu_from_settings)
            sett.labels(
                cf.SETTINGS_TEXT_POS[i],
                cf.SETTINGS_TEXT[i],
                cf.SETTINGS_TEXT_FONT[i],
            )
            sett.buttons(
                cf.SETTINGS_BUTTONS_POS[i],
                cf.SETTINGS_BUTTONS_SIZE,
                cf.SETTINGS_BUTTONS_FONT,
                cf.SETTINGS_BUTTONS_TEXT[i],
                cf.SETTINGS_BUTTONS_COLOR,
                buttons_commands[i],
            )

    def start_game():
        def back_to_menu_from_game():
            game.restart()
            game.kill()
            start_menu()

        def real_restart():
            game.restart()
            game.kill()
            start_game()

        menu.kill()
        game.display()
        game.shuffle_deck()
        for i in range(7):
            buttons_commands = (
                game.deal_cards,
                game.first_turn,
                game.second_turn,
                game.final_turn,
                game.showdown,
                real_restart,
                back_to_menu_from_game,
            )
            game.buttons(
                cf.GAME_BUTTONS_POS[i],
                cf.GAME_BUTTONS_SIZE,
                cf.GAME_BUTTONS_FONT,
                cf.GAME_BUTTONS_TEXT[i],
                cf.GAME_BUTTONS_COLOR,
                buttons_commands[i],
            )

    start_menu()
    window.mainloop()


if __name__ == "__main__":
    main()
