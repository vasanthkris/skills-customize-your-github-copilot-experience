
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Create the starting state for a Hangman game by selecting a secret word from a predefined list and initializing the variables needed to track the player's progress.

#### Requirements

Completed program should:

- Store several possible words in a list.
- Use the `random` module to select one secret word from the list.
- Track guessed letters, incorrect guesses, and the maximum number of incorrect guesses.

### 🛠️ Process Letter Guesses

#### Description

Create a game loop that asks the player for letter guesses and updates the displayed word as correct letters are discovered.

#### Requirements

Completed program should:

- Ask the player to enter a letter during each turn.
- Display the current progress with unguessed letters hidden, such as `_ _ _ _ _ _`.
- Reveal every position containing a correctly guessed letter.
- Update the incorrect-guess count when the player guesses a letter that is not in the secret word.

### 🛠️ End the Game

#### Description

Complete the game loop so that it ends when the player guesses the word or runs out of attempts, then reports the result.

#### Requirements

Completed program should:

- Stop when all letters in the secret word have been revealed.
- Stop when the player reaches the maximum number of incorrect guesses.
- Display a win message when the word is guessed.
- Display a lose message and reveal the secret word when attempts are exhausted.
