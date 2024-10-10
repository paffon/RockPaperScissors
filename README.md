# Rock Paper Scissors Game

This is a Python implementation of the classic Rock-Paper-Scissors game, designed with extensibility and scalability in mind.

## Project Structure

- `rps/`: Contains the main game code, including classes for game logic, players, strategies, and user input handling.
- `assets/`: Contains text files used by the game, such as the game title.
- `data/`: Contains configuration files, including weapon relationships and names.
- `tests/`: Contains unit tests and input file verification scripts.
- `requirements.txt`: Lists the Python dependencies required to run the project.
- `Dockerfile`: Defines the Docker image for containerizing the application.
- `README.txt`: This file.

## Decisions

1. **Explicit Relationships**: Instead of a cyclic implementation, explicit relationships between rock, paper, and scissors are used. This design allows for easy addition of new weapons and special relationships in future development.
2. **Containerization**: The application is containerized using Docker to ensure consistency across different environments and to simplify deployment.

## Setup and Running the Game

### Prerequisites

- **Docker**: Ensure Docker is installed on your system.

### Building and Running with Docker

1. **Build the Docker image:**

   ```bash
   docker build -t rock-paper-scissors .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -it rock-paper-scissors
    ```
   
The `-it` flags allow you to interact with the game via the terminal.

## Running Locally without Docker
1. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```
2. **Run the game:**

    ```bash
    python rps/main.py
    ```

## Running Tests
To run the unit tests, add the root directory to the python path temporarily, and then run the tests.:

```bash
$env:PYTHONPATH="."
pytest tests
```

## Future Improvements
- **User Input Handling:** Implement a dedicated class for user input and verification to enhance code modularity.
- **Tournament Mode:** Develop a tournament class to support more than two players, including knock-out stages or multiplayer matches.
- **Online Multiplayer:** Add online features to enable remote play with friends.
- **Advanced Strategies:** Create an API for integrating more complex strategies that utilize the history of rounds to make smarter moves.
- **Enhanced Error Messages:** Improve error messages for user input validation to include specific failure reasons.
- **Game Statistics:** Provide end-of-game statistics such as choices made and player weaknesses.
- **Logging:** Replace print statements with a logging system for better message control and to facilitate muting in test environments.
- **User-Friendly Errors:** Refine error messages to be more user-friendly rather than developer-oriented.
