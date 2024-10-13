# Minecraft 2D XYZ

## Overview

Minecraft 2D XYZ is a project inspired by the popular game "Minecraft," designed to create a simple 2D world where players can explore, build, and destroy objects. This project leverages the `colorama` library to enhance the visual experience by allowing colored outputs in the console.
We were truly impressed by the entire process of the project because, after having a clear idea, we were able to see the focus and development of each piece of code we wrote, resulting in a good outcome.

## Features

- **World Creation**: Generates a 30x20 world grid with various objects such as trees, rocks, water, and more.
- **Player Movement**: Move the player character using commands (up, down, left, right).
- **Resource Collection**: Collect wood and stone blocks from the environment.
- **Building and Destroying**: Build with collected resources and destroy certain blocks.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/minecraft-2d-xyz.git
   cd minecraft-2d-xyz
   ```

2. Install the `colorama` library if not already installed:
   ```bash
   pip install colorama
   ```

## Usage

To run the program, execute the following command in your terminal:
```bash
python main.py
```

### Commands

- **init**: Start the game.
- **top**: Move the player up.
- **down**: Move the player down.
- **left**: Move the player left.
- **right**: Move the player right.
- **build**: Build with collected blocks.
- **extract**: Collect nearby resources.
- **destroy**: Destroy specified blocks.

## Functions

- `draw_worldempty()`: Initializes and displays a blank world.
- `draw_world()`: Draws the world with all its objects.
- `draw_player()`: Draws the player avatar in the world.
- `move_player(option)`: Moves the player based on input commands.
- `collect_block(option)`: Collects resources from the world.
- `destroy_blocks(option)`: Destroys specified blocks.

## Summary
We start by importing the `colorama` library, which will be very helpful for painting our world. Following this, we create the function `draw_worldempty()` to draw the size of the world; our world will be 30x20 in size, and we paint the background white using the imported `colorama` library. Next, we create the function `draw_world()` to enable drawing each of the objects in our world, such as trees, rocks, the sun, the ground, and the river. When painting, we choose to paint matrix by matrix, which seemed easier, all thanks to the `colorama` library. After that, we create the function `draw_player()` based on the previous step, starting by drawing the world just as we did in the `draw_world()` function and adding the player. We continue the same process used to paint our world, matrix by matrix, placing the player at position (2,11) so that the selector is at (3,11). We then create the function `move_player(option)` to allow the player to move by inputting: top, down, right, or left. Finally, we create two functions, `collect_block(option)` and `destroy_blocks(option)`. The first function is used to collect wood and stone blocks, while the second function destroys the ground, grass, sun, and water.

## Definitions
1. **The `colorama` library**: The main library that enables visualization of the program with the capability to paint the spaces occupied by strings.
2. **Global variable `world`**: The matrix that represents the project’s environment that the code will work with.
3. **Function `draw_worldempty()`**: Draws the blank 30x20 environment with visible range and domain, formatting the drawing so that each pixel within the matrix is evenly spaced. However, only a certain number of pixels will be shown, which will increase as the player changes position.
4. **Function `draw_world2empty()`**: Draws the complete 40x20 environment with changes modified by user actions. This function works based on the previous function.
5. **Function `draw_world()`**: Draws the world according to project specifications, including the sun, trees, rocks, soil, and water by changing the color of each pixel.
6. **Function `draw_player()`**: Similar to the previous function, draws the world in the same way but includes the player’s avatar.
7. **Function `move_player()`**: This function allows the user to move the character within the game using the commands: ‘top’, ‘left’, ‘right’, and ‘down’. If an attempt is made to move outside the limits, the program returns ‘Invalid operation’ instead of moving the character. The program ends after any command.
8. **Function `build()`**: Allows the player to build with red blocks in the world.
9. **Variable `option`**: A variable whose value is determined by input and is used to execute the `move_player()` function and move the player.
10. **Option “init”**: The “init” option is a command to execute the code, which activates the previously described functions and develops them whenever called.

## Program Functionality
Upon starting the program, the `Back` and `init` commands from the `colorama` library are imported, followed by configuring the autoreset of `init`. Then, the global variable `world` is assigned a matrix created with list comprehension consisting of 21 rows and 32 columns. Each individual value within the matrix is a string of 4 spaces colored white using `Back.LIGHTWHITE_EX`. Next, these are set as global variables so they influence the entire developed code. The variable “world2” helps store changes made in “world,” so if the character moves and any function is executed, this variable will retain that function with the applied modification.

From the module, the functions `draw_worldempty()`, `draw_world()`, `move_player()`, `draw_world2empty()`, and `draw_world2()` from `main.py` are imported. A `main()` function is then created where the previous functions are called within a `while True` loop. Additionally, the program prompts for input to start the program, requiring “init” to execute the rest of the code. After that, the movements of the avatar are input, but “init” will not be requested again, and the program will execute.

### Functions `draw_worldempty()` and `draw_world2empty()`
In this function, all values in the first row and column of ‘map’ are converted to numbers from 0 to 40 and from 0 to 20 respectively using nested loops, applying a condition for row #0 and another for the first value of each row. Afterward, all values of the matrix are printed in an ordered format using another nested loop. As long as the value is less than or equal to 40 within the row, the value is printed with ‘end = ''’ to display the entire row on a single line; if the value equals 41, an empty print is executed as a row separator.

### Function `draw_world()`
The black space is drawn first, followed by grass and water using nested loops that graph them within a determined domain and range, changing white pixels to their respective colors using the global variables created earlier: `ESPACIONEGRO`, `PASTO`, and `AGUA`, without touching the numbers or going outside the edges of the environment. The other world objects are then graphically represented by changing individual values with `colorama` commands. We chose to do this one by one, as it seemed simpler, but they were also drawn in an orderly and classified manner. We repeat the same procedure for stones, the sun, and other environmental objects, concluding this function.

### Function `draw_player()`
The player avatar is colored within the world.

### Function `fill()`
This function compares world 1 with world 2, painting world 2 white if it detects that world 1 is red.

### Functions `tree`, `stone`, and `destroy()`
World ‘world2’ is called so that the first world is not drawn, allowing the functions to persist in the world. The `tree` function identifies whether the player’s hand is in red, indicating they are on a tree trunk.

### Function `collect()`
Initially, the variables `countwood` and `countrock` start at zero, as they will be used later to count the number of times extraction occurs. Additionally, `xi` and `yi` serve to verify that the player’s hand is in the same space as a tree or stone; if so, it returns the destroyed block counter.

### Function `build()`
This function allows players to build wood and stone blocks where necessary. It is essential to consider that the block where the construction will occur must be empty. The character must have collected blocks to perform this operation; if conditions are not met, the message “Invalid operation” will be displayed.

### Function `move_player()`
As a loop will be implemented later, the necessary variables are created to store the player’s position coordinates and the initial conditions of the camera and limit. In a `while True` loop, the world is drawn, a variable equal to the world is created, and commands are determined for actions or code termination. This function receives movement commands and can execute multiple commands, but the parameter only accepts a single string. Therefore, it uses `.split()` to execute them one after another. A loop changes the coordinates of the player’s pixels to allow for movement afterward.

To ensure the avatar follows the proposed actions, a loop is implemented for movement commands ‘top’, ‘left’, ‘right’, and ‘down’ that move the character one pixel in the indicated direction according to the number of commands entered. Before modifying the avatar’s coordinates, the program paints its initial position white. Additionally, a `while` loop makes the camera move alongside the player when moving right or left. If it reaches column 40, it stops moving; the map will not move further, but the player can continue moving. This condition applies to left or right movements as well.

Afterward, the `collect`, `destroy`, and `build` functions are executed if their respective commands were present in ‘option’. The quantity of collected objects is added to `wood` and `rock`, depending on the variable position in the `collect()` return. The program then changes the values within the matrix to the avatar using the `draw_player()` function in the new position with a condition on its coordinates, modifying the character’s position and the camera’s position, printing it along with the count of collected blocks in a “draw world 2.”

However, if the coordinates do not meet the condition (i.e., the entered commands modify the avatar's coordinates to values outside the matrix, attempting to exceed the world’s limits), the previous code within the condition does not execute, returning the string ‘invalid operation.’

### Function `destroy()`
The function receives the coordinates of the player’s hand. The code changes the color of the block selected by the player’s hand in ‘world’ and...


## Examples of Execution
For execution examples, the inputs and outputs of each will be taken into account.
- **Example 1:**
  - Input: $init
  - Output:
![image](https://github.com/user-attachments/assets/7905fa63-0c07-405a-b3df-3c6bd141f536)

  - Input: $30 right
  - Output:
![image](https://github.com/user-attachments/assets/bc6fa199-8cd5-4723-818d-d0a23218a0aa)

- **Example 2:**
  - Input: %init
  - Output:
![image](https://github.com/user-attachments/assets/864a5195-2bcd-4332-9944-c3a517ea199a)

  - Input: $34 right
  - Output:
![image](https://github.com/user-attachments/assets/45242faf-e378-4a5e-8b8d-65d4e9a70ff6)

  
- **Example 3:**
  - Input: %init
  - Output:
![image](https://github.com/user-attachments/assets/13e923b4-cbdd-4430-a319-14fe62ae92be)

  - Input: $2 right extract
  - Output:
![image](https://github.com/user-attachments/assets/65e919d4-43c0-4d50-83d6-cda49004364c)

  - Input: $2 right extract
  - Output:
![image](https://github.com/user-attachments/assets/5889c95c-738a-486a-b053-9431b91fa359) 


## Conclusions and Recommendations
### Conclusions:

1. This code is iterative, meaning players cannot undo or change their actions in the world once the code has been executed unless they restart the program.
2. Teamwork, communication, and a shared space like GitHub were vital in the development of this project. Organization simplified the process so that everyone understood the code, despite the division of labor.
3. The most challenging part of the project was implementing the `draw_emptyworld` function, as it was the starting point, and we lacked a clear idea of how to begin. Once we resolved that, the rest of the process was much quicker because we had defined the path we needed to follow.
4. We have gained a deeper understanding of the functionality, traversal, and use of matrices in practical applications, as the code mainly revolves around manipulating them.

### Recommendations

1. Utilize recursion to expand the range of possibilities within the project, such as enabling construction.
2. Consider using other tools to facilitate the programming of this code, such as dictionaries for certain variables.
3. Manage the project timeline better; we started the project late in this instance. Organizing our time effectively is advised.
4. Store pixel values in variables to achieve a less tedious drawing of objects, resulting in cleaner code.

### Errors

- While we have all the functions, they are not fully implemented. In the `destroy()` function, it's possible to execute the command, but it does not paint the block white. A similar issue occurs in the `collect()` function, where extraction and counting work, but subsequent movements do not repaint the area white, losing the record. We strongly believe the problem lies in how we create a new scenario that retains the character's previous movements; the `while` loop behaves like a snapshot, erasing and recreating the character. We attempted using `Back.LIGHTWHITE`, but it seems this is not iterating correctly in the code.
- Additionally, when entering a second movement in world 2, the world did not repaint, showing only the player. We had to review the code to ensure the world repainted correctly during the second movement through world 2.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

## Acknowledgments

- Inspired by the game "Minecraft."
- Special thanks to the creators of the `colorama` library.
