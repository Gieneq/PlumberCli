# Plumber Game
[![Python 3.9](https://img.shields.io/badge/python-3.9-green.svg)](https://www.python.org/downloads/release/python-390/)

Let water flow from the start to the end through ASCII pipes.

```text
  █A C E G I K M O Q S U W Y █
  █ B D F H J L N P R T V X Z█
▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
4 █╔╠╝╬═ ╚╬╣╣═╩╚╩╬╠╔╦ ╩╩╠╝╗╝╗█
3 █╬╗╣╚ ╬║╝╗╚══╣║╠╣╗║╣ ╝═ ╔╠╗█
2 █╦═╬═══╣╠╬╣╠╔╩═╬  ╬   ╦╦╩╗═█
1 █╬╚╚║╠╩╩╔ ║╗╗╣╗╔╠╬╔ ╠╣║╚╬  █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
```

## Usage



Simply run:
```shell
python plumber.py
```
You will see this small randomly generated game with basic instructions and prompt '=>':

```text
  █A C █
  █ B D█
▄▄█▄▄▄▄█
4 █╗╦╚╬█
3 █╬╝╠╦█
2 █╗╩╚║█
1 █╬╬╗ █
▀▀▀▀▀▀▀▀
Rotate pipes to let water flow e.g. 'A1l', 'c2rr', 'e1rlrlrl', 'h' for help, Ctrl-Z for exit.
=>
```

By typing 'a2l' then 'c2l' and finally 'c4r' you will solve the game:

```text
  █A C █
  █ B D█
▄▄█▄▄▄▄█
4 █╗╦╚╬█
3 █╬╝╠╦█
2 █╔╩╝║█
1 █╬╬╗ █
▀▀▀▀▀▀▀▀
Rotate pipes to let water flow e.g. 'A1l', 'c2rr', 'e1rlrlrl', 'h' for help, Ctrl-Z for exit.
=>c4r
Solved with 3 moves!
```

## Parameters
Parameters used to generate the board:
- --width - width e.g. '--width 8',
- --height - height e.g. '--height 5',
- --start - starting point x y e.g. '--start 0 0',
- --end - ending point x y e.g. '--end 7 4',
- --difficulty - board generation parameter e.g. '--difficulty easy'.

Be careful with start/end points - they should be within dimensions of the board.

## Algorithms
BFS is used to check connection between the start and the end. 

## TODO
- [ ] Fix: game can be not possible to solve.
- [ ] Fix: a randomly generated board is too random.
- [ ] Fix: start/end parameter are not concise with the board's coordinates.
- [ ] Add: DFS solution generation.
- [ ] Add: mixing pipe output's as difficulty parameter.