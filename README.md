# 2D Volleyball

A local two-player volleyball game built with Python, Pygame, and Pymunk. Play as Poland or Brazil, with physics-based ball movement and keyboard controls.

Updated for compatibility with **Python 3.15**.

## Running the Game

### From source

Install Python 3.15 and the dependencies listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

From the project’s root directory, run:

```bash
cd code
python Volleyball.py
```

Keep the `res` folder inside `code`, as it contains the resources required by the game.

### Windows executable

Extract the entire `Volleyball.zip` archive and run `Volleyball.exe` from the extracted folder. Keep all bundled files and folders together. A separate Python installation is not required.

## Controls

| Action | Player 1 — Poland | Player 2 — Brazil |
|---|---|---|
| Move left | Left arrow | A |
| Move right | Right arrow | D |
| Jump | Up arrow | W |

| Key | Action |
|---|---|
| P | Pause or resume the game |
| V | Stop or play music |
| R | Restart after the match ends |
| Esc | Quit the game |

## Settings

Edit `res/Settings.txt` to adjust the window dimensions and target frame rate (FPS). When running from source, this file is located in `code/res/Settings.txt`.

## Credits

The music and images used in this project are licensed under Creative Commons.
