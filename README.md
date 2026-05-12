# Tic-Tac-Toe AI (Human vs Computer)

This is a simple Tic-Tac-Toe game built using Flask where a human plays as **X** and the computer plays as **O**. The AI uses the **Minimax algorithm**, so it plays optimally and is quite hard to beat.

## How it works

* The board is a 3x3 grid (9 cells total)
* Player always goes first as **X**
* Computer responds as **O**
* The AI calculates the best possible move using Minimax
* Game ends when someone wins or all cells are filled

## AI Logic

The computer doesn’t just pick random moves. It checks all possible future moves and chooses the one that gives the best outcome for itself and worst for the player. This is done using the **minimax algorithm**.

## Features

* Play against an unbeatable AI
* Automatic win/draw detection
* Reset button to restart the game
* Simple UI with clickable grid

## Tech Stack

* Python (Flask)
* HTML, CSS, JavaScript

## Run it locally

```
python app.py
```

Then open:

```
http://127.0.0.1:5000/
```

## Project structure

* `app.py` → backend logic + AI
* `templates/index.html` → frontend UI
* `static/style.css` → styling
* `.gitignore` → ignores unnecessary files

## Note

The AI is strong because it checks every possible move (so it won’t lose easily unless you make a mistake)


