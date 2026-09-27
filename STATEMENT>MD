# PROBLEM STATEMENT:

Many beginner-level games provide simple number-guessing functionality but lack structured difficulty levels, attempt management, meaningful feedback, and scoring mechanisms. Players may also enter invalid data, which can cause a program to terminate unexpectedly if input is not handled properly. A simple guessing game can therefore be used to demonstrate how programming concepts such as random number generation, conditional statements, loops, functions, exception handling, and user input validation work together in a practical application.

This project solves this problem by providing an interactive command-line number guessing game that generates a random secret number, allows the player to select a difficulty level, limits the number of attempts, provides feedback and dynamic hints, and maintains a cumulative score throughout the game session. The program is lightweight, easy to execute, and provides an engaging way to apply fundamental Python programming concepts.

# OBJECTIVES:

* Design the program around a single main Python function, `number_guessing_game()`, that manages the complete game flow from difficulty selection to scoring and termination.

* Provide three difficulty levels—Easy, Medium, and Hard—with different number ranges and maximum attempt limits to create progressively challenging gameplay.

* Generate a different secret number dynamically using Python's `random.randint()` function instead of using a fixed value.

* Provide clear feedback after every valid guess by informing the player whether the entered number is too high, too low, or correct.

* Implement a dynamic hint system that provides information about whether the secret number is even or odd after the third unsuccessful attempt.

* Use exception handling to safely manage invalid user input and prevent the program from terminating when non-numeric values are entered.

* Implement a score calculation system that rewards players with higher scores when they identify the secret number using fewer attempts.

* Provide a continuous interactive mode where players can start multiple rounds without restarting the Python program.

# SCOPE OF THE PROJECT:

## Functional Scope

**Difficulty-based gameplay:**
The program provides three selectable difficulty levels:

* Easy — numbers from 1 to 50 with 10 attempts.
* Medium — numbers from 1 to 100 with 7 attempts.
* Hard — numbers from 1 to 200 with 5 attempts.

**Random number generation:**
For every new round, the program generates a random secret integer within the selected difficulty range using Python's `random` module.

**Attempt management:**
The program tracks the number of valid guesses made by the player and prevents further guesses once the maximum number of attempts for the selected difficulty has been reached.

**Interactive feedback:**
After every valid guess, the program compares the player's input with the secret number and displays whether the guess is too low, too high, or exactly correct.

**Dynamic hint system:**
After the third unsuccessful attempt, the program checks the parity of the secret number using the modulo operator and displays whether the number is even or odd.

**Scoring mechanism:**
The program calculates the score according to the number of attempts used:

```text
Score = (Maximum Attempts - Attempts Used + 1) × 10
```

Using fewer attempts therefore produces a higher score for that round. Scores are accumulated throughout the current game session.

**Input validation and exception handling:**
The program uses `try-except` with `ValueError` to handle non-integer input. Invalid difficulty selections are also detected and the user is asked to select a valid option.

**Continuous game session:**
After completing a round, the player can return to the difficulty menu and start another round. The cumulative score is maintained until the player chooses the exit option.

**Game termination:**
The player can select the Exit Game option at any time from the difficulty-selection menu. The program then displays the final accumulated score and terminates.

## Non-functional Scope:

**Fast execution:**
The program performs all calculations locally and responds immediately to user input. Since there are no network requests or external services, each operation requires minimal processing time.

**No external dependencies:**
The project uses Python's built-in `random` module and standard Python language features. No third-party packages or external libraries are required.

**Simple and intuitive:**
The menu-driven interface clearly displays the available difficulty levels, attempt limits, and exit option, making the game easy to understand for beginner users.

**Reliable input handling:**
Invalid numeric input is handled using exception handling instead of allowing the program to terminate unexpectedly. Invalid menu choices are also rejected and the user is prompted again.

**Maintainable structure:**
The main game logic is organized inside the `number_guessing_game()` function, while the `if __name__ == "__main__":` condition controls program execution when the file is run directly.

# TARGET AUDIENCE:

**Python and computer science students** who want to understand fundamental concepts such as loops, conditional statements, functions, exception handling, random number generation, and user input through a practical project.

**Beginner programmers** who want to learn how individual Python concepts can be combined to create a complete interactive command-line application.

**Programming instructors and educators** who need a simple project for demonstrating control flow, input validation, functions, and basic game logic.

**Casual users and gaming enthusiasts** who want a lightweight command-line guessing game that provides different difficulty levels, limited attempts, hints, and a cumulative scoring system.
