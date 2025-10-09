# Rock Paper Scissors

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

This project implements a predictive Rock-Paper-Scissors (RPS) player using a simple frequency-based strategy. The challenge in RPS is that most random or pattern-based opponents can be exploited if their move history is tracked. Our solution records the last few moves of the opponent, calculates the frequency of each move, and predicts the next move based on these probabilities. The player then chooses the counter move to maximize the chance of winning, while including a small random factor to avoid being predictable.

To test this project, simply download the repository and ensure Python 3.x is installed. Run the main.py file to simulate games between the predictive player and other strategies. No external libraries are required beyond Python’s standard library. The code is self-contained and ready for immediate simulation, making it easy to experiment with different opponents and track the player’s performance.

Alternatively, the solution can be run directly in Google Colab without any setup. Just upload the project files to a Colab notebook, ensure the working directory is set to the uploaded files, and run main.py using a code cell. This approach allows users to test and modify the player logic interactively without installing Python locally.
