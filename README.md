# Catch The Dot

This repository contains scripts which allow users to play a simple catch-the-dot game using their hands and a webcam.

## Getting Started

In order to run the software for the first time, execute the steps below:
1. Open your terminal
2. Navigate to the directory where you want to download the codebase
3. Run the following commands in order:
4. ```git clone ..```
5. ```cd catchthedot```
6. ```conda env create -f environment.yml```
7. ```conda activate catch_the_dot_game```
8. ```pip install mediapipe```
9. ```python Game.py --n_players <x>```

The subsequent times when you want to play the game, this simplifies to:
1. Open your terminal
2. Navigate to the catchthedot folder
3. ```conda activate catch_the_dot_game```
4. ```python Game.py --n_players <x>```

## Playing the Game

When executing the Python script Game.py, you can choose to play in single-player mode or multi-player mode by providing the 'n_players' parameter accordingly.
To start a single-player game: ```python Game.py --n_players 1```
To start a multi-player game: ```python Game.py --n_players 2```


