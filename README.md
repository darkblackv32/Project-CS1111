# README.md

## Summary
We start by importing the `colorama` library, which will be very helpful for painting our world. Following this, we create the function `draw_worldempty()` to draw the size of the world; our world will be 30x20 in size, and we paint the background white using the imported `colorama` library. Next, we create the function `draw_world()` to enable drawing each of the objects in our world, such as trees, rocks, the sun, the ground, and the river. When painting, we choose to paint matrix by matrix, which seemed easier, all thanks to the `colorama` library. After that, we create the function `draw_player()` based on the previous step, starting by drawing the world just as we did in the `draw_world()` function and adding the player. We continue the same process used to paint our world, matrix by matrix, placing the player at position (2,11) so that the selector is at (3,11). We then create the function `move_player(option)` to allow the player to move by inputting: top, down, right, or left. Finally, we create two functions, `collect_block(option)` and `destroy_blocks(option)`. The first function is used to collect wood and stone blocks, while the second function destroys the ground, grass, sun, and water.

## Introduction
Our project is inspired by the famous game “Minecraft,” a very entertaining construction and adventure video game that allows players to discover new worlds, build, and destroy objects within these worlds. We are sure you have heard of the game at some point or may have even played it. The project is called “Minecraft 2D XYZ,” which, like the original video game, focuses on the placement and destruction of blocks. The world will consist of two-dimensional square objects or blocks that represent parts of our world and its nature.

We were truly impressed by the entire process of the project because, after having a clear idea, we were able to see the focus and development of each piece of code we wrote, resulting in a good outcome.

## Definitions
1. **The `colorama` library**: The main library that enables the visualization of the program with the ability to color the spaces occupied by strings.
2. **Global variable ‘world’**: The matrix representing the project’s scenario with which the code will work.
3. **Global variables ‘ESPACIONEGRO’, ‘AGUA’, and ‘PASTO’**: These simply represent the values that the pixels of the rectangular objects in the world will have; they have more than one pixel and possess a single color.
4. **The function ‘draw_worldempty()’**: Draws the white scenario of 30 x 20 with visible range and domain and formats the drawing so that each pixel within the matrix is uniformly spaced.
5. **The function ‘draw_world()’**: Draws the world according to the project’s indications with the sun, trees, rocks, soil, and water by changing the color of each pixel.
6. **The function ‘draw_player()’**: Similar to the previous function, it draws the world in the same way but with the player’s avatar included.
7. **The function ‘move_player()’**: With this function, the user can move the character within the game using the commands: ‘top’, ‘left’, ‘right’, and ‘down’. If an attempt is made to move outside the boundaries, the program returns ‘Invalid operation’ instead of moving the character. After any command, the program ends.
8. **Variable ‘option’**: A variable whose value is determined by input and is used for the `move_player` function to move the player.
9. **Variable ‘d’**: Used to input `init` and run the program.

## Program Functionality
Upon starting the program, it imports the `Back` and `init` commands from the `colorama` library and then configures the `init` autoreset. The global variable `world` is assigned a matrix with 21 rows and 32 columns. Each individual value in the matrix is a string of 4 spaces colored white using `Back.LIGHTWHITE_EX`. Then, the global variables `ESPACIONEGRO`, `AGUA`, and `PASTO` are created with the values they will have in the rectangular objects in the world. Finally, before moving on to the rest of the code, a blank print is executed for better organization in the program's execution.

Next, the program requests input to start; entering `init` is required for the rest of the code to run. After that, it asks for the input of `option` for movements, but this can be omitted by pressing enter, and the program welcomes you to the world.

### Defining the function `draw_worldempty()`
In this function, all values in the first row and column of `mapa` are converted to numbers from 0 to 30 and from 0 to 20 respectively, using nested loops with a conditional for row #0 and a conditional for the first value of each row. Then, all values in the matrix are printed in an orderly format using another nested loop. As long as the value is less than or equal to 30 within the row, the value is printed with `end=''` to ensure the entire row appears on a single line; if the value equals 31, a blank print is executed as a row separator.

### Defining the function `draw_world()`
We begin drawing the black space, followed by grass and water using nested loops that plot them within a specified domain and range, changing white pixels to their respective colors using the global variables created earlier: `ESPACIONEGRO`, `PASTO`, and `AGUA`, without touching the numbers or going outside the scenario boundaries. We then plot the remaining objects in the world, changing values individually with `colorama` commands, as we felt it would be simpler that way. Each object was drawn in an organized and classified manner. We repeat the same procedure for stones, the sun, and other environmental objects, completing the function.

### Defining the function `draw_player()`
We color the player's avatar within the world.

### Defining the function `collect()`
Initially, we set the variables `countwood` and `countrock` to zero since they will be used later to count the number of times `extract` is executed. Additionally, `xi` and `yi` indicate the player's hand position, while `zx` and `zy` are used to sum the amount of space the player moves from the start, which is essential for the conditionals below. Conditionals are placed to identify the player's hand position and check if it is on a stem or a stone. Upon identification, the location where `extract` is executed is painted white, and counting is done according to whether it’s `countwood` or `countrock`. The function returns these two values for use in `move_player`.

### Defining the function `move_player()`
Since a loop will be implemented later, necessary variables are created to store the player's position coordinates each time a loop runs. Inside the loop, the world is drawn. If the `option` (input) is different from ‘no’, a variable equal to the world is created, and the commands to execute actions or terminate the code are determined. This function receives the movement commands ‘top’, ‘left’, ‘right’, and ‘down’, moving the character one pixel in the indicated direction. While it can execute multiple commands, the parameter only receives one string; therefore, a `.split()` is used to execute them one after another. The coordinates (x, y) of the player’s parts are then defined. In the list of movement commands, the coordinate variables are modified according to the amount and type of commands entered using a `for` loop with conditionals, painting the player's initial position white before modifying the avatar’s coordinates. With `draw_world`, we repaint the areas left blank after removing the previous avatar. Here, we also execute the functions `collect` and `destroy` if their respective commands were in `option`. The amounts of collected objects are added to `wood` and `rock` depending on the position of the variable in the return of `collect()`.

Afterwards, the program changes the values in the matrix to the avatar using the function `draw_player` at the new position, with a conditional based on its coordinates, and prints it along with the count of the collected blocks. If the coordinates do not meet the conditional—i.e., if the commands entered modify the avatar’s coordinates to values outside the matrix and thus exceed the world boundaries—the previous code within the conditional does not execute, returning the string ‘invalid operation’.

### Defining the function `destroy()`
The function receives the coordinates of the player’s hand. The code checks if the player’s hand would occupy any coordinates of destructible blocks and changes it to a blank space accordingly. This process is repeated for the rest of the blocks of water, grass, and the sun present in the world.

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
1. This code is iterative, so actions taken by the player within the world cannot be undone or changed once the code is executed unless it is run again.
2. Teamwork, communication, and a common space where the entire team could access the program, like GitHub, were vital to the project’s development. Organization simplified the process, ensuring everyone understood the code despite the division of labor.
3. The most challenging part of the project was implementing the `
