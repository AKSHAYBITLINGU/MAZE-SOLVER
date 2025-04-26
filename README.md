# MAZE-SOLVER

## Description
Maze Solver is a Python application that generates and solves a rectangular maze using a graphical interface built with Tkinter. The maze is created using a randomized depth-first search algorithm, and a recursive backtracking algorithm finds a path from the top-left entrance to the bottom-right exit. The visualization displays the maze generation and solving process with animated steps.

## Features
- Generates a customizable maze with specified rows and columns
- Visualizes the maze creation process with red walls
- Solves the maze and highlights the path in red (backtracks in gray)
- Supports dynamic window sizing with adjustable cell sizes
- Includes unit tests for maze cell creation
- Animated rendering of maze generation and solving

## Prerequisites
- Python 3.6 or higher
- Tkinter (included with standard Python installations)
- `tk` library (version 0.1.0, as specified in `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AKSHAYBITLINGU/maze-solver.git
   ```
2. Navigate to the project directory:
   ```bash
   cd maze-solver
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main application:
   ```bash
   python app.py
   ```
2. A window titled "MAZE SOLVER" will open, displaying a 6x8 maze (default configuration).
3. Watch the maze being generated, followed by the solver finding a path from the top-left to the bottom-right.
4. Close the window to exit the application.

To customize the maze size or window dimensions, modify the `main()` function in `app.py`:
- `num_rows`: Number of rows in the maze
- `num_cols`: Number of columns in the maze
- `screen_x`, `screen_y`: Window dimensions
- `margin`: Border around the maze

## Running Tests
The project includes unit tests to verify maze cell creation. To run the tests:
```bash
python -m unittest tests.py
```

## Project Structure
- `app.py`: Main application code, including maze generation, solving, and visualization logic
- `tests.py`: Unit tests for the `MAZE` class
- `requirements.txt`: Lists project dependencies

## Dependencies
- `tk==0.1.0` (Tkinter interface for Python)

## Notes
- The maze is drawn with red walls, and walls are removed (drawn in white) as the maze is generated.
- The solver uses a recursive backtracking algorithm, marking visited cells and drawing the path in red. Backtracked paths are shown in gray.
- Animation speed is controlled by a 0.05-second delay in the `_animate` method in `app.py`. Adjust `time.sleep(0.05)` for faster or slower animations.
- The entrance is at the top-left (0,0), and the exit is at the bottom-right (last row, last column).

## Contributing
1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, open an issue on GitHub or contact [akshaybitlingu786@gmail.com](mailto:akshaybitlingu786@gmail.com).
