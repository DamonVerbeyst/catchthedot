#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:20:28 2024

@author: damon
"""

import sys
import argparse
from game_logic import single_player_game, double_player_game

def main():
    parser = argparse.ArgumentParser(description='Catch-The-Dot script with a configurable number of players.')
    parser.add_argument('--n_players', type=int, choices=[1, 2], required=True, help='Number of players (must be 1 or 2)')

    args = parser.parse_args()
    n_players = args.n_players

    if n_players not in [1, 2]:
        print("Error: n_players must be either 1 or 2.")
        sys.exit(1)

    print(f"Starting Catch-The-Dot game with {n_players} player(s).")

    if n_players == 1:
        print("Single player mode selected.")
        single_player_game()

    elif n_players == 2:
        print("Two player mode selected.")
        double_player_game()


if __name__ == '__main__':
    main()