# Project: Arnav' TicTacToe
  -  This is a two-player console TicTacToe game where X and O take turns choosing positions on a 3×3 board until someone wins or the game ties.
## Features
  - Text-based 3×3 board that updates after every move.
  - Turn-based play with automatic switching between X and O.
  - Win and tie detection for rows, columns, and diagonals, with winner/tie messages.
## How it works
  - The board is stored as a list of 9 elements, each position starting as "-".
  - A loop repeatedly prints the board, asks the current player for a move (1–9), and places their symbol if the spot is free.
  - After each move, functions check for winning combinations or a full board; if found, the loop stops and the result is printed.
## What i learned 
  - This project teaches how to use functions, loops, and conditional statements together to manage game state and implement real game rules in code.
## Improvement
  - Add input error handling so if a player types something that isn’t a number 1–9, the game shows a message and asks again instead of crashing or wasting a turn. 
