# Snake Game

A classic Snake Game implementation using Pygame, following the [Clear Code tutorial](https://www.youtube.com/watch?v=QFvqStqPCRU).

## Overview

This is a modern implementation of the classic Snake game with graphical assets, sound effects, and increasing difficulty as you progress. The game has been refactored into a modular structure with each component having its own class and file.

![Snake Game Screenshot](assets/screenshots/gui.png)

## Requirements

- Python 3.6 or higher
- Pygame

### Controls
- Use the arrow keys to control the snake's direction
- Try to eat as many apples as you can without hitting the walls or yourself
- The snake will move faster as it gets longer, increasing the challenge

## Credits

This game was created by following the [Clear Code Pygame tutorial](https://www.youtube.com/watch?v=QFvqStqPCRU&t=1818s), with additional refactoring into a modular code structure.

### Modifications from the Original Tutorial

- Code has been restructured into separate files for better organization
- Fixed an issue with speed adjustment that could cause the game to crash
- Added proper dependency injection between components
- Implemented a proper game reset mechanism

## License

This project is open-source and available under the MIT License.

## Future Improvements (maybe, or maybe not)

- Add a start menu
- Repeating walls mode
- High score tracking
- Different types of fruits with special effects, maybe a boss fruit?
- Create different difficulty levels
- Add obstacles in higher levels