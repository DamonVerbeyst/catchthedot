# Catch The Dot

This repository contains scripts which allow users to play a simple catch-the-dot game using their hands and a webcam.

## Getting Started

In order to prepare for your first execution of the script, execute the steps below:

1. Open your terminal
2. Navigate to the directory where you want to download the codebase
3. Run the following commands in order:
4. ```git clone ..```
5. ```cd catchthedot```
6. ```conda env create -f environment.yml```
7. ```conda activate catch_the_dot_game```
8. ```pip install mediapipe```

These steps will create a virtual conda environment, which allows you to use the same library versions that were used for the development of the game.
In order to exit the virtual environment, run: ```conda deactivate```


## Playing the Game

In order to actually play the game, execute the steps below:
1. Open your terminal
2. Navigate to the catchthedot folder
3. ```conda activate catch_the_dot_game```
4. ```python Game.py --n_players <x>```

When executing the Python script Game.py, you can choose to play in single-player mode or multi-player mode by providing the 'n_players' parameter accordingly.\\
To start a single-player game: ```python Game.py --n_players 1```\\
To start a multi-player game: ```python Game.py --n_players 2```


