# ETCH-A-Sketch App

This is a Python-based ETCH-A-Sketch application that uses the turtle graphics library to create an interactive drawing experience controlled by keyboard inputs. It simulates the classic ETCH-A-Sketch toy in a digital format.

## Features

- Control the drawing cursor using keyboard inputs
- Create continuous lines by moving the cursor
- Clear the screen to start a new drawing
- Adjustable line thickness and color

## Controls

- 'w': Move cursor up
- 's': Move cursor down
- 'a': Move cursor left
- 'd': Move cursor right
- 'c': Clear screen (shake the ETCH-A-Sketch)
- Click on the screen to exit the program

## Requirements

- Python 3.x
- turtle module (typically comes pre-installed with Python)

## How to Run

1. Save the code in a file named `etch_a_sketch.py`
2. Open a terminal or command prompt
3. Navigate to the directory containing the file
4. Run the command: `python etch_a_sketch.py`

## Customization

You can easily customize the ETCH-A-Sketch by modifying the following parameters in the code:

- `tim.pensize(5)`: Change the number to adjust the line thickness
- `tim.color('blue')`: Change 'blue' to any other color name or RGB value
- Adjust the `forward()` and `backward()` functions to change the step size

## Extending the App

Here are some ideas to extend the functionality of your ETCH-A-Sketch app:

1. Add diagonal movements (e.g., 'q' for up-left, 'e' for up-right)
2. Implement a color-changing feature
3. Add an "undo" function to remove the last line drawn
4. Create a simple GUI with buttons for common actions

Feel free to expand on this program and make it your own!

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Author

Created by HS160
