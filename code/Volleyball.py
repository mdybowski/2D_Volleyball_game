# Application entry point for the volleyball game.
from Game import Game

def open_settings(settings_path):
    """Read the window dimensions and target frame rate from the settings file."""
    try:
        with open(settings_path, 'r') as settings:
            f_line = settings.readline().split()
            window_size = (int(f_line[1].replace(',', '')), int(f_line[2]))
            fps = int(settings.readline().split()[1])
    except IOError:
        # Use defaults if the file cannot be opened or read.
        print("Can't load settings")
        print('Opening with settings: window_size = (1200, 650); fps = 60')
        window_size = (1200, 650)
        fps = 60

    return window_size, fps


def run_game():
    """Load configuration before creating the game and its resources."""
    window_size, fps = open_settings(Game.SETTINGS)

    game = Game(window_size, fps)

    while True:

        game.interface()

        game.step()


if __name__ == '__main__':

    run_game()
