# Ayoub Chess – CS50 Final Project

#### Video Demo: [https://youtu.be/NIbBauF8NXk](https://youtu.be/NIbBauF8NXk)  
#### GitHub Repository: [https://github.com/AYOUB-CODING1/ayoub_chess](https://github.com/AYOUB-CODING1/ayoub_chess)  
#### Author: Ayoub  
#### edX Username: ayoub-coding  
#### City: Casablanca, Morocco  
#### Date: July 2025  

## Description

**Ayoub Chess** is a simple two-player chess game written in Python using the Pygame and `python-chess` libraries. This is my final project for the CS50x 2025 course. It runs as a desktop application and provides a clean, user-friendly experience for playing chess locally on one computer.  

The idea behind this project was to create something fun, interactive, and not based on web development (which I'm less interested in). I also wanted to get hands-on experience with Pygame and graphical interfaces using Python.

The game includes basic features like drawing the board, selecting and moving pieces, highlighting valid moves, detecting check, and adding sound effects for moves and when a player is in check.

In the end, I compiled the game into a `.exe` file using `pyinstaller`, so that even non-programmers can run it easily.

---

## How to Run

1. Install Python 3 on your system.
2. Install dependencies by running:  
   `pip install pygame chess`
3. Run the program:  
   `python main.py`

To run the `.exe` version, just double-click `ayoub_chess.exe` (included in the repo).

---

## File Structure

- `main.py`: This is the main file that runs the entire game. It handles the game loop, rendering, and user interaction.
- `chess_engine.py`: This file contains functions to draw the board, pieces, and move highlights. It’s where most of the rendering logic is located.
- `sounds/`: A folder that includes the sound effects: one for normal moves, and one when a player is in check.
- `images/`: A folder containing all chess piece images in `.png` format.
- `icon.ico`: The icon used for the `.exe` version.
- `ayoub_chess.exe`: Compiled executable for Windows.
- `README.md`: This file you are reading, explaining the project.

---

## Design Decisions

I chose to use `pygame` because I wanted full control over the graphics without needing a web browser or online platform. It also allowed me to use my own sound and image assets, which made the project more fun to build.

I used the `chess` library only for checking legal moves and game logic, not for rendering or AI. This way, I had freedom to design my own visuals.

Instead of focusing on online multiplayer or AI (which would have taken more time), I focused on making the local 2-player experience as smooth and clear as possible.

---

## Features

- Graphical 8x8 chessboard using Pygame.
- All pieces move according to standard chess rules.
- Highlights possible legal moves when a piece is selected.
- Plays a sound when a move is made.
- Special sound plays when one player is in check.
- Clean layout with a custom icon.
- Runs on both Python and as `.exe`.

---

## Future Improvements

In the future, I would like to:
- Add a basic chess engine for single-player mode.
- Add a timer for blitz games.
- Improve the design using animations or smoother transitions.
- Allow undoing moves and saving game progress.

---

## Conclusion

This project helped me learn a lot about Pygame, event loops, and how to organize a graphical Python app. It also pushed me to learn how to package Python apps for users who don’t code, using tools like `pyinstaller`.

I’m proud of how the game turned out, and I’m excited to keep improving it even after CS50. Thanks for reviewing my project!
